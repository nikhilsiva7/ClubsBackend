from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from .models import Events,EventRegistration
from django.contrib import messages



# Create your views here.
@login_required
def register_event(request,event_id):
    event=get_object_or_404(Events,id=event_id)

    if request.method=='POST':
        user=request.user
        user_mail=request.POST['email']

        if  EventRegistration.objects.filter(user=user,event=event).exists():
            messages.info(request,'You are already registered for this event')
            return redirect('register_event',event_id=event_id)
            
        else:
            EventRegistration.objects.create(user=user,event=event)
            


        html_message = render_to_string('email.html', {'user': user,"event":event})
        email=EmailMessage(
            subject='Thank you for registering',
            body=html_message,
            from_email='clubmanagement.dev@gmail.com',
            to=[user_mail],
            
        )
        email.content_subtype = "html"
        email.send()

        return render(request,"success.html",{"event":event})

    return render(request, 'form.html',{"event":event}) 