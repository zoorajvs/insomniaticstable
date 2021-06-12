from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import UserRegistartionForm, UserUpdateForm ,ProfileUpdateForm


def register(request):
    if request.method == 'POST':
        form = UserRegistartionForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'{username} your account has been created, You are now able to login !')
            return redirect('profile')

    else:
        form = UserRegistartionForm()
    context = {
        'title':'Registration',
        'form':form,
    }
    return render(request,'users/register.html',context)

@login_required
def Profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated !')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form':u_form,
        'p_form':p_form,
        'title': 'Profile'
    }
    return render(request,'users/profile.html',context)