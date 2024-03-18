from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate

from .forms import AccountCreationForm
from .tasks import send_activation_code
from .models import User, Code

import pprint


def user_login(request):
    if request.user.is_authenticated:
        return redirect('user_profile')

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('user_profile')
        else:
            messages.info(request, 'Login error')

    context = {}

    return render(
        request,
        "login.html",
        context
    )


def user_register(request):
    if request.user.is_authenticated:
        return redirect('user_profile')

    if request.method == 'POST':
        form = AccountCreationForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            username = user.username
            user_email = user.email

            if not User.objects.filter(email=user_email).exists():
                user.is_active = False
                user.save()
                send_activation_code.delay(user.id)
                messages.info(request, message='Код подтверждения отправлен на Вашу почту')

                return redirect(to='account_activation')

            else:
                existing_user = User.objects.get(email=user_email)

                if existing_user.username != username and existing_user.is_active:
                    messages.info(request, message='Аккаунт с данной элетронной почтой уже существует!')
                    context = {'reg_form': form}
                    return render(request, 'register.html', context)

        else:
            messages.error(request, message=form.errors)
            print(form.errors)

    else:
        form = AccountCreationForm()

    context = {'reg_form': form}
    return render(
        request,
        'register.html',
        context=context
    )


def activate_account(request):
    if request.method == "POST":
        cur_code = request.POST.get('code')

        if Code.objects.filter(code=cur_code):
            user = Code.objects.get(code=cur_code).user
            user.is_active = True
            user.save()
            Code.objects.get(code=cur_code).delete()
            return redirect('login')
        else:
            messages.info(request, 'Некорректный код')

    return render(
        request,
        'account_activation.html'
    )


def user_logout(request):
    logout(request)
    return redirect('ads_list')
