from django.shortcuts import render


from .models import Category
# Create your views here.
def categories(request):
    categories = Category.objects.all()
    return render(request, 'categories/show-all.html', {'categories': categories})

def category_detail(request, pk):
    category = Category.objects.get(pk=pk)
    return render(request, 'categories/show.html', {'category': category})