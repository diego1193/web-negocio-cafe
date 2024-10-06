from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm

# Create your views here.

def contact(request):
    # Ocurre GET cuando se llama la plantilla y ocurre POST cuando se llama el for 
    # print("Tipo de petición: {}".format(request.method))
    contact_form = ContactForm()

    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            # Enviamos el correo y redireccionamiento
            email = EmailMessage(
                "La Caffetiera: Nuevo mensaje de contacto",
                f"De {name} <{email}>\n\nEscribió:\n\n{content}",
                "no-contestar@inbox.mailtrap.io",
                ["diegocabrera1193@gmail.com"],
                reply_to=[email] # responder al usuario es mas sofisisticada
            )
            try:
                email.send()
                return redirect(reverse('contact')+"?ok") # 'reverse('contact') + "?ok"'
            except:
                return redirect(reverse('contact')+"?fail")
            

    return render(request, "contact/contact.html", {"form": contact_form})