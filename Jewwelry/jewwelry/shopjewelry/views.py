# jewelry/views.py

from django.shortcuts import render,redirect
from django.contrib.auth import login
from .forms import registerForm
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from django.db import IntegrityError
from django.db import models
from django.contrib.auth.models import User
from .models import CustomUser
def home(request):
    return render(request, 'home.html')  # หน้าหลัก

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # หา User โดยใช้อีเมล
        try:
            user = CustomUser.objects.get(email=email)
            username = user.username  # ดึง username เพื่อใช้ authenticate
        except CustomUser.DoesNotExist:
            error_message = "ไม่พบบัญชีที่มีอีเมลนี้"
            return render(request, 'login.html', {'error_message': error_message})

        # ตรวจสอบข้อมูลล็อกอิน
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('pageuser')  # ไปยังหน้า pageuser หลังล็อกอินสำเร็จ
        else:
            error_message = "อีเมลหรือรหัสผ่านไม่ถูกต้อง"
            return render(request, 'login.html', {'error_message': error_message})

    return render(request, 'login.html')

User = get_user_model()

def register(request):
    if request.method == 'POST':  # ตรวจว่ามีการส่งข้อมูลจากฟอร์ม
        # รับค่าจากฟอร์ม
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        birthday = request.POST.get('birthday')  # วันเกิด

        # ตรวจสอบว่ารหัสผ่านตรงกันหรือไม่
        if password != confirm_password:
            error_message = "รหัสผ่านไม่ตรงกัน"
            return render(request, 'register.html', {'error_message': error_message})

        # พยายามสร้างผู้ใช้ใหม่ในระบบ
        try:
            user = User.objects.create_user(
                username=email,  # ใช้ email เป็น username
                email=email,
                password=password,
                name=name,
                phone=phone,
                address=address,
                birthday=birthday
            )
            return redirect('login')  # ถ้าสมัครเสร็จ ไปหน้า Login

        # ถ้ามีข้อมูลซ้ำ เช่น email ซ้ำ จะแสดงข้อผิดพลาด
        except IntegrityError:
            error_message = "อีเมลนี้ถูกใช้ไปแล้ว กรุณาลองใหม่"
            return render(request, 'register.html', {'error_message': error_message})

    # ถ้าเป็น GET request ให้แสดงหน้า register.html
    return render(request, 'register.html')

 
def profile(request):
    return render(request, 'profile.html') 

def pageuser(request):
    return render(request, 'pageuser.html')  

def confirm(request):
    return render(request, 'confirm.html')

def login_view(request):
    return render(request, 'admin.html')

from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    # เชื่อมโยงผู้ใช้กับโมเดล User (User เป็นโมเดลที่ Django ใช้จัดการผู้ใช้งาน)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    # ฟิลด์สำหรับเก็บภาพโปรไฟล์
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    
    # คำอธิบายหรือข้อมูลเพิ่มเติมเกี่ยวกับโปรไฟล์ (ไม่บังคับ)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.user.username} Profileedit'
    def profileedit_view(request):
        user_profile = profile.objects.get(user=request.user)
        form = Profile(instance=user_profile)
        return render(request, 'profileedit.html', {'form': form})
    
    # View สำหรับข้อมูลส่วนตัว
def profileedit_view(request):
    return render(request, 'profileedit.html')

# View สำหรับติดตามงาน
from django.shortcuts import render
import requests
import json
from django.http import JsonResponse
def track_package_view(request):
    if request.method == "POST":
        # Get the barcode input from the form
        barcode = request.POST.get("barcode")
        
        # Make sure the barcode is not empty
        if barcode:
            url = "https://trackapi.thailandpost.co.th/post/api/v1/track"
            
            payload = json.dumps({
                "status": "all",
                "language": "TH",
                "barcode": [barcode]  # Use the barcode entered by the user
            })
            
            headers = {
                'Authorization': 'Token eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpc3MiOiJzZWN1cmUtYXBpIiwiYXVkIjoic2VjdXJlLWFwcCIsInN1YiI6IkF1dGhvcml6YXRpb24iLCJleHAiOjE3MzkwMzk5NjMsInJvbCI6WyJST0xFX1VTRVIiXSwiZCpzaWciOnsicCI6InpXNzB4IiwicyI6bnVsbCwidSI6ImYyNWIzYmRjODFjNjE0ZTUzMTkyNmQxNTk5YzUwNzQzIiwiZiI6InhzeiM5In19.bJr3iRUhet092uBS19KhFTBHlpZH1fDbchXnPWvpljdjGVOKoJujf6qnjTY1e9B1eg0NfvmphrtIp723R5kvIw',
                'Content-Type': 'application/json'
            }
            
            # Make the API request to track the package
            response = requests.post(url, headers=headers, data=payload)
            
            # Check if the response was successful
            if response.status_code == 200:
                response_data = response.json()
                return JsonResponse(response_data)
            else:
                return JsonResponse({'error': 'ไม่พบข้อมูลพัสดุ'}, status=400)
        else:
            return JsonResponse({'error': 'กรุณากรอกหมายเลขพัสดุ'}, status=400)
    
    return render(request, 'track-package.html')

# View สำหรับติดต่อสอบถาม
def contact_view(request):
    return render(request, 'contact.html')

# View สำหรับออกจากระบบ
def logout_view(request):
    # ใช้ logout() เพื่อล็อกเอาต์ผู้ใช้
    from django.contrib.auth import logout
    logout(request)
    return redirect('home')  # ส่งผู้ใช้กลับไปยังหน้าแรก

def detail_view(request, id):
    # ตัวอย่างข้อมูล (สามารถดึงจากฐานข้อมูลได้จริง ๆ)
    product = {
        'id': id,
        'name': 'แหวนเงินแท้ 925',
        'price': 1500,
        'description': 'แหวนเงินแท้ดีไซน์สวยงาม เหมาะกับทุกโอกาส',
    }
    return render(request, 'detail.html', {'product': product})

def ad_view(request):
    return render(request, 'ad.html')
