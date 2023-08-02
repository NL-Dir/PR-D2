from django.urls import path
from .views import NewsList, PostDetail, SearchList, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

app_name = 'news'
urlpatterns = [
    path('', NewsList.as_view(), name='news'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('search', SearchList.as_view()),
    path('post/create/', PostCreateView.as_view(), name='post_create'),
    path('post/edit/<int:pk>', PostUpdateView.as_view(), name='post_update'),
    path('post/delete/<int:pk>', PostDeleteView.as_view(), name='post_delete'),
]