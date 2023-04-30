from django.shortcuts import render, get_object_or_404
from django.contrib.auth import login
from django.http import HttpResponse
from demo_portfolio.models import User
import requests

def userIndex(request):
	return HttpResponse("Hello World this is the users´s index")

def userShow(request, intra_username):
	user = get_object_or_404(User, intra_username=intra_username)
	return render(request, "users/show.html", {"user": user, "user_serialized": user.serialize()})

def intraCallback(request):
	get_token_path = "https://api.intra.42.fr/oauth/token"
	data = {
		'grant_type': 'authorization_code',
		'client_id': 'u-s4t2ud-c85140fe4385257415ed1433c2cf14e27ccaf945213c460e784751a9e830a397',
		'client_secret': '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',
		'code': request.GET["code"],
		'redirect_uri': 'http://localhost:8000/auth/intra_callback',
	}
	r = requests.post(get_token_path, data=data)
	token = r.json()['access_token']
	headers = {"Authorization": "Bearer %s" % token}
	user_response = requests.get("https://api.intra.42.fr/v2/me", headers=headers)
	user_response_json = user_response.json()
	
	user, created = User.objects.get_or_create(
    	intra_id=user_response_json['id'],
    	intra_username=user_response_json['login'],
    	first_name=user_response_json['first_name'],
    	last_name=user_response_json['last_name'],
    	email=user_response_json['email'],
	)
	login(request, user)
	return HttpResponse("User %s %s" % (user, "created now" if created else "found"))
