from django.shortcuts import render

# Create your views here.
# image_app/views.py
from django.shortcuts import render, redirect
from .forms import ImageForm
from .models import Image

def image_list(request):
    images = Image.objects.all()
    return render(request, 'image_app/image_list.html', {'images': images})

def image_upload(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('image_list')
    else:
        form = ImageForm()
        data = Image.objects.all()
    return render(request, 'image_app/image_upload.html', {'form': form,'data':data})

def image_update(request, pk):
    image = Image.objects.get(pk=pk)
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES, instance=image)
        if form.is_valid():
            form.save()
            return redirect('image_list')
    else:
        form = ImageForm(instance=image)
    return render(request, 'image_app/image_upload.html', {'form': form})

def image_delete(request, pk):
    Image.objects.filter(pk=pk).delete()
    return redirect('image_list')
