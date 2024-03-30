from base.models import MailLog
from django.template.loader import render_to_string



from django.conf import settings
from django.core.mail import send_mail

import threading
# class EmailThread(threading.Thread):

#     def __init__(self, name):
#         self.name = name
#         threading.Thread.__init__(self)

#     def run(self):
#         print("Starting " + self.name)
#         flush_queue()

def flush_queue():
    from django.core import mail
    from django.core.mail import EmailMessage
    from django.conf import settings
    mails_to_send = MailLog.objects.filter(queue=True)
    sent_count = 0

    # Copy mail from database and update to Queue False
    # Append database queue to temp list 
    if mails_to_send:
        copy_mails_to_send = []
        for i in mails_to_send:
            copy_mails_to_send.append(i)
        mails_to_send.update(queue=False)

        # Check mail Connection
        try:
            connection = mail.get_connection()
        except Exception as e:
            print('Flush Queue mail Connection Error :',e)
            mails_to_send.update(queue=True)
            return False

        # Send mail 
        for email in copy_mails_to_send:
            subject = email.subject
            html_content = email.body
            from_email = settings.EMAIL_HOST_USER
            to = [settings.EMAIL_HOST_USER, 'info@touheed.education']

             
            try:       
                msg = EmailMessage(subject, html_content, from_email, to)     
                msg.content_subtype = "html"  # Main content is now text/html
                connection.send_messages([msg])
                sent_count += 1
            except Exception as e:
                print('Flush Queue Error :',e)
                email.update(queue=True)
                
        print("Sent {}/{} mails".format(sent_count, len(copy_mails_to_send)))
        connection.close()
    else:
        print(mails_to_send)
        print("No mails in queue")
    
    return True

def send_contact_form_mail(template_data):
    to = "admin@touheed.education"
    html_content = render_to_string('base/contact.html',context=template_data)
    subject = "Message From T.E Contact Form"
    ml = MailLog(to=to,subject=subject,body=html_content)
    ml.save()
    t1 = threading.Thread(target=flush_queue)
    t1.start()

    # subject = 'welcome to GFG world'
    # message = 'Hi x1, thank you for registering in geeksforgeeks.'
    # email_from = settings.EMAIL_HOST_USER
    # recipient_list = [settings.EMAIL_HOST_USER, ]
    # send_mail( subject, message, email_from, recipient_list )