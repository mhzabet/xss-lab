from django.shortcuts import render
from . import forms 
from .models import Stock
from django.contrib import messages

def home_view(request):
    return render(request, 'home/home.html')

## Lab 1
def xss_no_protection_view(request):
    if request.method == "GET":
        form = forms.xss_no_protection_form(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            result = Stock.objects.filter(item__contains=query)
            return render(request, 'vulns/reflected_xss/xss_no_protection.html', context={'result':result, 'query':query})
        
    return render(request, 'vulns/reflected_xss/xss_no_protection.html')

## Lab 2
def xss_brackets_protection_view(request):
    if request.method == "GET":
        form = forms.xss_brackets_protection_form(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            result = Stock.objects.filter(item__contains=query)
            return render(request, "vulns/reflected_xss/xss_brackets_escaping.html",context={'result':result, 'query':query})

    return render(request, "vulns/reflected_xss/xss_brackets_escaping.html")

## Lab 3
def xss_attributes_no_protection_view(request):
    if request.method == "GET":
        form = forms.xss_attributes_no_protection_form(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            result = Stock.objects.filter(item__contains=query)
            return render(request, "vulns/reflected_xss/xss_attributes_no_protection.html",context={'result':result, 'query':query})

    return render(request, "vulns/reflected_xss/xss_attributes_no_protection.html")

## Lab 4
def xss_javascript_context_no_protection_view(request):
    if request.method == "GET":
        form = forms.xss_javascript_context_no_protection_form(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            result = Stock.objects.filter(item__contains=query)
            return render(request, "vulns/reflected_xss/xss_javascript_context_no_protection.html",context={'result':result, 'query':query})

    return render(request, "vulns/reflected_xss/xss_javascript_context_no_protection.html")

## Lab 5
def xss_javascript_context_brackets_escape_view(request):
    if request.method == "GET":
        form = forms.xss_javascript_context_brackets_escape_form(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            result = Stock.objects.filter(item__contains=query)
            return render(request, "vulns/reflected_xss/xss_javascript_context_brackets_escape.html",context={'result':result, 'query':query})
    return render(request, "vulns/reflected_xss/xss_javascript_context_brackets_escape.html")
## Lab 6
def stored_xss_no_protection_view(request):
    if request.method == "POST":
        form = forms.stored_xss_no_protection_form(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "vulns/stored_xss/stored_xss_no_protection.html")
        else:
