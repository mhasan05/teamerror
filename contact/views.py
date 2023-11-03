from django.shortcuts import render,redirect
from django.views import View
from django.contrib import messages
from .models import Support

class ContactView(View):
    def get(self, request, *args, **kwargs):
        active_page = "Contact"
        data={
            'active_page': active_page
        }
        return render(request,'contact.html',data)
    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        set_contact = Support(name=name, email=email, message=message)
        set_contact.save()
        messages.success(request, 'Successfully Send message')
        return redirect('contact')

