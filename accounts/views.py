from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages

def signup(request):
    """회원가입"""
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        email = request.POST.get('email')
        
        # 유효성 검사
        if not username or not password1:
            messages.error(request, '사용자명과 비밀번호를 입력해주세요.')
            return render(request, 'accounts/signup.html')
        
        if password1 != password2:
            messages.error(request, '비밀번호가 일치하지 않습니다.')
            return render(request, 'accounts/signup.html')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, '이미 존재하는 사용자명입니다.')
            return render(request, 'accounts/signup.html')
        
        # 사용자 생성
        user = User.objects.create_user(
            username=username,
            password=password1,
            email=email
        )
        login(request, user)
        messages.success(request, '회원가입이 완료되었습니다.')
        return redirect('home')
    
    return render(request, 'accounts/signup.html')

def user_login(request):
    """로그인"""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, f'{username}님, 환영합니다!')
            next_url = request.GET.get('next', 'home')
            return redirect(next_url)
        else:
            messages.error(request, '사용자명 또는 비밀번호가 올바르지 않습니다.')
    
    return render(request, 'accounts/login.html')

@login_required
def user_logout(request):
    """로그아웃"""
    logout(request)
    messages.success(request, '로그아웃되었습니다.')
    return redirect('home')

@login_required
def profile(request):
    """프로필 보기"""
    return render(request, 'accounts/profile.html')

@login_required
def profile_update(request):
    """프로필 수정"""
    if request.method == 'POST':
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        user = request.user
        
        # 이메일 수정
        if email:
            user.email = email
        
        # 비밀번호 수정
        if password1:
            if password1 == password2:
                user.set_password(password1)
                messages.success(request, '비밀번호가 변경되었습니다. 다시 로그인해주세요.')
                user.save()
                logout(request)
                return redirect('accounts:login')
            else:
                messages.error(request, '비밀번호가 일치하지 않습니다.')
                return render(request, 'accounts/profile_update.html')
        
        user.save()
        messages.success(request, '프로필이 수정되었습니다.')
        return redirect('accounts:profile')
    
    return render(request, 'accounts/profile_update.html')

