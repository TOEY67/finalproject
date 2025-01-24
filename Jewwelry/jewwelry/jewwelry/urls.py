"""
URL configuration for jewwelry project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
# jewelry/urls.py หรือ myproject/urls.py (ขึ้นอยู่กับว่าไฟล์นี้อยู่ที่ไหน)

from django.contrib import admin
from django.urls import include, path
from shopjewelry import views
from shopjewelry.views import pageuser
from shopjewelry.views import profile, pageuser, confirm
from django.contrib.auth.views import LogoutView



urlpatterns = [
    path('admin/', admin.site.urls),           # URL สำหรับหน้า Admin
    path('', include('shopjewelry.urls')), # รวม URLs ของแอป shopjewelry  
] 