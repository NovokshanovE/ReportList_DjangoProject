from django.shortcuts import render
from django.shortcuts import get_object_or_404
# Create your views here.
from .models import TextFile, Image
from .models import Group

def section_view(request, section):
    files = TextFile.objects.filter(section=section)
    return render(request, 'textfiles/section.html', {'files': files, 'section': section})
def file_list(request, group_id):
    group = get_object_or_404(Group, id=group_id)
    files = TextFile.objects.filter(group_id=group)
    return render(request, 'textfiles/file_list.html', {'group': group,'files': files})





def file_detail(request, file_id):
    file = get_object_or_404(TextFile, pk=file_id)
    images = Image.objects.all()
    return render(request, 'textfiles/file_detail.html', {'file': file, 'images':images, 'group':file.group_id})


def about(request):
    return render(request, 'textfiles/about.html')


def home_view(request):
    groups = Group.objects.all()
    return render(request, 'textfiles/home.html', {'groups': groups})

