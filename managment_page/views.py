from django.shortcuts import render,redirect
from django.contrib.auth.models import User,Group
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth import login

from engineer_manage.models import Story_List_Managment,Engineer_List_Managment
from stock.models import Stock_Phone_Manage
from mainpage.models import Phone_name
from managment_page.models import Stock_Phone_Parts_Price
import datetime
from datetime import timedelta
# Create your views here.

def post_login(request):
	username = request.POST['username']
	password = request.POST['password']
	user = authenticate(username=username,password=password)
	if user is not None:
		auth.login(request,user)
		# story = Story_Player.objects.get(play_list=username).story_num
		return redirect('/')
	else:
		return redirect('/accounts/login/')
		return  response

def post_logout(request):
	auth.logout(request)
	return redirect('/accounts/login/')

@login_required
def user_manage(request):
	# can_read_group = ['tch_admin_1','tch_admin_2']
	can_read_user = ['admin1','doraflower','peterhsiao']
	user_storys = Story_List_Managment.objects.filter(alive=True)
	group_list = []
	# user_story = Story_Player.objects.get(play_list=request.user.username)
	try:
		chg_delete_user = request.POST['chg_delete_user']
		user_delete = 'True'
		print('aa')
		response = render(request,'management/user_manage.html',locals())
		return response
	except:

		if request.user.username not in can_read_user:
			response = redirect('/')
			
		elif request.user.username in can_read_user:

			# group = request.user.groups.values_list('name',flat=True)[0]
			# user_story = Story_Player.objects.get(play_list=request.user.username)
			Users_list = User.objects.all().order_by('-date_joined')
			for i in range(len(Users_list)):
				group_list.append(Users_list[i].groups.get().name)
			Users_list_zip = zip(Users_list,group_list)
			response = render(request,'management_page/user_manage.html',locals())
		return response

@login_required
def user_add(request):
	# can_read_group = ['tch_admin_1','tch_admin_2']
	page_type = 'add'
	group = request.user.groups.values_list('name',flat=True)[0]
	user_story_lists = Story_List_Managment.objects.filter(alive=True)
	response = render(request,'management_page/profile.html',locals())
	return response

@login_required
def user_profile(request):
	page_type = 'profile'
	story = User.objects.get(username=request.user.username).groups.get().name
	response = render(request,'management_page/profile.html',locals())
	return response	

@login_required
def user_add_post(request):
	can_read_group = ['tch_admin_1','tch_admin_2']
	username = request.POST['username']
	name = request.POST['name']
	nickname = request.POST['nickname']
	password = request.POST['password']
	group_mod = request.POST['group_mod']
	story = request.POST['story']
	print('aa')
	# if nickname:
	user = User.objects.create(username=username,first_name=name,last_name=story+group_mod)
	# else:
	# 	user = User.objects.create(username=username,first_name=name)
	user.set_password(password)
	user.save()
	print('bb')
	if 'engineer' in group_mod:
		g = Group.objects.get(name=group_mod)
		g.user_set.add(user)
		Engineer_List_Managment.objects.create(story = story , engineer_num = username , engineer_name = name)
		print('cc')
	elif 'staff' in group_mod:
		g = Group.objects.get(name=group_mod)
		g.user_set.add(user)
		Engineer_List_Managment.objects.create(story = story , engineer_num = username , engineer_name = name)
		print('cc')
	response = redirect('/manage/user_manage/')
	return response	

@login_required
def change_user_pw(request,chg_user):
	story = User.objects.get(username=request.user.username).groups.get().name
	page_type = 'profile'
	# if request.user.is_authenticated():
	# 	old_password = request.POST['old_password']
	try:
		# username = request.POST['chg_user']
		username = chg_user
		new_password = '000000'
		new_password_check = '000000'
		user = User.objects.get(username=username)
		user.set_password(new_password)
		user.save()
		response = redirect('/manage/user_manage/')
		return response
	except:
		username = request.user.username
		new_password = request.POST['new_password']
		new_password_check = request.POST['new_password_check']

		if new_password == new_password_check:
			user = User.objects.get(username=username)
			user.set_password(new_password)
			user.save()
			auth.logout(request)
			response = redirect('/manage/user_manage/')
			return response
		else:
			alert_text = '兩次密碼錯誤!! 請確認密碼!!'
			response = render(request,'management_page/return_page.html',locals())
			return response

def stock_price_manage(request):
	phone_name_lists = []
	count_lists = []
	title_lists = []
	list_ = []
	
	stock_price_manage = Stock_Phone_Parts_Price.objects.filter(alive=True)
	for l in range(len(stock_price_manage)):
		list_.append(stock_price_manage[l].phone_name_num)
	stock_name_manage = Stock_Phone_Manage.objects.filter(alive=True,phone_name_num__in = list_)
	print('stock_name_manage=',stock_name_manage,'stock_price_manage=',stock_price_manage)
	# phone_name = Phone_name.objects.filter(alive=True)
	for i in range(len(stock_name_manage)):
		phone_name = stock_name_manage[i].phone_name_num
		print(phone_name)
		phone_name_lists.append(str(Phone_name.objects.get(alive=True,phone_name_num=phone_name).phone_brand_name)+'/'+str(Phone_name.objects.get(alive=True,phone_name_num=phone_name).phone_name))

	for j in range(1,21):
		title_lists.append(j)
	for k in range(1,len(stock_name_manage)+1):
		count_lists.append(k)
	stock_name_manage_lists = zip(count_lists,stock_name_manage,stock_price_manage,phone_name_lists)
	response = render(request,'management_page/stock_price_manage.html',locals())
	return response

def stock_price_manage_edit(request,phone_name_num):
	title_lists = []
	phone_name = []
	stock_name_manage = Stock_Phone_Manage.objects.get(alive=True,phone_name_num=phone_name_num)
	stock_price_manage = Stock_Phone_Parts_Price.objects.get(alive=True,phone_name_num=phone_name_num)
	phone_name.append(Phone_name.objects.get(alive=True,phone_name_num=phone_name_num).phone_brand_name)
	phone_name.append(Phone_name.objects.get(alive=True,phone_name_num=phone_name_num).phone_name)
	for j in range(1,21):
		title_lists.append(j)
	page_edit = 'True'
	response = render(request,'management_page/stock_price_manage.html',locals())
	return response	

def stock_price_manage_edit_post(request,phone_name_num):
	stock_name = request.POST.getlist('stock_name')
	stock_price_edit = request.POST.getlist('stock_price')
	print(stock_price_edit)
	stock_phone = Stock_Phone_Parts_Price.objects.get(alive=True,phone_name_num=phone_name_num)
	time_now = datetime.datetime.today() + timedelta(hours=8)
	for i in range(len(stock_name)):
		if stock_phone.phone_fix_elements_1 == stock_name[i]:
			Stock_Phone_Parts_Price.objects.filter(alive=True,phone_name_num=phone_name_num).update(phone_fix_elements_price_1 = stock_price_edit[i])
		if stock_phone.phone_fix_elements_2 == stock_name[i]:
			Stock_Phone_Parts_Price.objects.filter(alive=True,phone_name_num=phone_name_num).update(phone_fix_elements_price_2 = stock_price_edit[i])
		if stock_phone.phone_fix_elements_3 == stock_name[i]:
			Stock_Phone_Parts_Price.objects.filter(alive=True,phone_name_num=phone_name_num).update(phone_fix_elements_price_3 = stock_price_edit[i])
		if stock_phone.phone_fix_elements_4 == stock_name[i]:
			Stock_Phone_Parts_Price.objects.filter(alive=True,phone_name_num=phone_name_num).update(phone_fix_elements_price_4 = stock_price_edit[i])
		if stock_phone.phone_fix_elements_5 == stock_name[i]:
			Stock_Phone_Parts_Price.objects.filter(alive=True,phone_name_num=phone_name_num).update(phone_fix_elements_price_5 = stock_price_edit[i])
		if stock_phone.phone_fix_elements_6 == stock_name[i]:
			Stock_Phone_Parts_Price.objects.filter(alive=True,phone_name_num=phone_name_num).update(phone_fix_elements_price_6 = stock_price_edit[i])
		if stock_phone.phone_fix_elements_7 == stock_name[i]:
			Stock_Phone_Parts_Price.objects.filter(alive=True,phone_name_num=phone_name_num).update(phone_fix_elements_price_7 = stock_price_edit[i])
		if stock_phone.phone_fix_elements_8 == stock_name[i]:
			Stock_Phone_Parts_Price.objects.filter(alive=True,phone_name_num=phone_name_num).update(phone_fix_elements_price_8 = stock_price_edit[i])
		if stock_phone.phone_fix_elements_9 == stock_name[i]:
			Stock_Phone_Parts_Price.objects.filter(alive=True,phone_name_num=phone_name_num).update(phone_fix_elements_price_9 = stock_price_edit[i])
		if stock_phone.phone_fix_elements_10 == stock_name[i]:
			Stock_Phone_Parts_Price.objects.filter(alive=True,phone_name_num=phone_name_num).update(phone_fix_elements_price_10 = stock_price_edit[i])
		if stock_phone.phone_fix_elements_11 == stock_name[i]:
			Stock_Phone_Parts_Price.objects.filter(alive=True,phone_name_num=phone_name_num).update(phone_fix_elements_price_11 = stock_price_edit[i])
		if stock_phone.phone_fix_elements_12 == stock_name[i]:
			Stock_Phone_Parts_Price.objects.filter(alive=True,phone_name_num=phone_name_num).update(phone_fix_elements_price_12 = stock_price_edit[i])
		if stock_phone.phone_fix_elements_13 == stock_name[i]:
			Stock_Phone_Parts_Price.objects.filter(alive=True,phone_name_num=phone_name_num).update(phone_fix_elements_price_13 = stock_price_edit[i])
		if stock_phone.phone_fix_elements_14 == stock_name[i]:
			Stock_Phone_Parts_Price.objects.filter(alive=True,phone_name_num=phone_name_num).update(phone_fix_elements_price_14 = stock_price_edit[i])
		if stock_phone.phone_fix_elements_15 == stock_name[i]:
			Stock_Phone_Parts_Price.objects.filter(alive=True,phone_name_num=phone_name_num).update(phone_fix_elements_price_15 = stock_price_edit[i])
		if stock_phone.phone_fix_elements_16 == stock_name[i]:
			Stock_Phone_Parts_Price.objects.filter(alive=True,phone_name_num=phone_name_num).update(phone_fix_elements_price_16 = stock_price_edit[i])
		if stock_phone.phone_fix_elements_17 == stock_name[i]:
			Stock_Phone_Parts_Price.objects.filter(alive=True,phone_name_num=phone_name_num).update(phone_fix_elements_price_17 = stock_price_edit[i])
		if stock_phone.phone_fix_elements_18 == stock_name[i]:
			Stock_Phone_Parts_Price.objects.filter(alive=True,phone_name_num=phone_name_num).update(phone_fix_elements_price_18 = stock_price_edit[i])
		if stock_phone.phone_fix_elements_19 == stock_name[i]:
			Stock_Phone_Parts_Price.objects.filter(alive=True,phone_name_num=phone_name_num).update(phone_fix_elements_price_19 = stock_price_edit[i])
		if stock_phone.phone_fix_elements_20 == stock_name[i]:
			Stock_Phone_Parts_Price.objects.filter(alive=True,phone_name_num=phone_name_num).update(phone_fix_elements_price_20 = stock_price_edit[i])
	Stock_Phone_Parts_Price.objects.filter(alive=True,phone_name_num=phone_name_num).update(update_at = time_now)
	response = redirect('/manage/stock_price_manage/')
	return response
