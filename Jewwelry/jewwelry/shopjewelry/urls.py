# jewelry/urls.py

from django.urls import path
from . import views
from .views import *
from shopjewelry.views import pageuser
from shopjewelry.views import profile, pageuser, confirm
from django.contrib.auth.views import LogoutView
from django.conf.urls.static import static
from django.conf import settings 
from .views import track_package_view
from django.urls import path , include
from django.contrib import admin
urlpatterns = [
    path('', views.home, name='home'),  
    path('login/', views.login, name='login'), 
    path('register/', views.register, name='register'),
    path('pageuser/', pageuser, name='pageuser'),
    path('profile/', profile, name='profile'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('confirm/', confirm, name='confirm'),
    path('loginadmin/', views.login_view, name='loginadmin'),
    path('profileedit/', views.profileedit_view, name='profileedit'),         
    path('track-package/', track_package_view, name='track_package_view'),     
    path('contact/', views.contact_view, name='contact'),         
    path('logout/', views.logout_view, name='logout'),
    path('detail/<int:id>/', views.detail_view, name='detail'),
    path('ad/', views.ad_view, name='ad'),
     path('admin/', admin.site.urls),
    path('', include('user.urls')),
    path('', include('chat.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
