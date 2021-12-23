from django import forms
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from website.models import Contact
from website.forms import NameForm,ContactForm,NewsletterForm

def index_view(request):
    return render(request, 'website/index.html')

def about_view(request):
    return render(request, 'website/about.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
    form = ContactForm()
    return render(request, 'website/contact.html') 

def newsletter_view(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')

def elements_view(request):
    return render(request, 'website/elements.html') 

def test_view(request):
    if request.method =='POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # name =form.cleaned_data['name']
            # email =form.cleaned_data['email']
            # subject =form.cleaned_data['subject']
            # message =form.cleaned_data['message']
            # print(name,email,subject,message)
            form.save()
            return HttpResponse('done')
        else:
            return HttpResponse('not valid')

    form = ContactForm()
    return render(request,'test.html',{'form':form})
    