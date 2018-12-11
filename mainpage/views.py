from django.shortcuts import render,redirect
from django.contrib.auth.models import User,Group
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth import login


import datetime
from datetime import timedelta
import random
from mainpage.models import Phone_Brand,Phone_name,Accessories_Name,Fix_Part_Manage,Phone_Color,Stock_Phone_Amount_Manage,Costomer_Manage
from stock.models import Stock_Phone_Manage
from engineer_manage.models import Costomer_Fix_Managment,Engineer_List_Managment
from user_log.models import User_Log_Info

from django.utils import timezone
import requests
# Create your views here.

@login_required
def get_index(request):
	response = render(request,'mainpage/index.html',locals())
	return response



def customer_form(request):
	phone_brand_name_lists = []
	phone_brand_num_lists = []
	phone_color_lists = Phone_Color.objects.filter(alive=True)
	phone_brand_lists = Phone_Brand.objects.filter(alive=True)
	phones_fix = Fix_Part_Manage.objects.filter(alive=True)
	accessories_names = Accessories_Name.objects.filter(alive=True)
	date_now = datetime.datetime.today().strftime("%Y/%m/%d %H:%M:%S")
	user_sn = datetime.datetime.today().strftime("%Y%m%d%S") + str(random.randint(100,999))
	try:
		phone_brand_choice = request.POST['phone_brand_choice']
		if phone_brand_choice == 'none':
			response = redirect('/customer_form/')
		else:
			phone_brand_name = Phone_Brand.objects.filter(phone_brand_num=phone_brand_choice,alive=True)[0].phone_brand_name
			phone_brand_name_alls = Phone_name.objects.filter(phone_brand_name=phone_brand_name,alive=True)
			for phone_brand_name_all in phone_brand_name_alls:
				if phone_brand_name_all.phone_name in phone_brand_name_lists:
					pass
				else:
					phone_brand_name_lists.append(phone_brand_name_all.phone_name)
					phone_brand_num_lists.append(phone_brand_name_all.phone_name_num)
			phone_name_lists = zip(phone_brand_name_lists,phone_brand_num_lists)
	except:
		pass
	response = render(request,'mainpage/customer_form.html',locals())
	return response

def customer_form_edit(request,costomer_sn):
	phone_brand_name_lists = []
	phone_brand_num_lists = []
	customer_lists = Costomer_Manage.objects.get(costomer_sn=costomer_sn,alive=True)
	phone_name_num_text = Phone_name.objects.get(phone_name=customer_lists.phone_name_num).phone_name_num
	phone_brand_num_text = phone_name_num_text[:4]
	print('phone_name_num=',phone_name_num_text,'phone_brand_num=',phone_brand_num_text)
	phone_color_lists = Phone_Color.objects.filter(alive=True)
	# phone_name_lists = Phone_name.objects.filter(phone_name_num__startswith=phone_brand_num_text,alive=True)
	phones_fix = Fix_Part_Manage.objects.filter(alive=True)
	accessories_names = Accessories_Name.objects.filter(alive=True)
	plus_buy_lists = customer_lists.plus_buy.replace('[','').replace(']','').replace("'","").split(',')
	plus_buy_price_lists = customer_lists.plus_buy_price.replace('[','').replace(']','').replace("'","").split(',')
	# phone_brand_name = Phone_Brand.objects.get(phone_brand_num=phone_brand_choice,alive=True).phone_brand_name
	phone_brand_name = Phone_Brand.objects.get(phone_brand_num=phone_brand_num_text,alive=True).phone_brand_name
	phone_brand_name_alls = Phone_name.objects.filter(phone_brand_name=phone_brand_name,alive=True)
	for phone_brand_name_all in phone_brand_name_alls:
		phone_brand_name_lists.append(phone_brand_name_all.phone_name)
		phone_brand_num_lists.append(phone_brand_name_all.phone_name_num)
	phone_name_lists = zip(phone_brand_name_lists,phone_brand_num_lists)
	plus_buy_zip = zip(plus_buy_lists,plus_buy_price_lists)
	response = render(request,'mainpage/customer_form_edit.html',locals())
	return response	

def customer_form_info(request,costomer_sn):
	phone_brand_name_lists = []
	phone_brand_num_lists = []
	plus_buy_price_total = 0
	customer_lists = Costomer_Manage.objects.get(costomer_sn=costomer_sn,alive=True)
	if customer_lists.finish_status == True:
		engineer_lists = Costomer_Fix_Managment.objects.get(costomer_sn=costomer_sn,alive=True)
		engineer_fix_part_name = engineer_lists.stock_part_name.split(',')[:-1]
		engineer_fix_part_num = engineer_lists.stock_part_num.split(',')[:-1]
		if engineer_lists.engineer_2 :
			engineer_name_2 = Engineer_List_Managment.objects.get(engineer_num=engineer_lists.engineer_2).engineer_name
	else:
		engineer_fix_part_name = []
		engineer_fix_part_num = []
	if customer_lists.engineer:
		engineer_name = Engineer_List_Managment.objects.get(engineer_num=customer_lists.engineer).engineer_name
	stock_part_zip = zip(engineer_fix_part_name,engineer_fix_part_num)
	phone_name_num_text = Phone_name.objects.get(phone_name=customer_lists.phone_name_num).phone_name_num
	phone_brand_num_text = phone_name_num_text[:4]
	print('phone_name_num=',phone_name_num_text,'phone_brand_num=',phone_brand_num_text)
	phone_color_lists = Phone_Color.objects.filter(alive=True)
	# phone_name_lists = Phone_name.objects.filter(phone_name_num__startswith=phone_brand_num_text,alive=True)
	phones_fix = Fix_Part_Manage.objects.filter(alive=True)
	accessories_names = Accessories_Name.objects.filter(alive=True)
	plus_buy_lists = customer_lists.plus_buy.replace('[','').replace(']','').replace("'","").split(',')
	plus_buy_price_lists = customer_lists.plus_buy_price.replace('[','').replace(']','').replace("'","").split(',')
	# phone_brand_name = Phone_Brand.objects.get(phone_brand_num=phone_brand_choice,alive=True).phone_brand_name
	phone_brand_name = Phone_Brand.objects.get(phone_brand_num=phone_brand_num_text,alive=True).phone_brand_name
	phone_brand_name_alls = Phone_name.objects.filter(phone_brand_name=phone_brand_name,alive=True)
	for phone_brand_name_all in phone_brand_name_alls:
		phone_brand_name_lists.append(phone_brand_name_all.phone_name)
		phone_brand_num_lists.append(phone_brand_name_all.phone_name_num)
	phone_name_lists = zip(phone_brand_name_lists,phone_brand_num_lists)
	plus_buy_zip = zip(plus_buy_lists,plus_buy_price_lists)
	try:
		plus_buy_status = True
		for i in range(len(plus_buy_price_lists)):
			plus_buy_price_total = plus_buy_price_total + int(plus_buy_price_lists[i])
	except:
		plus_buy_status = False
	user_log_losts = User_Log_Info.objects.filter(costomer_sn=costomer_sn).order_by('-created_at')
	if customer_lists.customer_receive == True :

		step_5 = 'done'
		step_1 = 'done'
		step_2 = 'done'
		step_3 = 'done'
		step_4 = 'done'
		step_5_text = customer_lists.receive_at
		step_4_text = User_Log_Info.objects.get(costomer_sn=costomer_sn,type_log = 'system' , log_text = '已通知取件').created_at
		step_3_text = customer_lists.update_at
		step_2_text = Costomer_Fix_Managment.objects.get(costomer_sn = customer_lists.costomer_sn).created_at
	else:
		if customer_lists.field_1 != '' :
			step_5 = 'disabled'
			step_4 = 'done'
			step_3 = 'done'
			step_2 = 'done'
			step_1 = 'done'
			step_4_text = User_Log_Info.objects.get(costomer_sn=costomer_sn,type_log = 'system' , log_text = '已通知取件').created_at
			step_3_text = customer_lists.update_at
			step_2_text = Costomer_Fix_Managment.objects.get(costomer_sn = customer_lists.costomer_sn).created_at
		else:
			if customer_lists.finish_status == True :
				step_5 = 'disabled'
				step_4 = 'disabled'
				step_3 = 'done'
				step_2 = 'done'
				step_1 = 'done'
				step_3_text = customer_lists.update_at
				step_2_text = Costomer_Fix_Managment.objects.get(costomer_sn = customer_lists.costomer_sn).created_at
			else:
				if customer_lists.engineer != '' :
					step_5 = 'disabled'
					step_4 = 'disabled'
					step_3 = 'disabled'
					step_2 = 'done'
					step_1 = 'done'
					step_2_text = Costomer_Fix_Managment.objects.get(costomer_sn = customer_lists.costomer_sn).created_at
				else:
					step_5 = 'disabled'
					step_4 = 'disabled'
					step_3 = 'disabled'
					step_2 = 'disabled'
					step_1 = 'done'

	step_1_text = customer_lists.created_at
	response = render(request,'mainpage/customer_form_info.html',locals())
	return response	

def customer_form_notice(request):
	costomer_sn = request.POST['costomer_sn']
	user_text = request.user.username
	date_text =  datetime.datetime.today()
	customer_lists = Costomer_Manage.objects.filter(costomer_sn=costomer_sn,alive=True,finish_status=True).update(field_1=user_text)
	User_Log_Info.objects.create(costomer_sn=costomer_sn,type_log = 'system',sign_user = user_text , log_text = '已通知取件',created_at = date_text)
	response = redirect('/customer_form_info/'+costomer_sn)
	return response

def customer_form_recive(request):
	costomer_sn = request.POST['costomer_sn']
	action = request.POST['action']
	user_text = request.user.username
	date_text =  datetime.datetime.today()
	if action == 'notice':
		Costomer_Manage.objects.filter(costomer_sn=costomer_sn,alive=True,finish_status=True).update(field_1=user_text)
		User_Log_Info.objects.create(costomer_sn=costomer_sn,type_log = 'system',sign_user = user_text , log_text = '已通知取件',created_at = date_text)
	elif action == 'recive':
		Costomer_Manage.objects.filter(costomer_sn=costomer_sn,alive=True,finish_status=True).update(customer_receive=True, receive_at = date_text)
		User_Log_Info.objects.create(costomer_sn=costomer_sn,type_log = 'system',sign_user = user_text , log_text = '客戶已取件',created_at = date_text)
		Costomer_Fix_Managment.objects.filter(costomer_sn = costomer_sn,alive = True).update(customer_receive=True)
	response = redirect('/customer_form_info/'+costomer_sn)
	return response

def customer_create_post(request):
	phone_brand_num = request.POST['phone_brand']
	phone_name_num = request.POST['phone_name']
	customer_name = request.POST['customer_name']
	customer_phone_num = request.POST['customer_phone_num']
	gender_text = request.POST['gender']
	phone_color = request.POST.getlist('phone_color')
	fix_parts = request.POST.getlist('fix_part')
	total_price = request.POST['total_price']
	deposit = request.POST['deposit']
	plus_buys = request.POST.getlist('plus_buy')
	plus_buy_price = request.POST.getlist('plus_buy_price')
	costomer_sn = request.POST['user_sn']
	data_type = request.POST['data_type']
	phone_pw = request.POST['phone_pw']
	phone_sn = request.POST['phone_sn']
	phone_comment = request.POST['phone_comment']

	fix_part_manage = Fix_Part_Manage.objects.filter(alive=True)
	phone_color_manage = Phone_Color.objects.filter(alive=True)
	phone_brand_manage = Phone_Brand.objects.filter(alive=True)
	phone_name_manage = Phone_name.objects.filter(alive=True)
	plus_buy_manage = Accessories_Name.objects.filter(alive=True)

	if gender_text == 'male':
		gender = True
	elif gender_text == 'female':
		gender = False
	sells = request.user.username
	story = '測試店家1'
	fix_part_text = []
	plus_buy_text = []

	for fix_part in fix_parts:
		fix_part_text.append(fix_part_manage.get(fix_part_num=fix_part).fix_part_name)

	for plus_buy in plus_buys:
		plus_buy_text.append(plus_buy_manage.get(accessories_num=plus_buy).accessories_name)

	phone_brand_text = phone_brand_manage.get(phone_brand_num=phone_brand_num).phone_brand_name
	phone_name_text = phone_name_manage.get(phone_name_num=phone_name_num).phone_name
	phone_color_text = phone_color[1]

	if data_type == 'create':
		Costomer_Manage.objects.create(costomer_sn=costomer_sn,customer_name=customer_name,customer_phone_num=customer_phone_num,phone_brand_num=phone_brand_text,phone_name_num=phone_name_text,gender=gender,phone_color=phone_color_text,fix_part=fix_part_text,total_price=total_price,deposit=deposit,plus_buy=plus_buy_text,plus_buy_price=plus_buy_price,sells=sells,story=story,phone_pw = phone_pw ,fix_part_sn_num = phone_sn,bg_note = phone_comment)
	elif data_type == 'edit':
		Costomer_Manage.objects.filter(costomer_sn=costomer_sn).update(customer_name=customer_name,customer_phone_num=customer_phone_num,phone_brand_num=phone_brand_text,phone_name_num=phone_name_text,gender=gender,phone_color=phone_color_text,fix_part=fix_part_text,total_price=total_price,deposit=deposit,plus_buy=plus_buy_text,plus_buy_price=plus_buy_price)
	# print(phone_brand,phone_name,customer_name,customer_phone_num,gender,phone_color,fix_part,total_price,deposit,plus_buy,plus_buy_price,costomer_sn)
	response = redirect('/')
	return response

def customer_review(request):
	plus_buy_price_lists = []
	fix_part_text_lists = []
	fix_part_num_lists = []
	plus_buy_text_lists = []
	plus_buy_num_lists = []
	accessories_price = 0
	phone_name = request.POST['phone_name']
	customer_name = request.POST['customer_name']
	customer_phone_num = request.POST['customer_phone_num']
	gender = request.POST['gender']
	phone_color = request.POST['phone_color']
	fix_parts = request.POST.getlist('fix_part')
	phone_pw = request.POST['phone_pw']
	phone_sn = request.POST['phone_sn']
	total_price = request.POST['total_price']
	deposit = request.POST['deposit']
	phone_comment = request.POST['phone_comment']
	data_type = request.POST['data_type']

	try:
		plus_buys = request.POST.getlist('plus_buy')
		plus_buy_prices = request.POST.getlist('plus_buy_price')
		for plus_buy in plus_buys:
			accessories_name = Accessories_Name.objects.get(accessories_num=plus_buy,alive=True)
			plus_buy_text_lists.append(accessories_name.accessories_name)
			plus_buy_num_lists.append(accessories_name.accessories_num)
		for plus_buy_price in plus_buy_prices:
			if plus_buy_price == '0':
				pass
			else:
				plus_buy_price_lists.append(plus_buy_price)
			accessories_price = accessories_price + int(plus_buy_price)

		accessories_name_lists = zip(plus_buy_text_lists,plus_buy_price_lists,plus_buy_num_lists)
		# print(plus_buy_text_lists,plus_buy_price_lists,plus_buy_num_lists,accessories_price)
	except:
		pass
	user_sn = request.POST['user_sn']
	phone_brand = request.POST['phone_brand']
	if phone_color == 'else':
		phone_color_name = request.POST['color_else']
	else:	
		phone_color_name = Phone_Color.objects.get(phone_color_num=phone_color).phone_color_name
	phone_name_text = Phone_name.objects.get(phone_name_num=phone_name,alive=True)
	for fix_part in fix_parts:
		fix_part_text_lists.append(Fix_Part_Manage.objects.get(fix_part_num=fix_part,alive=True).fix_part_name)
		fix_part_num_lists.append(Fix_Part_Manage.objects.get(fix_part_num=fix_part,alive=True).fix_part_num)
	fix_part_lists = zip(fix_part_num_lists,fix_part_text_lists)

	total_price_plus_buy = int(total_price) + accessories_price
	response = render(request,'mainpage/customer_form_review.html',locals())
	return response


def customer_table(request):
	try:
		phone_brand_choice = request.POST['phone_brand_choice']
		status = request.POST['status']
		customer_info = request.POST['customer_info']
		search_type = request.POST['search_type']
		search_type_list = ['姓名','手機','序號','IMEI']
		reservation = request.POST['reservation']
		start_date_text = reservation.split('/')[2].split(' ')[0] + '/' +reservation.split('/')[0] + '/' + reservation.split('/')[1]
		start_date = datetime.datetime.combine(datetime.datetime.strptime(start_date_text,"%Y/%m/%d") , datetime.time.min)
		end_date_text = reservation.split('/')[4] + '/' + reservation.split('/')[2].split(' ')[2] + '/' + reservation.split('/')[3]
		end_date = datetime.datetime.combine(datetime.datetime.strptime(end_date_text,"%Y/%m/%d") , datetime.time.max)
		print('start_date=',start_date)
		print('end_date=',end_date)
		print('phone_brand_choice=',phone_brand_choice,'status=',status,'customer_info=',customer_info,'search_type=',search_type)
		if customer_info == '':
			print('dd')
			if status == 'NO':
				costomer_manage_lists = Costomer_Manage.objects.filter(created_at__range = (start_date,end_date),customer_receive = False ,alive=True).order_by('-update_at')
			elif status == 'YES':
				costomer_manage_lists = Costomer_Manage.objects.filter(created_at__range = (start_date,end_date),customer_receive = True ,alive=True).order_by('-update_at')
			elif status == 'ALL':
				costomer_manage_lists = Costomer_Manage.objects.filter(created_at__range = (start_date,end_date),alive=True).order_by('-update_at')
		else:
			print('cc')
			if search_type == 'name':
				costomer_manage_lists = Costomer_Manage.objects.filter(customer_name = customer_info,alive=True).order_by('-update_at')
				search_type_text = search_type_list[0]
			elif search_type == 'phone':
				costomer_manage_lists = Costomer_Manage.objects.filter(customer_phone_num = customer_info,alive=True).order_by('-update_at')
				search_type_text = search_type_list[1]
			elif search_type == 'sn':
				if len(customer_info) > 5:
					costomer_manage_lists = Costomer_Manage.objects.filter(costomer_sn__startswith = customer_info,alive=True).order_by('-update_at')
					search_type_text = search_type_list[2]
			elif search_type == 'IMEI':
				if len(customer_info) > 5:
					costomer_manage_lists = Costomer_Manage.objects.filter(fix_part_sn_num__startswith = customer_info,alive=True).order_by('-update_at')
					search_type_text = search_type_list[3]
		engineer_none_lists = costomer_manage_lists.filter(engineer='')
		print('ee')
		date_text = (datetime.datetime.today() - datetime.timedelta(days=30)).strftime("%m/%d/%Y")+' - '+datetime.datetime.today().strftime("%m/%d/%Y")
		phone_brand_lists = Phone_Brand.objects.filter(alive=True)
		plus_buy_list_text = []
		fix_part_list_text = []
		
		for costomer_manage_list in costomer_manage_lists:
			temp_text = ''
			temp_fix_text = ''
			print('customer_name=',costomer_manage_list.customer_name,'update_at=',costomer_manage_list.update_at)
			plus_buy_list = costomer_manage_list.plus_buy.replace("'","").replace("[","").replace("]","").replace(' ','').split(',')
			plus_buy_list_price = costomer_manage_list.plus_buy_price.replace("'","").replace("[","").replace("]","").replace(' ','').split(',')
			fix_part_list = costomer_manage_list.fix_part.replace("'","").replace("[","").replace("]","").replace(' ','').split(',')
			# print('plus_buy_list=',plus_buy_list,'plus_buy_list_price=',plus_buy_list_price,'fix_part_list=',fix_part_list)
			if len(plus_buy_list) == 1:
				for i in range(len(plus_buy_list)):
					plus_buy_list_text.append(str(plus_buy_list[i]) + ' $' +str(plus_buy_list_price[i]))
			elif len(plus_buy_list) > 1:
				for i in range(len(plus_buy_list)):
					temp_text = temp_text + str(plus_buy_list[i]) + ' $' +str(plus_buy_list_price[i]) + ' '
				plus_buy_list_text.append(temp_text)
			else:
				plus_buy_list_text.append('無')
		
			for j in range(len(fix_part_list)):
				temp_fix_text = temp_fix_text + ' ' +str(fix_part_list[j])
			fix_part_list_text.append(temp_fix_text)
		if phone_brand_choice == 'none':
			phone_brand_choice_text = '全部'
		else:		
			phone_brand_choice_text = Phone_Brand.objects.get(phone_brand_num=phone_brand_choice,alive=True).phone_brand_name
		if status == 'ALL':
			status_text = '全部'
		elif status == 'YES':
			status_text = '已交件'
		elif status == 'NO':
			status_text = '未交件'

		costomer_manage_lists_zip = zip(costomer_manage_lists,plus_buy_list_text,fix_part_list_text)
		print('aa')
	except:
		date_text = (datetime.datetime.today() - datetime.timedelta(days=30)).strftime("%m/%d/%Y")+' - '+datetime.datetime.today().strftime("%m/%d/%Y")
		phone_brand_lists = Phone_Brand.objects.filter(alive=True)
		print('bb')

	response = render(request,'mainpage/fix_customer.html',locals())
	return response

def customer_table_engineer_post(request,purchase_num):
	story = 'story_1'
	engineer = request.user.username
	date_text = datetime.datetime.today()
	customer_info = Costomer_Manage.objects.get(costomer_sn = purchase_num,alive=True)
	Costomer_Manage.objects.filter(costomer_sn = purchase_num,alive=True).update(engineer = engineer,update_at = date_text)
	fix_part_text = customer_info.fix_part
	phone_name_num = Phone_name.objects.get(phone_brand_name = customer_info.phone_brand_num ,phone_name = customer_info.phone_name_num).phone_name_num
	Costomer_Fix_Managment.objects.create(costomer_sn=purchase_num,story=story,case_percent_1='100',engineer_1=engineer,case_percent_2='',engineer_2='',created_at = date_text , engineer_fix_1=fix_part_text,phone_name_num = phone_name_num)
	response = redirect('/customer_table')
	return response

def phone_brand(request):
	phone_name_amount = []
	phone_brand_list = []
	last_update_lists = []
	phone_brands = Phone_Brand.objects.filter(alive='True')
	for i in range(len(phone_brands)):
		phone_brand_list.append(phone_brands[i].phone_brand_name)
	for j in range(len(phone_brand_list)):
		phone_name = Phone_name.objects.filter(phone_brand_name=phone_brand_list[j],alive='True')
		if len(phone_name) == '0':
			phone_name_amount.append(0)
		else:
			phone_name_amount.append(len(phone_name))
		try:
			last_update_lists.append(phone_name.order_by('-update_at')[0].update_at)
		except:
			last_update_lists.append('none')

	phone_brand_list_zip = zip(phone_brands,phone_name_amount,last_update_lists)
	response = render(request,'mainpage/phone_brand.html',locals())
	return response

def phone_brand_create(request):
	phone_brand_name = request.POST['phone_brand']
	phone_brand_num = phone_brand_name[:2] + str(random.randint(10,99))
	Phone_Brand.objects.create(phone_brand_num=phone_brand_num,phone_brand_name=phone_brand_name,alive='True')
	response = redirect('/manage/phone_brand/')
	return response

def phone_name(request,phone_brand_num):
	stock_phone_list = []
	phone_brand = Phone_Brand.objects.get(phone_brand_num=phone_brand_num,alive='True')
	phone_brand_name = phone_brand.phone_brand_name
	phone_name_lists =  Phone_name.objects.filter(phone_brand_name=phone_brand_name,alive='True').order_by('phone_name')
	stock_phones = Stock_Phone_Manage.objects.filter(alive='True')
	for stock_phone in stock_phones:
		stock_phone_list.append(stock_phone.phone_name_num)
	response = render(request,'mainpage/phone_name.html',locals())
	return response

def phone_name_edit(request,phone_brand_num,phone_name_num):
	# phone_nam_color_list = []
	phone_brand = Phone_Brand.objects.get(phone_brand_num=phone_brand_num,alive='True')
	phone_brand_name = phone_brand.phone_brand_name
	phone_name_list =  Phone_name.objects.get(phone_name_num=phone_name_num,alive='True')
	phone_name_color_list = phone_name_list.phone_color.split(',')
	page_edit = 'True'
	response = render(request,'mainpage/phone_name.html',locals())
	return response	

def phone_name_edit_post(request,phone_brand_num,phone_name_num):
	time_now = datetime.datetime.today() + timedelta(hours=8)
	Phone_name.objects.filter(phone_name_num=phone_name_num,alive=True).update(alive=False,update_at=time_now)
	response = redirect('/manage/phone_name/'+ phone_brand_num)
	return response

def phone_name_del_post(request,phone_brand_num,phone_name_num):
	time_now = datetime.datetime.today() + timedelta(hours=8)
	Phone_name.objects.filter(phone_name_num=phone_name_num,alive=True).update(alive=False,update_at=time_now)
	response = redirect('/manage/phone_name/'+ phone_brand_num)
	return response

# def phone_name_create(request,phone_brand_num):
# 	phone_name = request.POST['phone_name']
# 	phone_color = request.POST['phone_color']
# 	phone_color_lists = phone_color.split(',')
# 	phone_brand = Phone_Brand.objects.get(phone_brand_num=phone_brand_num,alive='True')
# 	print(len(Phone_name.objects.filter(phone_name=phone_name,alive='True')))
# 	if len(Phone_name.objects.filter(phone_name=phone_name,alive='True')) == 0:
# 		print('bb')
# 		phone_name_rand = str(random.randint(100,999))
# 		for phone_color_list in phone_color_lists:
# 			if phone_color_list == '通用' :
# 				phone_name_num = str(phone_brand.phone_brand_num) + str(phone_name_rand) + '000'
# 				Phone_name.objects.create(phone_name_num=phone_name_num,phone_brand_name=phone_brand.phone_brand_name,phone_name=phone_name,phone_color=phone_color_list,alive='True')
# 			else:
# 				phone_name_num = str(phone_brand.phone_brand_num) + str(phone_name_rand) + str(random.randint(100,999))
# 				Phone_name.objects.create(phone_name_num=phone_name_num,phone_brand_name=phone_brand.phone_brand_name,phone_name=phone_name,phone_color=phone_color_list,alive='True')
# 	else:
# 		print(Phone_name.objects.filter(phone_name=phone_name,alive='True')[0].phone_name,phone_name)
# 		if Phone_name.objects.filter(phone_name=phone_name,alive='True')[0].phone_name == phone_name:
# 			print('ee')
# 			phone_name_rand = Phone_name.objects.filter(phone_name=phone_name,alive='True')[0].phone_name_num[4:7]
# 			for phone_color_list in phone_color_lists:
# 				print('ff')
# 				phone_name_num = str(phone_brand.phone_brand_num) + str(phone_name_rand) + str(random.randint(100,999))
# 				Phone_name.objects.create(phone_name_num=phone_name_num,phone_brand_name=phone_brand.phone_brand_name,phone_name=phone_name,phone_color=phone_color_list,alive='True')		
# 	response = redirect('/manage/phone_name/'+phone_brand_num)
# 	return response

def phone_name_create(request,phone_brand_num):
	phone_name = request.POST['phone_name']
	# phone_color = request.POST['phone_color']
	stock = request.POST['stock']
	print(stock)
	if stock == 'on':
		stock_text = True
	elif stock == 'off':
		stock_text = False
	# phone_color_lists = phone_color.split(',')
	phone_brand = Phone_Brand.objects.get(phone_brand_num=phone_brand_num,alive='True')
	print(len(Phone_name.objects.filter(phone_name=phone_name,alive='True')))
	if len(Phone_name.objects.filter(phone_name=phone_name,alive='True')) == 0:
		print('bb')
		phone_name_rand = str(random.randint(100,999))
		phone_name_num = str(phone_brand.phone_brand_num) + str(random.randint(100,999))
		Phone_name.objects.create(phone_name_num=phone_name_num,phone_brand_name=phone_brand.phone_brand_name,phone_name=phone_name,phone_color='',stock=stock_text,alive=True)
		r = requests.get('http://146.148.75.24/stock/stock_manage_init/'+phone_name_num)

	else:
		print(Phone_name.objects.filter(phone_name=phone_name,alive='True')[0].phone_name,phone_name)
		if Phone_name.objects.filter(phone_name=phone_name,alive='True')[0].phone_name == phone_name:
			print('ee')
			phone_name_rand = Phone_name.objects.filter(phone_name=phone_name,alive='True')[0].phone_name_num[4:7]
			for phone_color_list in phone_color_lists:
				print('ff')
				phone_name_num = str(phone_brand.phone_brand_num) + str(phone_name_rand) + str(random.randint(100,999))
				Phone_name.objects.create(phone_name_num=phone_name_num,phone_brand_name=phone_brand.phone_brand_name,phone_name=phone_name,phone_color='',stock=stock_text,alive='True')		
		r = requests.get('http://146.148.75.24/stock/stock_manage_init/'+phone_name_num)

	response = redirect('/manage/phone_name/'+phone_brand_num)
	return response

def accessories_name(request):
	accessories_name_lists = Accessories_Name.objects.filter(alive=True)
	count_lists = []
	for i in range(1,len(accessories_name_lists)+1):
		count_lists.append(i)
	accessories_lists = zip(count_lists,accessories_name_lists)
	response = render(request,'mainpage/accessories_table.html',locals())
	return response 

def accessories_name_post(request):
	alpha_list = random.sample('abcdefghijklmnopqrstuvwxyz',3)
	accessories_name = request.POST['accessories_name']
	accessories_price = request.POST['accessories_price']
	accessories_cost = request.POST['accessories_cost']
	accessories_note = request.POST['accessories_note']
	accessories_num = alpha_list[0]+alpha_list[1]+alpha_list[2]+str(random.randint(1000,9999))
	Accessories_Name.objects.create(accessories_num=accessories_num,accessories_name=accessories_name,accessories_price=accessories_price,accessories_cost=accessories_cost,accessories_note=accessories_note)
	response = redirect('/manage/accessories_name/')
	return response	

def accessories_name_del_post(request,num):
	Accessories_Name.objects.filter(accessories_num=num,alive=True).update(alive=False)
	response = redirect('/manage/accessories_name/')
	return response	


def fix_part_manage(request):
	fix_part_lists = Fix_Part_Manage.objects.filter(alive=True)
	count_lists = []
	for i in range(1,len(fix_part_lists)+1):
		count_lists.append(i)
	fix_part_manage_lists = zip(count_lists,fix_part_lists)
	response = render(request,'mainpage/fix_part_manage_table.html',locals())
	return response 

def fix_part_manage_post(request):
	alpha_list = random.sample('abcdefghijklmnopqrstuvwxyz',4)
	fix_part_name = request.POST['fix_part_name']
	fix_part_note = request.POST['fix_part_note']
	fix_part_num = alpha_list[0]+alpha_list[1]+str(random.randint(100,999))+alpha_list[2]+alpha_list[3]	
	Fix_Part_Manage.objects.create(fix_part_name=fix_part_name,fix_part_num=fix_part_num,fix_part_note=fix_part_note)
	response = redirect('/manage/fix_part_manage/')
	return response	

def fix_part_del_post(request,num):
	Fix_Part_Manage.objects.filter(fix_part_num=num,alive=True).update(alive=False)
	response = redirect('/manage/fix_part_manage/')
	return response	


def phone_color_manage(request):
	phone_color_lists = Phone_Color.objects.filter(alive=True)
	count_lists = []
	for i in range(1,len(phone_color_lists)+1):
		count_lists.append(i)
	phone_color_manage_lists = zip(count_lists,phone_color_lists)
	response = render(request,'mainpage/phone_color_manage_table.html',locals())
	return response 

def phone_color_manage_post(request):	
	alpha_list = random.sample('abcdefghijklmnopqrstuvwxyz',4)
	phone_color_name = request.POST['phone_color_name']
	phone_color_note = request.POST['phone_color_note']
	phone_color_num = alpha_list[0]+alpha_list[1]+str(random.randint(100,999))+alpha_list[2]+alpha_list[3]	
	Phone_Color.objects.create(phone_color_name=phone_color_name,phone_color_num=phone_color_num,phone_color_note=phone_color_note)
	response = redirect('/manage/phone_color_manage/')
	return response	

def phone_color_del_post(request,num):	
	Phone_Color.objects.filter(phone_color_num=num,alive=True).update(alive=False)
	response = redirect('/manage/phone_color_manage/')
	return response	
