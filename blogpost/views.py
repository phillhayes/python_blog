from django.shortcuts import render


from .models import Blogpost
# Create your views here.
def blogposts(request):
    blogposts = Blogpost.objects.all()
    return render(request, 'categories/show-all.html', {'categories': categories})

def blogpost_detail(request, pk):
    blogpost = Blogpost.objects.get(pk=pk)
    return render(request, 'blogpost/show.html', {'blogpost': blogpost})