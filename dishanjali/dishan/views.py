# -*- coding: utf-8 -*-


from django.conf import settings
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Gallery, Registrationdetails
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ContactForms


def Index(request):
    context_dict = {'hello':'this is hrishabh patidar'}
    return render(request, 'dishan/index.html', context=context_dict)


def Motivation(request):
    context_dict = {'hello':'this is hrishabh patidar'}
    return render(request, 'dishan/motivation.html', context=context_dict)

def Involve(request):
    context_dict={'hello':'this is hrishabh patidar'}
    return render(request, 'dishan/involve.html', context=context_dict)


def Donate(request):
    context_dict={'hello':'this is hrishabh patidar'}
    return render(request, 'dishan/donate.html' , context=context_dict)


def Center(request):
    context_dict={'hello':'this is hrishabh patidar'}
    return render(request, 'dishan/center.html' , context=context_dict)



class About(ListView):
    template_name = 'dishan/about.html'
    model = Registrationdetails
    context_object_name = 'pdf'
    def get_queryset(self):
        return Registrationdetails.objects.all




class ContactView(ListView):
    template_name = 'dishan/contact.html'

    def get(self, request):
        forms = ContactForms()
        return render(request, self.template_name, {'form': forms, })


    def post(self, request):
        if request.method == 'POST':
            form = ContactForms(request.POST, request.FILES)
            if form.is_valid():
                post = form.save(commit = False)
                post.save()
                cd = form.cleaned_data
                subject = 'Query at NSBM Dishanjali'
                message = 'Thnak you {} we are glad that you contact dishanjali'.format(cd['first_name'])
                from_email = settings.EMAIL_HOST_USER
                to_list = [ cd['contact_email'], settings.EMAIL_HOST_USER, ]
                send_mail(subject,message,from_email,to_list,fail_silently=True)
                messages.success(request,'thank you for your query. We will contact you soon',)
                return HttpResponseRedirect('/dishan/index.html/')



            arg = {'form': form, }
        return render(request, self.template_name, arg)




def Event(request):
    context_dict={'hello':'this is event page'}
    return render(request, 'dishan/event.html/' ,context=context_dict)

class GalleryView(ListView):
    template_name = 'dishan/gallery.html'
    model = Gallery()
    context_object_name = 'photos'
    def get_queryset(self):
        return Gallery.objects.all()

    def gallery( self, request):
        return render(request, self.template_name, {'Gallery':Gallery})
