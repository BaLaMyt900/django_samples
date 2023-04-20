
from django.contrib import admin
from django.urls import path, include
from samples.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('pages/', include('django.contrib.flatpages.urls')),
    path('about/', about_page),
    path('', index_page)
]
