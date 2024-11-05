from django.shortcuts import render, redirect
from .forms import MediaForm

from .models import Media

def home(request):
    return render(request, 'home.html')

def gallery(request):

    media = Media.objects.all()

    return render(request, 'gallery.html', {'media': media})

def upload(request):
    if request.method == 'POST':
        form = MediaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redirect to a success page or index
    else:
        form = MediaForm()
    
    return render(request, 'upload.html', {'form': form})

def detail(request, pk):
    media = Media.objects.get(pk=pk)
    return render(request, 'detail.html', {'media': media})