"""alpha URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import signup, user_logout

urlpatterns = [
    #site admin
    path('admin/', admin.site.urls),
    path('signup/', signup, name='signup'),
    path('logout/', user_logout, name='logout'),

    #backend 3pty apps
    path('summernote/', include('django_summernote.urls')),

    #site apps
    path('', include('pages.urls',namespace='pages')),
    path('blog/', include('articles.urls',namespace='articles')),
    path('contact/', include('contact.urls',namespace='contact')),
    path('calendar/', include('events.urls',namespace='events')),
    path('gallery/', include('gallery.urls',namespace='gallery')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)