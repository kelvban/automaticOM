# -*-coding:utf-8 -*-
from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse,HttpResponse
from models import *
import json

def user_info(request):
	ip_addr=request.META['REMOTE_ADDR']
	user_ua=request.META['HTTP_USER_AGENT']
	
	user_obj=UserIPInfo.objects.filter(ip=ip_addr)
	if not user_obj:
		res=UserIPInfo.objects.create(ip=ip_addr)
		ip_add_id=res.id
	else:
		ip_add_id=user_obj[0].id
	BrowseInfo.objects.create(user_agent=user_ua,user_ip_id=ip_add_id)

	result={"status":"success",
			"info":"User Info",
			"ip":ip_addr,
			"ua":user_ua}
	return HttpResponse(json.dumps(result),content_type="application/json")
