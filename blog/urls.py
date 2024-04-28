from django.urls import path
from . import views

app_name = 'blog' # se crea para diferenciar la llamada de las url por el template ejemplo({% url 'blog:post_detail' id=post.id %})

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>', views.post_detail, name='post_detail'),
]