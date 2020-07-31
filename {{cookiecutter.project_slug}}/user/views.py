from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.conf import settings
from django.contrib.auth.decorators import login_required

from .forms import UserSignUpForm, UserSignInForm, ProfileForm
from .models import User


def signup(request):
    if request.user.is_authenticated:
        return redirect(settings.LOGIN_REDIRECT_URL)
    if request.method == 'POST':
        form = UserSignUpForm(request.POST)
        if not form.is_valid():
            return render(request, 'user/signup.html', {'form': form})

        user = form.save()
        login(request, user)

        # email
        # current_site = get_current_site(request)
        #
        # mail_subject = 'Activate your blog account.'
        # message = render_to_string('emails/verification.html', {
        #     'user': user,
        #     'domain': current_site.domain,
        #     'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        #     'token': account_activation_token.make_token(user),
        # })
        # to_email = form.cleaned_data.get('email')
        # email = EmailMessage(
        #     mail_subject, message, to=[to_email]
        # )
        # email.send()

        return redirect(settings.LOGIN_REDIRECT_URL)
    else:
        form = UserSignUpForm()
        return render(request, 'user/signup.html', {'form': form})


def signin(request):
    if request.user.is_authenticated:
        return redirect(settings.LOGIN_REDIRECT_URL)

    if request.method == 'POST':
        form = UserSignInForm(request.POST)
        if not form.is_valid():
            return render(request, 'user/signin.html', {'form': form})

        user = form.login(request)

        login(request, user)
        return redirect(settings.LOGIN_REDIRECT_URL)
    else:
        form = UserSignInForm()
        return render(request, 'user/signin.html', {'form': form})


def signout(request):
    if not request.user.is_authenticated:
        return redirect('/')

    logout(request)
    return redirect('/')


@login_required()
def profile(request):
    user = request.user

    return render(request, 'user/profile.html', {
        'profile': user,
    })


@login_required()
def edit_profile(request):
    user = request.user

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=user)

        if form.is_valid():
            form.save()

            return redirect('profile', user.id, permanent=False)
    else:
        form = ProfileForm(instance=user)

    return render(request, 'user/edit_profile.html', {
        'form': form,
    })
