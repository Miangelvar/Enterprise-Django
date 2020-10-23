from django.core.mail import EmailMessage
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from contact.forms import ContactForm


def contact(request):
    contact_form = ContactForm
    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            email = EmailMessage(
                "la Caffetiera: Nuevo mensaje de Contacto",
                "De {} <{}>\n\nEscribió:\n\n{}".format(name, email, content),
                "no-contestar@inbox.mailtrap.io",
                ["miguel.vargas.bejarano@unillanos.edu.co"],
                reply_to=[email]
            )

            try:
                email.send()
                return redirect(reverse('contact') + "?ok")
            except:
                return redirect(reverse('contact') + "?fail")

    return render(request, "contact/contact.html", {'form': contact_form})
