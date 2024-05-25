from django.shortcuts import render
from django.shortcuts import get_object_or_404
# Create your views here.
from .models import TextFile, Image

def section_view(request, section):
    files = TextFile.objects.filter(section=section)
    return render(request, 'textfiles/section.html', {'files': files, 'section': section})
def home_view(request):
    files = TextFile.objects.all()
    return render(request, 'textfiles/home.html', {'files': files})





def file_detail(request, file_id):
    file = get_object_or_404(TextFile, pk=file_id)
    images = Image.objects.all()
    return render(request, 'textfiles/file_detail.html', {'file': file, 'images':images})