from django.shortcuts import render, redirect
from .forms import ContactForm
from django.urls import reverse
from django.core.mail import EmailMessage

# Create your views here.

def contact(request):
    contact_form = ContactForm

    if request.method == "POST":
        contact_form = contact_form(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            #Enviamos el correo
            email = EmailMessage(
                "Nueva PQRS",
                "De {} <{}> \n\n Informa:\n{}".format(name,email,content),
                "no-contestar@inbox.mailtrap.io",
                ["custom.atencion.cliente@gmail.com"],
                reply_to=[email]
            )
            try:
                email.send()
                return redirect(reverse('contact') + "?ok")
            except:
                return redirect(reverse('contact') + "?fail")

    return render(request, "contact/contact.html", {'form': contact_form})
