from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import Context
from django.template.loader import get_template
from .forms import ContactForm
from .email import send_contact_email


def contact(request):
    form_class = ContactForm

    return render(request, 'contact/contact.html', {
        'form': form_class,
    })

def send(request):

    if request.method == 'POST':

        message = request.POST['sender_message']
        sender_name = request.POST['sender_name']
        sender_email = request.POST['sender_email']

        send_contact_email(sender_name, sender_email, message)

        return HttpResponseRedirect(reverse('contact:sent'))




def sent(request):
    return render(request, 'contact/sent.html')
