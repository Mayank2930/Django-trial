from django.shortcuts import render

from . models import Article

from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
)

# class ArticleListView(ListView):
#     template_name = 'articles/article_list.html'
#     queryset = article.objects.all()


def articleListView(request):
    list_of_article = Article.objects.all()

    context = {
        'list_of_article': list_of_article
    }

    return render(request, 'article_list.html', context)


def articleView(request, id):
    
    article = Article.objects.get(id=id)

    context = {
        'article': article
    }

    return render(request, 'article_detail.html', context)

# class ArticleDetailView(DetailView):
#     template_name = 'articles/article_detail.html'
#     queryset = article.objects.all()




