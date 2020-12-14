from django.shortcuts import (render, redirect,get_object_or_404,HttpResponseRedirect)
from django.http import HttpResponse
from django import forms
from .models import Blogger

class bloggerform(forms.ModelForm):
    class Meta:
        model = Blogger
        fields ="__all__"

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def blogger_create(request):
    context ={}
    form = bloggerform(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list/') # press refresh button to see the changes
    context['form'] = form
    return render(request, "BLOG_POSTS/post_form.html", context)

def blogger_list(request,template_name = 'BLOG_POSTS/post_list.html'):
    context = {}
    context["bloggers"] = Blogger.objects.all()
    return render(request,template_name,context)

def blogger_delete(request,id):
    context ={}
    obj = get_object_or_404(Blogger, id=id)
    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect("/")
    return render(request, "BLOG_POSTS/post_delete.html", context)



