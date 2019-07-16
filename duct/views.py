import logging
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.db.utils import IntegrityError
from duct.forms import SignUpForm


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            logging.debug("singup message test")
            try:
                form.save()
            except IntegrityError as e:
                logging.debug("singup message test {}".format(e.message))

            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})
