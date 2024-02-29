from django.shortcuts import render, redirect

from .forms import AccountCreationForm


def user_login(request):
    pass


def user_register(request):
    if request.user.is_authenticated:
        return redirect('ads_list')

    if request.method == 'POST':
        form = AccountCreationForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            username = user.name
            user_email = user.email

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
