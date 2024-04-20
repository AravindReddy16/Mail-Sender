from django.shortcuts import render,redirect
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from django.http import JsonResponse

# Create your views here.

def main(request):
    if request.method == 'POST':
        subject = request.POST.get('subject')
        body = request.POST.get('body')
        from_ = request.POST.get('from')
        passkey = request.POST.get('passkey')
        to = request.POST.get('to')

        settings.EMAIL_HOST_USER = from_
        settings.EMAIL_HOST_PASSWORD = passkey

        email = EmailMessage(
            subject,
            body,
            settings.EMAIL_HOST_USER,
            list(map(str,to.split(','))),
        )

        if request.FILES:
            file = request.FILES.get('file')
            email.attach(file.name,file.read(),file.content_type)

        email.fail_silently = True
        email.send()
        return redirect('main')
    return render(request,'App/index.html')