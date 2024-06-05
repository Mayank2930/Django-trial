from django.urls import path
from .views import articleListView, articleView
# from .views import (
#     ArticleListView,
#     ArticleDetailView
# )

app_name = 'articles'

urlpatterns = [
    path('', articleListView, name='article_list'),
    path('<id>/', articleView, name='article')
]