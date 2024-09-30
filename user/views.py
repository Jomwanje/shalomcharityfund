from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SignupForm
# Create your views here.


def signup(request):
    if request.method == 'POST':
        new_form = SignupForm(request.POST)
        if new_form.is_valid():
            new_form.save()
            messages.success(request, f'Registration Completed')
            return redirect('https://jomwanjegachui.pythonanywhere.com//')
    else:
        new_form = SignupForm()

    return render(request, 'user/signup.html', {'new_form': new_form})
