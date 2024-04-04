import threading
from django.core.mail import EmailMessage as Email
from django.conf import settings
# from portal.constants import QUARTOLOOM_SOLUTIONS_MAILING_LIST


class EmailService(threading.Thread):
    def __init__(self, subject, body, recievers, to_cc=[], *args, **kwargs):
        self.email = Email(
            subject,  # subject
            body,  # body
            settings.EMAIL_HOST_NAME + " " + settings.EMAIL_HOST_USER,  # from mail
            list(set(recievers)),  # recievers
            cc=list(set(to_cc)),  # in cc
            # bcc=QUARTOLOOM_SOLUTIONS_MAILING_LIST
        )
        super(EmailService, self).__init__(*args, **kwargs)
    

    def run(self):
        self.email.send(fail_silently=True)

    def send(self,):
        self.start()    


