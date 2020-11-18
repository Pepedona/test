
from django.contrib import admin
from django.urls import path

from gordolab import views 
urlpatterns = [
    path('', views.index),
    path('admin/', admin.site.urls),
]
