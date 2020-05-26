from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from .forms import access


@login_required
def sign_out(request):
    # signs the user out

    if request.user.is_authenticated:
        auth.logout(request)
        messages.success(request, "Logout successful!")
        return redirect(reverse('home'))

    else :
        return redirect(reverse('home'))


def sign_in(request):
    # returns homepage

        if request.user.is_authenticated:
            return redirect(reverse('home'))

        if request.method == "POST":
            sign_in_form = access(request.POST)
            if sign_in_form.is_valid():
                user = auth.authenticate(
                    username=request.POST['username'],
                    password=request.POST['password'])
                if user:
                    auth.login(user=user, request=request)
                    messages.success(request, "Login successful!")
                    return redirect(reverse('home'))
                else:
                    sign_in_form.add_error(
                        None, "Your username or password is incorrect!")
        else:
            sign_in_form = access()
    
        return render(request, "../templates/sign_in.html", {"sign_in_form": sign_in_form})
