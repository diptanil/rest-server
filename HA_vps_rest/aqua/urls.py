from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
path('', views.getData),
# path('connect/', views.checkConnection),
# path('post/', views.postData),
]