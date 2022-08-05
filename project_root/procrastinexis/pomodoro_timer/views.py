# Django Libraries
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# Other Third Party Libraries

# Own Libraries

# Default Route
def index(request):
    return render(request, "pomodoro_timer/index.html")


# Log in
def login_view(request):
    # POST Request
    if request.method == "POST":

        # Try to log user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if Login was successful
        if user is not None:
            # Log User in
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "pomodoro_timer/login.html", {
                "error_message": "Invalid Username and/or Password. Please try again."
            })

    # Visitor trying to Log in [GET Request]
    else:
        return render(request, "pomodoro_timer/login.html")

# Log out
def logout_view(request):
    # Use Logout Function
    logout(request)
    return HttpResponseRedirect(reverse("index"))

# Register for Account
def register(request):
    # POST Request. Visitor creating an account
    if request.method == "POST":
        pass

    # GET Request
    else:
        pass