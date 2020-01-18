from django.shortcuts import render,reverse
from .models import Article
# Create your views here.

def home(request):
    return render(request, 'base.html')

def articlelist(request):
    articles = Article.objects.all()
    ctx = {
        'articles': articles
    }
    return render(request,'core/listarticle.html', ctx)

def articledetail(request, pk):
    article = Article.objects.get(pk=pk)
    ctx = {
        'article': article
    }
    return render(request,'core/articledetail.html', ctx)


def articlecreate(request):
    if request.method == "POST":
        title = request.POST['title']
        author = request.POST['author']
        content = request.POST['content']
        article = Article.objects.create(title=title,author=author,content=content)
        ctx = {
            'article': article
        }
        return render(request,'core/articledetail.html', ctx)
    return render(request, 'core/articlecreate.html')




