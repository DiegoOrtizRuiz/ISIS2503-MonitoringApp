from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import PasswordForm
from .logic.password_logic import get_passwords, create_password

def password_list(request):
    passwords = get_passwords()
    context = {
        'password_list': passwords
    }
    return render(request, 'Password/passwords.html', context)

def password_create(request):
    if request.method == 'POST':
        form = PasswordForm(request.POST)
        if form.is_valid():
            create_password(form)
            messages.add_message(request, messages.SUCCESS, 'Successfully created password')
            return HttpResponseRedirect(reverse('passwordCreate'))
        else:
            print(form.errors)
    else:
        form = PasswordForm()

    context = {
        'form': form,
    }
    return render(request, 'Password/passwordCreate.html', context)