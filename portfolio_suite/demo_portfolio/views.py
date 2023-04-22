from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from demo_portfolio.models import User

def userIndex(request):
	return HttpResponse("Hello World this is the users´s index")

def userShow(request, intra_username):
	user = get_object_or_404(User, intra_username=intra_username)
	return render(request, "users/show.html", {"user": user, "user_serialized": user.serialize()})
