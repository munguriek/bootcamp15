from django.urls import path 

from . import views

from django import admin
from django.urls import path, include


app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name='all_posts'),
    path('<int:id>/', views.post_detail, name='post_detail'),
]

app_name = 'hello_world'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', include('hello_world.urls'))
]