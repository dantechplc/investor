from django.utils import timezone

from accounts.models import Investment_profile, Client, Account, Investment
from transaction import EmailSender
from transaction.models import Transactions


def daily_roi():
    today = timezone.now()
    print("✅ Cron daily_roi ran at", today)

    investments = Investment_profile.objects.filter(status='Active', next_payout__lte=timezone.now())

    for investment in investments:
        print(f"Processing investment {investment.id} for {investment.user}, next payout: {investment.next_payout}, today: {today}")

        if investment.next_payout and investment.next_payout <= today:
            account_user = investment.user
            account_client = Account.objects.get(user=account_user)

            # Add interest
            interest = investment.earning
            account_client.roi_balance += interest
            account_client.total_roi_received += interest

            account_client.save(update_fields=['roi_balance', 'total_roi_received'])

            # Update investment profile
            investment.amount_earned += interest
            investment.next_payout = Transactions.get_next_payout(today)  # define this helper
            investment.save(update_fields=['amount_earned', 'next_payout'])

            # Record transaction
            trx = Transactions.objects.create(
                user=account_client,
                amount=interest,
                status='Successful',
                investment_name=Investment.objects.get(name=investment.investment),
                transaction_type='ROI',
                date=today,
            )

            # Send ROI email
            EmailSender.roi_success_email(
                user=account_user.user,
                amount=interest,
                balance=account_client.roi_balance,
                date=today,
                plan=Investment.objects.get(name=investment.investment),
                trx_id=trx.trx_id,
            )