# Create your form views here.

from django.shortcuts import render
from django.http import HttpResponseRedirect
from contact.forms import ContactForm

def contact(request):
    if request.method == 'POST': # If the form has been submitted...
        form = ContactForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            cc_myself = form.cleaned_data['cc_myself']
            
            recipients = ['talilief@gmail.com']
            if cc_myself:
	            recipients.append(sender)
            
            from django.core.mail import send_mail
            send_mail(subject, message, sender, recipients)
			
            return HttpResponseRedirect('/thanks/') # Redirect after POST
    else:
        form = ContactForm(
		    initial={'subject': 'I love your site!'}) # An unbound form

    return render(request, 'contact.html', {
        'form': form,
    })
