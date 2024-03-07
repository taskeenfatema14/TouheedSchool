from base.models import MailLog
from base.utils import send_contact_form_mail


from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(["POST"])
def send_contact_mail(request):
    data = request.data

    contact_name = data['contact_name'] if  'contact_name' in data else "-"
    contact_email = data['contact_email'] if 'contact_email' in data else "-"
    contact_subject = data['contact_subject'] if 'contact_subject' in data else "-"
    contact_message = data['contact_message'] if 'contact_subject' in data else "-"

    template_data = {'contact_name':contact_name,'contact_email':contact_email,'contact_subject':contact_subject,'contact_message':contact_message}
    send_contact_form_mail(template_data)
    data = {'success':True, 'message':'Mail Send'}
    return Response(data)