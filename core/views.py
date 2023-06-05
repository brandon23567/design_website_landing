from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def index(request):
	return render(request, "core/index.html")

def not_ready(request):
	return render(request, "core/not_ready.html")

def signup(request):
	if request.method == "POST":
		username = request.POST["username"]
		email = request.POST["email"]
		password = request.POST["password"]
		confirm_password = request.POST["confirm_password"]

		new_user = User.objects.create_user(username=username, email=email, password=password)
		new_user.save()
		return redirect("not_ready")
	return render(request, "core/signup.html")