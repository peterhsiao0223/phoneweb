from django.shortcuts import render,redirect
import datetime
from user_log.models import User_Log_Info
# Create your views here.

def customer_form_info_post(request):
	user_name = 'peter'
	type_log = 'note'
	date_text = datetime.datetime.today()
	log_text = request.POST['log_text']
	costomer_sn = request.POST['costomer_sn']
	print('log_text=',log_text)
	User_Log_Info.objects.create(costomer_sn = costomer_sn , type_log = type_log , sign_user = user_name , log_text = log_text ,created_at = date_text)
	response = redirect('/customer_form_info/'+ costomer_sn)
	return response	