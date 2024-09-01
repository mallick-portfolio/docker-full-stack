import smtplib
from email.mime.text import MIMEText
from django.core.management.base import BaseCommand
from todo.models import EmailQueue

class Command(BaseCommand):
    help = 'Send queued emails'

    def handle(self, *args, **kwargs):
        unsent_emails = EmailQueue.objects.filter(status=False, attempt__lt=3)

        for email in unsent_emails:
            try:
                # Set up the email
                msg = MIMEText(email.body)
                msg['Subject'] = email.subject
                msg['From'] = email.from_user
                msg['To'] = email.to
                msg['Cc'] = email.cc

                # Replace the following with your SMTP server configuration
                smtp_server = 'smtp.example.com'
                smtp_port = 587
                smtp_username = 'your_username'
                smtp_password = 'your_password'

                # Send the email
                with smtplib.SMTP(smtp_server, smtp_port) as server:
                    server.starttls()
                    server.login(smtp_username, smtp_password)
                    server.sendmail(email.from_user, [email.to] + [email.cc], msg.as_string())

                # Update the status and reset attempt count
                email.status = True
                email.attempt = 0
                email.save()
                self.stdout.write(self.style.SUCCESS(f'Successfully sent email to {email.to}'))
            
            except Exception as e:
                # Increment the attempt count if sending fails
                email.attempt += 1
                email.save()
                self.stdout.write(self.style.ERROR(f'Failed to send email to {email.to}: {str(e)}'))
