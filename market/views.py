from django.shortcuts import render
from django.shortcuts import (
    render,
    redirect,
)

from django.contrib.auth import (
    authenticate,
    login,
    logout,
)

from django.contrib import messages

from .forms import SignUpForm


# Create your views here.
def main(request):
    return render(request, 'market/main.html')

def signup(request):

    if request.user.is_authenticated:

        return redirect(
            "main"
        )


    if request.method == "POST":

        form = SignUpForm(
            request.POST
        )

        if form.is_valid():

            user = form.save()

            login(
                request,
                user
            )

            return redirect(
                "main"
            )

    else:

        form = SignUpForm()


    return render(
        request,
        "market/signup.html",
        {
            "form": form
        }
    )



def login_view(request):

    if request.user.is_authenticated:

        return redirect(
            "main"
        )


    if request.method == "POST":

        username = request.POST.get(
            "username"
        )

        password = request.POST.get(
            "password"
        )


        user = authenticate(
            request,
            username=username,
            password=password
        )


        if user is not None:

            login(
                request,
                user
            )

            return redirect(
                "main"
            )


        messages.error(
            request,
            "아이디 또는 비밀번호가 올바르지 않습니다."
        )


    return render(
        request,
        "market/login.html"
    )


def logout_view(request):

    if request.method == "POST":

        logout(request)

    return redirect(
        "main"
    )