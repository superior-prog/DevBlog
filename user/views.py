from django.shortcuts import render
from .decorators import *
from .forms import *
from django.contrib.auth import authenticate, login, logout


@unauthenticated_user
def login_page(request):
    if request.POST:
        form = LoginForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)

            if user and user.is_active:
                login(request, user)
                if request.GET.get('next'):
                    return redirect(request.GET.get('next'))
                return redirect('blog-home')
            else:
                return redirect('login')
        else:
            return render(request, 'user/login.html', {'form': form})
    form = LoginForm()
    context = {
        'form': form
    }
    return render(request, 'user/login.html', context)


def logout_user(request):
    logout(request)
    return redirect('login')


@unauthenticated_user
def user_register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=raw_password)
            login(request, user)
            return redirect('blog-home')
        else:
            return render(request, 'user/register.html', {"form": form})

    form = UserRegistrationForm()
    context = {
        "form": form
    }
    return render(request, 'user/register.html', context)
