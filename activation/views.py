from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, reverse, get_object_or_404
from django.utils import timezone
from activation.models import Activation
from activation.helpers.utils import regenerate_activation
from users.forms import SetPassword
from django.contrib.auth import authenticate, login
from django.conf import settings

app_name = 'activation'


def activate(request, token):
    activation = get_object_or_404(Activation, token=token)

    if activation.user.is_active:
        raise Http404

    if activation.expires_at < timezone.now():
        if request.GET.get('resend'):
            regenerate_activation(activation)
            return HttpResponseRedirect(reverse('users:login'))

        return render(request, 'activation/activate.html', {
            'token': activation.token
        })

    if request.method == 'POST':
        form = SetPassword(activation.user, request.POST)
        if form.is_valid():
            user_with_password = form.save(commit=False)
            user_with_password.is_active = True
            user_with_password.save()

            activation.activated_at = timezone.now()
            activation.save()

            email = user_with_password.email
            password = form.cleaned_data['password']

            authenticated_user = authenticate(request, username=email, password=password)
            print('settings.DJANGO_AUTH_BACKEND', settings.DJANGO_AUTH_BACKEND)
            login(request, authenticated_user, backend=settings.DJANGO_AUTH_BACKEND, )

            return HttpResponseRedirect(reverse('users:login'))

    else:
        form = SetPassword(activation.user)

    return render(request, 'activation/set_password.html', {
        'form': form,
        'token': token
    })
