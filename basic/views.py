from django.shortcuts import render
from .forms import ContactForm

# new imports that go at the top of the file
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template.loader import get_template


def About(request):
    return render(request, 'basic/about.html', {'title': 'About Us'})


def Services(request):
    return render(request, 'basic/services.html', {'title': 'Services'})


def Contact(request):
    form_class = ContactForm
    # new logic!
    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get(
                'contact_name'
            , '')
            contact_email = request.POST.get(
                'contact_email'
            , '')
            form_content = request.POST.get('content', '')
            # Email the profile with the
            # contact information
            template =\
                get_template('basic/contact_template.txt')
            context = {
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content,
            }
            content = template.render(context)

            email = EmailMessage(
                "New contact Insomniatic",
                content,
                "Insomniatic" + '',
                ['soorajytad@gmail.com','zanjeevztrex@gmail.com'],
                headers={'Reply-To': contact_email}
            )
            email.send()
            return redirect('contactsuccess')
    context = {
        'title': 'Contact Us',
        'form': form_class
    }
    return render(request, 'basic/contact.html', context)

def Contactsuccess(request):
    return render(request,'basic/contact_success.html',{'title':'Contact Form Submitted'})


def Terms(request):
    return render(request, 'basic/terms.html', {'title': 'Terms & Conditions'})
