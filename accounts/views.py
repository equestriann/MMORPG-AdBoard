from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate

from .forms import AccountCreationForm


def user_login(request):
    pass
    # username = request.POST("username")
    # password = request.POST('password')
    # user = authenticate(
    #     request,
    #     username=username,
    #     password=password
    # )
    #
    # if user is not None:
    #     login(request, user)
    #     return redirect('login_success')
    # else:
    #     messages.info(request, 'Ошибка при попытке входа')
    #
    # context = {}
    #
    # return render(
    #     request,
    #     'login.html',
    #     context
    # )


def user_register(request):
    # if request.user.is_authenticated:
    #     return redirect('ads_list')

    if request.method == 'POST':
        form = AccountCreationForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Аккаунт зарегистрирован')

            return redirect('ads_list')

        else:
            messages.error(request, message=form.errors)
            print(form.errors)

    else:
        form = AccountCreationForm()

    context = {
        'reg_form': form,
    }
    return render(
        request,
        'register.html',
        context=context
    )


def user_logout(request):
    pass
