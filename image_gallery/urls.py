"""image_gallery URL Configuration

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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from pages.views import(
    home_page_view,
    upload_picture_view,
    must_authenticate_view,
    gallery_view,
)

from account.views import(
    registration_view,
    logout_view,
    login_view,
    )

urlpatterns = [
    path('', home_page_view, name='home'),
    path('admin/', admin.site.urls),
    path('gallery/', gallery_view, name='gallery'),
    path('must_authenticate/', must_authenticate_view, name='must_auth'),
    path('logout/', logout_view, name='logout'),
    path('login/', login_view, name='login'),
    path('upload/', upload_picture_view, name='upload_picture'),
    path('register/', registration_view, name='register'),
]


if settings.DEBUG:
    urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

