from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import CustomUser

def register(request):
    if request.method == 'POST':
        username  = request.POST.get('username')
        email     = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            messages.error(request, 'Les mots de passe ne correspondent pas.')
            return redirect('register')

        if CustomUser.objects.filter(username=username).exists():
            messages.error(request, 'Ce nom d\'utilisateur est déjà pris.')
            return redirect('register')

        user = CustomUser.objects.create_user(username=username, email=email, password=password1)
        login(request, user)
        messages.success(request, f'Bienvenue {username} !')
        return redirect('dashboard')

    return render(request, 'accounts/register.html')

@login_required
def dashboard(request):
    applications = request.user.applications.select_related('offer').order_by('-applied_at')
    return render(request, 'accounts/dashboard.html', {'applications': applications})