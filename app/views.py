from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, render, redirect
from .models import Text


# Create your views here.
def index(request):
    return render(request, 'home.html')

def find(request):
    if request.method == 'POST':
        title = request.POST.get('title_input')
        if title:
            return redirect(read, title=title)
    return render(request, 'find.html')

def read(request, title):
    try:
        text = get_object_or_404(Text, title=title)
        return render(request, 'page.html', {'title': text.title, 'text': text.text})
    except Http404:
        return render(request, 'empty.html')

def write(request):
    if request.method == 'POST':
        title = request.POST.get('title_input')
        text = request.POST.get('text_input')

        if len(title) <= 50 and text:
            obj, created = Text.objects.get_or_create(title=title,defaults={'text':text})

            if not created:
                obj.text = text
                obj.save()
            return redirect(read, title=title)
        
    return render(request, 'write.html')

def clear_all(request):
    Text.objects.all().delete()
    return HttpResponse('Cleared.')