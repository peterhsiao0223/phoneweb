from django.shortcuts import render,redirect
from stock.models import Stock_Phone_Parts,Stock_Phone_Fix_Parts,Stock_Phone_Manage,Stock_Phone_Amount,Stock_Fix_Manu,Stock_Phone_Purchase_Ng
from mainpage.models import Phone_name,Phone_Brand,Stock_Phone_Amount_Manage
from logfile.models import Stock_Phone_Purchase_Log,Stock_Phone_Purchase_Records
from managment_page.models import Stock_Phone_Parts_Price

from django.http import JsonResponse
from django.core import serializers
import datetime
from datetime import timedelta
import random
# Create your views here.
def demo(request):
	alert_text = '錯誤!!有料件重複!!'
	response = render(request,'stock/return_page.html',locals())
	return response

def stock_purchase(request,phone_name_num):
	phone_name_title_list = []
	phone_stock_num_list = []
	phone_name_title = []
	phone_name_lists = []
	phone_name_colors = []
	stock_phone_list = []
	part_name_lists = []
	stock_phones = Stock_Phone_Manage.objects.get(alive=True,phone_name_num=phone_name_num)
	phone_name_title_list.append(Phone_name.objects.get(alive=True,phone_name_num=phone_name_num).phone_brand_name)
	phone_name_title_list.append(Phone_name.objects.get(alive=True,phone_name_num=phone_name_num).phone_name)
	stock_fix_manu_lists = Stock_Fix_Manu.objects.filter(alive=True)
	values = []
	for i in range(1,21):
		values.append(i)
	response = render(request,'stock/stock_manage_purchase.html',locals())
	return response
	
def stock_purchase_post(request,phone_name_num):
	log_user = request.user.username
	part_num = ''
	stock_name_manage_lists = []
	part_num_lists = request.POST.getlist('part_name')
	stock_fix_manu_num = request.POST['stock_fix_manu_name']
	purchase_type = request.POST['purchase_type']
	stock_fix_manu_name = Stock_Fix_Manu.objects.get(stock_fix_manu_num=stock_fix_manu_num).stock_fix_manu_name
	part_name = ''
	stock_manage_num_lists = []
	print(phone_name_num)	
	stock_num_plus = []
	# phone_name_num = request.POST['phone_name_num']
	try:
		comment = request.POST['phone_comment']
	except:
		comment = ''
	stock_name_manage = Stock_Phone_Manage.objects.get(alive=True,phone_name_num=phone_name_num)
	if stock_name_manage.phone_fix_elements_1 != 'none':
		stock_name_manage_lists.append(stock_name_manage.phone_fix_elements_1)
	if stock_name_manage.phone_fix_elements_2 != 'none':
		stock_name_manage_lists.append(stock_name_manage.phone_fix_elements_2)
	if stock_name_manage.phone_fix_elements_3 != 'none':
		stock_name_manage_lists.append(stock_name_manage.phone_fix_elements_3)
	if stock_name_manage.phone_fix_elements_4 != 'none':
		stock_name_manage_lists.append(stock_name_manage.phone_fix_elements_4)
	if stock_name_manage.phone_fix_elements_5 != 'none':
		stock_name_manage_lists.append(stock_name_manage.phone_fix_elements_5)
	if stock_name_manage.phone_fix_elements_6 != 'none':
		stock_name_manage_lists.append(stock_name_manage.phone_fix_elements_6)
	if stock_name_manage.phone_fix_elements_7 != 'none':
		stock_name_manage_lists.append(stock_name_manage.phone_fix_elements_7)
	if stock_name_manage.phone_fix_elements_8 != 'none':
		stock_name_manage_lists.append(stock_name_manage.phone_fix_elements_8)
	if stock_name_manage.phone_fix_elements_9 != 'none':
		stock_name_manage_lists.append(stock_name_manage.phone_fix_elements_9)
	if stock_name_manage.phone_fix_elements_10 != 'none':
		stock_name_manage_lists.append(stock_name_manage.phone_fix_elements_10)
	if stock_name_manage.phone_fix_elements_11 != 'none':
		stock_name_manage_lists.append(stock_name_manage.phone_fix_elements_11)
	if stock_name_manage.phone_fix_elements_12 != 'none':
		stock_name_manage_lists.append(stock_name_manage.phone_fix_elements_12)
	if stock_name_manage.phone_fix_elements_13 != 'none':
		stock_name_manage_lists.append(stock_name_manage.phone_fix_elements_13)
	if stock_name_manage.phone_fix_elements_14 != 'none':
		stock_name_manage_lists.append(stock_name_manage.phone_fix_elements_14)
	if stock_name_manage.phone_fix_elements_15 != 'none':
		stock_name_manage_lists.append(stock_name_manage.phone_fix_elements_15)
	if stock_name_manage.phone_fix_elements_16 != 'none':
		stock_name_manage_lists.append(stock_name_manage.phone_fix_elements_16)
	if stock_name_manage.phone_fix_elements_17 != 'none':
		stock_name_manage_lists.append(stock_name_manage.phone_fix_elements_17)
	if stock_name_manage.phone_fix_elements_18 != 'none':
		stock_name_manage_lists.append(stock_name_manage.phone_fix_elements_18)
	if stock_name_manage.phone_fix_elements_19 != 'none':
		stock_name_manage_lists.append(stock_name_manage.phone_fix_elements_19)
	if stock_name_manage.phone_fix_elements_20 != 'none':
		stock_name_manage_lists.append(stock_name_manage.phone_fix_elements_20)

	for i in range(len(part_num_lists)):
		if part_num_lists[i] != '0':
			if i == (len(part_num_lists)-1):
				part_num = part_num  + str(part_num_lists[i])
				part_name = part_name + stock_name_manage_lists[i]
			else:
				part_num = part_num  + str(part_num_lists[i]) + ','
				part_name = part_name + stock_name_manage_lists[i] + ','

	# for j in range(len(stock_name_manage_lists)):
	# 	if j == 0 :
			
	# 	else:
			

	purchase_num = datetime.datetime.today().strftime("%Y%m%d") + str(phone_name_num) + str(random.randint(100,999))
	Stock_Phone_Purchase_Log.objects.create(purchase_num=purchase_num,phone_name_num=phone_name_num,log_user=log_user,purchase_type=purchase_type,part_name=part_name,part_num=part_num,stock_fix_manu_num=stock_fix_manu_name,comment=comment,create_at=datetime.datetime.now())
	stock_manage_num = Stock_Phone_Manage.objects.filter(phone_name_num=phone_name_num,alive=True)
	print('stock_manage_num=',stock_manage_num)
	stock_manage_num_lists.append(stock_manage_num[0].phone_fix_elements_num_1)
	stock_manage_num_lists.append(stock_manage_num[0].phone_fix_elements_num_2)
	stock_manage_num_lists.append(stock_manage_num[0].phone_fix_elements_num_3)
	stock_manage_num_lists.append(stock_manage_num[0].phone_fix_elements_num_4)
	stock_manage_num_lists.append(stock_manage_num[0].phone_fix_elements_num_5)
	stock_manage_num_lists.append(stock_manage_num[0].phone_fix_elements_num_6)
	stock_manage_num_lists.append(stock_manage_num[0].phone_fix_elements_num_7)
	stock_manage_num_lists.append(stock_manage_num[0].phone_fix_elements_num_8)
	stock_manage_num_lists.append(stock_manage_num[0].phone_fix_elements_num_9)
	stock_manage_num_lists.append(stock_manage_num[0].phone_fix_elements_num_10)
	stock_manage_num_lists.append(stock_manage_num[0].phone_fix_elements_num_11)
	stock_manage_num_lists.append(stock_manage_num[0].phone_fix_elements_num_12)
	stock_manage_num_lists.append(stock_manage_num[0].phone_fix_elements_num_13)
	stock_manage_num_lists.append(stock_manage_num[0].phone_fix_elements_num_14)
	stock_manage_num_lists.append(stock_manage_num[0].phone_fix_elements_num_15)
	stock_manage_num_lists.append(stock_manage_num[0].phone_fix_elements_num_16)
	stock_manage_num_lists.append(stock_manage_num[0].phone_fix_elements_num_17)
	stock_manage_num_lists.append(stock_manage_num[0].phone_fix_elements_num_18)
	stock_manage_num_lists.append(stock_manage_num[0].phone_fix_elements_num_19)
	stock_manage_num_lists.append(stock_manage_num[0].phone_fix_elements_num_20)

	if purchase_type == 'add':
		for i in range(len(part_num_lists)):
			print('i=',i,'原:',int(stock_manage_num_lists[i]),'加總後:',int(part_num_lists[i]))
			stock_num_plus.append(int(stock_manage_num_lists[i]) + int(part_num_lists[i]))
			print(stock_num_plus)
	elif purchase_type == 'ng':
		for j in range(len(part_num_lists)):
			print('j=',j,'原:',int(stock_manage_num_lists[j]),'相減後:',int(part_num_lists[j]))
			stock_num_plus.append(int(stock_manage_num_lists[j]) - int(part_num_lists[j]))
			print(stock_num_plus)
		Stock_Phone_Purchase_Ng.objects.create(purchase_num=purchase_num,phone_name_num=phone_name_num,log_user=log_user,purchase_type=purchase_type,part_name=part_name,part_num=part_num,stock_fix_manu_num=stock_fix_manu_name,comment=comment,finish_comment='',update_at=datetime.datetime.now(),create_at=datetime.datetime.now())
	elif purchase_type == 'ship':
		for k in range(len(part_num_lists)):
			print('k=',k,'原:',int(stock_manage_num_lists[k]),'相減後:',int(part_num_lists[k]))
			stock_num_plus.append(int(stock_manage_num_lists[k]) - int(part_num_lists[k]))
			print(stock_num_plus)
	print('stock_num_plus=',stock_num_plus)
	try:
		Stock_Phone_Manage.objects.filter(phone_name_num=phone_name_num,alive=True).update(phone_fix_elements_num_1=stock_num_plus[0])
	except:
		pass
	try:
		Stock_Phone_Manage.objects.filter(phone_name_num=phone_name_num,alive=True).update(phone_fix_elements_num_2=stock_num_plus[1])
	except:
		pass
	try:
		Stock_Phone_Manage.objects.filter(phone_name_num=phone_name_num,alive=True).update(phone_fix_elements_num_3=stock_num_plus[2])
	except:
		pass
	try:
		Stock_Phone_Manage.objects.filter(phone_name_num=phone_name_num,alive=True).update(phone_fix_elements_num_4=stock_num_plus[3])
	except:
		pass
	try:
		Stock_Phone_Manage.objects.filter(phone_name_num=phone_name_num,alive=True).update(phone_fix_elements_num_5=stock_num_plus[4])
	except:
		pass
	try:
		Stock_Phone_Manage.objects.filter(phone_name_num=phone_name_num,alive=True).update(phone_fix_elements_num_6=stock_num_plus[5])
	except:
		pass
	try:
		Stock_Phone_Manage.objects.filter(phone_name_num=phone_name_num,alive=True).update(phone_fix_elements_num_7=stock_num_plus[6])
	except:
		pass
	try:
		Stock_Phone_Manage.objects.filter(phone_name_num=phone_name_num,alive=True).update(phone_fix_elements_num_8=stock_num_plus[7])
	except:
		pass
	try:
		Stock_Phone_Manage.objects.filter(phone_name_num=phone_name_num,alive=True).update(phone_fix_elements_num_9=stock_num_plus[8])
	except:
		pass
	try:
		Stock_Phone_Manage.objects.filter(phone_name_num=phone_name_num,alive=True).update(phone_fix_elements_num_10=stock_num_plus[9])
	except:
		pass
	try:
		Stock_Phone_Manage.objects.filter(phone_name_num=phone_name_num,alive=True).update(phone_fix_elements_num_11=stock_num_plus[10])
	except:
		pass
	try:
		Stock_Phone_Manage.objects.filter(phone_name_num=phone_name_num,alive=True).update(phone_fix_elements_num_12=stock_num_plus[11])
	except:
		pass
	try:
		Stock_Phone_Manage.objects.filter(phone_name_num=phone_name_num,alive=True).update(phone_fix_elements_num_13=stock_num_plus[12])
	except:
		pass
	try:
		Stock_Phone_Manage.objects.filter(phone_name_num=phone_name_num,alive=True).update(phone_fix_elements_num_14=stock_num_plus[13])
	except:
		pass
	try:
		Stock_Phone_Manage.objects.filter(phone_name_num=phone_name_num,alive=True).update(phone_fix_elements_num_15=stock_num_plus[14])
	except:
		pass
	try:
		Stock_Phone_Manage.objects.filter(phone_name_num=phone_name_num,alive=True).update(phone_fix_elements_num_16=stock_num_plus[15])
	except:
		pass
	try:
		Stock_Phone_Manage.objects.filter(phone_name_num=phone_name_num,alive=True).update(phone_fix_elements_num_17=stock_num_plus[16])
	except:
		pass
	try:
		Stock_Phone_Manage.objects.filter(phone_name_num=phone_name_num,alive=True).update(phone_fix_elements_num_18=stock_num_plus[17])
	except:
		pass
	try:
		Stock_Phone_Manage.objects.filter(phone_name_num=phone_name_num,alive=True).update(phone_fix_elements_num_19=stock_num_plus[18])
	except:
		pass
	try:
		Stock_Phone_Manage.objects.filter(phone_name_num=phone_name_num,alive=True).update(phone_fix_elements_num_20=stock_num_plus[19])
	except:
		pass
	try:
		Stock_Phone_Manage.objects.filter(phone_name_num=phone_name_num,alive=True).update(phone_fix_elements_num_2=stock_num_plus[20])
	except:
		pass
	# if stock_num_plus[2]:
		# Stock_Phone_Manage.objects.filter(phone_name_num=phone_name_num,alive=True).update(phone_fix_elements_num_3=stock_num_plus[2])
		# Stock_Phone_Amount_Manage.objects.filter(phone_name_num=phone_name_num).update()
	print(stock_num_plus)
	response = redirect('/stock/manage_purchase/')
	return response

def stock_manage(request,phone_name_num):
	try:
		stock_phone_list = []
		titles = []
		phone_name_title_list = []
		stock_name_manage_list = []
		# phone_name_colors = []
		phone_name_title = []
		phone_stock_num_lists = []
		stock_phone_list_alls = []
		stock_name_manage_title_list = []
		phone_name_list = []
		# phone_name_all_colors = []
		if 'all' in phone_name_num :
			phone_brand_num = phone_name_num[3:]
			phone_brand_name = Phone_Brand.objects.get(alive=True,phone_brand_num=phone_brand_num).phone_brand_name
			phone_name_lists = Phone_name.objects.filter(alive=True,stock=True,phone_brand_name=phone_brand_name)
			for phone_name_list in phone_name_lists:
				stock_name_manage_list.append(Stock_Phone_Manage.objects.get(alive=True,phone_name_num=phone_name_list.phone_name_num))
				print(stock_name_manage_list)
				# stock_name_manage = 
				phone_name_title.append(str(Phone_name.objects.get(alive=True,stock=True,phone_name_num=phone_name_list.phone_name_num).phone_brand_name)+'/'+str(Phone_name.objects.get(alive=True,phone_name_num=phone_name_list.phone_name_num).phone_name))
				print(phone_name_title)
			stock_name_manage_lists = zip(phone_name_title,stock_name_manage_list)
			for i in range(1,21):
				titles.append(i)
			select_type = 'all'
			phone_name_title_list.append(Phone_Brand.objects.get(alive=True,phone_brand_num=phone_name_num[3:]).phone_brand_name)
			phone_name_title_list.append('總表')
		else:
			phone_name_list.append(Phone_name.objects.get(alive=True,stock=True,phone_name_num=phone_name_num).phone_brand_name)
			phone_name_list.append(Phone_name.objects.get(alive=True,stock=True,phone_name_num=phone_name_num).phone_name)
			stock_name_manage = Stock_Phone_Manage.objects.get(alive=True,phone_name_num=phone_name_num)
			select_type = 'one'

			phone_name_title_list.append(Phone_name.objects.get(alive=True,stock=True,phone_name_num=phone_name_num).phone_brand_name)
			phone_name_title_list.append(Phone_name.objects.get(alive=True,stock=True,phone_name_num=phone_name_num).phone_name)
	except:
		phone_name_title_list.append(Phone_name.objects.get(alive=True,phone_name_num=phone_name_num).phone_brand_name)
		phone_name_title_list.append(Phone_name.objects.get(alive=True,phone_name_num=phone_name_num).phone_name)
	response = render(request,'stock/stock_manage.html',locals())
	return response	

	# stock_phones = Stock_Phone_Manage.objects.filter(alive=True)
	# stock_phones = Stock_Phone_Amount_Manage.objects.filter(alive=True)
	# phone_color_names = Phone_name.objects.filter(alive=True).order_by('phone_name_num')

	# for stock_phone in stock_phones:
	# 	stock_phone_list.append(stock_phone.phone_name_num)

	# for phone_name in phone_names:
	# 	if phone_name_num in phone_name.phone_name_num and phone_name.phone_name_num in stock_phone_list:
	# 		phone_name_title = phone_name.phone_brand_name
	# 		phone_name_lists.append(phone_name.phone_name)
	# 		# phone_name_colors.append(phone_name.phone_color)
	# 		try:
	# 			phone_stock_num_lists.append(Stock_Phone_Manage.objects.filter(phone_name_num=phone_name.phone_name_num)[0])
	# 			# print(phone_stock_num_list)
	# 		except:
	# 			phone_stock_num_lists.append(' ')
	# 			# print('error')
	# try:
	# 	phone_name_title_list.append(phone_name_title)
	# 	phone_name_title_list.append(phone_name_lists[0].split(' (')[0])
	# 	phone_name_lists_zip = zip(phone_name_lists,phone_stock_num_lists)
	# except:
	# 	pass
	# print(phone_stock_num_lists[0].phone_fix_elements_num_1)


def stock_manage_init(request,phone_name_num):
	stock_phone_parts_lists = []
	phone_story = 'story1'
	phone_fix_elements_num_text = ''
	for i in range(20):
		phone_fix_elements_num_text = phone_fix_elements_num_text + '0,'
		if i == 19:
			phone_fix_elements_num_text = phone_fix_elements_num_text + '0'
	# stock_phone_parts = Stock_Phone_Fix_Parts.objects.all()
	stock_phone_manages = Stock_Phone_Manage.objects.filter(alive=True)
	for stock_phone_manage in stock_phone_manages:
		if phone_name_num == stock_phone_manage.phone_name_num:
			response = redirect('/stock/manage/'+phone_name_num[:7]+'/all')
			return response
	# for i in range(len(stock_phone_parts)):
		# stock_phone_parts_lists.append(stock_phone_parts[i].phone_fix_parts)
	Stock_Phone_Manage.objects.create(phone_name_num=phone_name_num,phone_story='story1')
	Stock_Phone_Parts_Price.objects.create(phone_name_num=phone_name_num)
	# Stock_Phone_Amount_Manage.objects.create(phone_name_num=phone_name_num,phone_fix_elements_num=phone_fix_elements_num_text,phone_story=phone_story)
	response = redirect('/manage/phone_name/'+phone_name_num[:4])
	return response


def stock_manage_brand_search(request):
	stock_type = 'search'
	phone_brands = Phone_Brand.objects.filter(alive=True).order_by('phone_brand_name')
	phone_name_lists = []
	phone_names = Phone_name.objects.filter(alive=True,stock='True')
	for phone_name in phone_names:
		if (phone_name.phone_name_num[:7]+phone_name.phone_name) in phone_name_lists:
			pass
		else:
			phone_name_lists.append(phone_name.phone_name_num+phone_name.phone_name)
	response = render(request,'stock/stock_manage_brand.html',locals())
	return response

def stock_manage_brand_purchase(request):
	stock_type = 'purchase'
	phone_brands = Phone_Brand.objects.filter(alive=True).order_by('phone_brand_name')
	phone_name_lists = []
	phone_names = Phone_name.objects.filter(alive=True)
	for phone_name in phone_names:
		if (phone_name.phone_name_num[:7]+phone_name.phone_name) in phone_name_lists:
			pass
		else:
			phone_name_lists.append(phone_name.phone_name_num[:7]+phone_name.phone_name)
	response = render(request,'stock/stock_manage_brand.html',locals())
	return response

def stock_manage_ship(request):
	stock_type = 'ship'
	phone_brands = Phone_Brand.objects.filter(alive=True).order_by('phone_brand_name')
	phone_name_lists = []
	phone_names = Phone_name.objects.filter(alive=True)
	for phone_name in phone_names:
		if (phone_name.phone_name_num[:7]+phone_name.phone_name) in phone_name_lists:
			pass
		else:
			phone_name_lists.append(phone_name.phone_name_num[:7]+phone_name.phone_name)
	response = render(request,'stock/stock_manage_brand.html',locals())
	return response

def stock_ship(request,phone_name_num):
	phone_name_title_list = []
	phone_stock_num_list = []
	phone_name_title = []
	phone_name_lists = []
	phone_name_colors = []
	stock_phone_list = []
	stock_phones = Stock_Phone_Manage.objects.get(alive=True,phone_name_num=phone_name_num)
	phone_name_title_list.append(Phone_name.objects.get(alive=True,phone_name_num=phone_name_num).phone_brand_name)
	phone_name_title_list.append(Phone_name.objects.get(alive=True,phone_name_num=phone_name_num).phone_name)
	stock_fix_manu_lists = Stock_Fix_Manu.objects.filter(alive=True)
	values = []
	for i in range(1,21):
		values.append(i)
	response = render(request,'stock/stock_ship.html',locals())
	return response

def stock_manage_ng_ship(request):
	stock_type = 'ng'
	phone_brands = Phone_Brand.objects.filter(alive=True).order_by('phone_brand_name')
	phone_name_lists = []
	phone_names = Phone_name.objects.filter(alive=True)
	for phone_name in phone_names:
		if (phone_name.phone_name_num[:7]+phone_name.phone_name) in phone_name_lists:
			pass
		else:
			phone_name_lists.append(phone_name.phone_name_num[:7]+phone_name.phone_name)
	response = render(request,'stock/stock_manage_brand.html',locals())
	return response



def stock_ng_ship(request,phone_name_num):
	phone_name_title_list = []
	phone_stock_num_list = []
	phone_name_title = []
	phone_name_lists = []
	phone_name_colors = []
	stock_phone_list = []
	stock_phones = Stock_Phone_Manage.objects.get(alive=True,phone_name_num=phone_name_num)
	phone_name_title_list.append(Phone_name.objects.get(alive=True,phone_name_num=phone_name_num).phone_brand_name)
	phone_name_title_list.append(Phone_name.objects.get(alive=True,phone_name_num=phone_name_num).phone_name)
	stock_fix_manu_lists = Stock_Fix_Manu.objects.filter(alive=True)
	values = []
	for i in range(1,21):
		values.append(i)
	response = render(request,'stock/stock_ng_ship.html',locals())
	return response


def get_phone_name_api(request):
	phone_names = Phone_name.objects.filter(alive=True)
	data = serializers.serialize('json',phone_names)
	return JsonResponse({'data':data})

def stock_name_manage(request):
	phone_name_lists = []
	count_lists = []
	title_lists = []
	stock_name_manage = Stock_Phone_Manage.objects.filter(alive=True)
	# phone_name = Phone_name.objects.filter(alive=True)
	for i in range(len(stock_name_manage)):
		phone_name = stock_name_manage[i].phone_name_num
		print(phone_name)
		phone_name_lists.append(str(Phone_name.objects.get(phone_name_num=phone_name).phone_brand_name)+'/'+str(Phone_name.objects.get(phone_name_num=phone_name).phone_name))

	for j in range(1,21):
		title_lists.append(j)
	for k in range(1,len(stock_name_manage)+1):
		count_lists.append(k)
	stock_name_manage_lists = zip(count_lists,stock_name_manage,phone_name_lists)
	response = render(request,'stock/stock_name_manage.html',locals())
	return response

def stock_name_manage_edit(request,phone_name_num):
	title_lists = []
	phone_name = []
	stock_name_manage = Stock_Phone_Manage.objects.get(alive=True,phone_name_num=phone_name_num)
	phone_name.append(Phone_name.objects.get(alive=True,phone_name_num=phone_name_num).phone_brand_name)
	phone_name.append(Phone_name.objects.get(alive=True,phone_name_num=phone_name_num).phone_name)
	for j in range(1,21):
		title_lists.append(j)
	page_edit = 'True'
	response = render(request,'stock/stock_name_manage.html',locals())
	return response	

def stock_name_manage_edit_post(request,phone_name_num):
	stock_name_edit = request.POST.getlist('stock_name_edit')
	print(stock_name_edit)
	for i in range(len(stock_name_edit)):
		if stock_name_edit[i] == '':
			stock_name_edit[i] = 'none'
	print(stock_name_edit)
	time_now = datetime.datetime.today() + timedelta(hours=8)
	Stock_Phone_Manage.objects.filter(phone_name_num=phone_name_num,alive=True).update(phone_fix_elements_1=stock_name_edit[0],phone_fix_elements_2=stock_name_edit[1],phone_fix_elements_3=stock_name_edit[2],phone_fix_elements_4=stock_name_edit[3],phone_fix_elements_5=stock_name_edit[4],phone_fix_elements_6=stock_name_edit[5],phone_fix_elements_7=stock_name_edit[6],phone_fix_elements_8=stock_name_edit[7],phone_fix_elements_9=stock_name_edit[8],phone_fix_elements_10=stock_name_edit[9],phone_fix_elements_11=stock_name_edit[10],phone_fix_elements_12=stock_name_edit[11],phone_fix_elements_13=stock_name_edit[12],phone_fix_elements_14=stock_name_edit[13],phone_fix_elements_15=stock_name_edit[14],phone_fix_elements_16=stock_name_edit[15],phone_fix_elements_17=stock_name_edit[16],phone_fix_elements_18=stock_name_edit[17],phone_fix_elements_19=stock_name_edit[18],phone_fix_elements_20=stock_name_edit[19],update_at=time_now)
	Stock_Phone_Parts_Price.objects.filter(phone_name_num=phone_name_num,alive=True).update(phone_fix_elements_1=stock_name_edit[0],phone_fix_elements_2=stock_name_edit[1],phone_fix_elements_3=stock_name_edit[2],phone_fix_elements_4=stock_name_edit[3],phone_fix_elements_5=stock_name_edit[4],phone_fix_elements_6=stock_name_edit[5],phone_fix_elements_7=stock_name_edit[6],phone_fix_elements_8=stock_name_edit[7],phone_fix_elements_9=stock_name_edit[8],phone_fix_elements_10=stock_name_edit[9],phone_fix_elements_11=stock_name_edit[10],phone_fix_elements_12=stock_name_edit[11],phone_fix_elements_13=stock_name_edit[12],phone_fix_elements_14=stock_name_edit[13],phone_fix_elements_15=stock_name_edit[14],phone_fix_elements_16=stock_name_edit[15],phone_fix_elements_17=stock_name_edit[16],phone_fix_elements_18=stock_name_edit[17],phone_fix_elements_19=stock_name_edit[18],phone_fix_elements_20=stock_name_edit[19],update_at=time_now)
	response = redirect('/manage/stock_manage/')
	return response

def stock_name_manage_order(request,phone_name_num):
	title_lists = []
	count_lists = []
	stock_name_manage = Stock_Phone_Manage.objects.get(alive=True,phone_name_num=phone_name_num)
	if stock_name_manage.phone_fix_elements_1 != 'none':
		count_lists.append(stock_name_manage.phone_fix_elements_1)
	if stock_name_manage.phone_fix_elements_2 != 'none':
		count_lists.append(stock_name_manage.phone_fix_elements_2)
	if stock_name_manage.phone_fix_elements_3 != 'none':
		count_lists.append(stock_name_manage.phone_fix_elements_3)
	if stock_name_manage.phone_fix_elements_4 != 'none':
		count_lists.append(stock_name_manage.phone_fix_elements_4)
	if stock_name_manage.phone_fix_elements_5 != 'none':
		count_lists.append(stock_name_manage.phone_fix_elements_5)
	if stock_name_manage.phone_fix_elements_6 != 'none':
		count_lists.append(stock_name_manage.phone_fix_elements_6)
	if stock_name_manage.phone_fix_elements_7 != 'none':
		count_lists.append(stock_name_manage.phone_fix_elements_7)
	if stock_name_manage.phone_fix_elements_8 != 'none':
		count_lists.append(stock_name_manage.phone_fix_elements_8)
	if stock_name_manage.phone_fix_elements_9 != 'none':
		count_lists.append(stock_name_manage.phone_fix_elements_9)
	if stock_name_manage.phone_fix_elements_10 != 'none':
		count_lists.append(stock_name_manage.phone_fix_elements_10)
	if stock_name_manage.phone_fix_elements_11 != 'none':
		count_lists.append(stock_name_manage.phone_fix_elements_11)
	if stock_name_manage.phone_fix_elements_12 != 'none':
		count_lists.append(stock_name_manage.phone_fix_elements_12)
	if stock_name_manage.phone_fix_elements_13 != 'none':
		count_lists.append(stock_name_manage.phone_fix_elements_13)
	if stock_name_manage.phone_fix_elements_14 != 'none':
		count_lists.append(stock_name_manage.phone_fix_elements_14)
	if stock_name_manage.phone_fix_elements_15 != 'none':
		count_lists.append(stock_name_manage.phone_fix_elements_15)
	if stock_name_manage.phone_fix_elements_16 != 'none':
		count_lists.append(stock_name_manage.phone_fix_elements_16)
	if stock_name_manage.phone_fix_elements_17 != 'none':
		count_lists.append(stock_name_manage.phone_fix_elements_17)
	if stock_name_manage.phone_fix_elements_18 != 'none':
		count_lists.append(stock_name_manage.phone_fix_elements_18)
	if stock_name_manage.phone_fix_elements_19 != 'none':
		count_lists.append(stock_name_manage.phone_fix_elements_19)
	if stock_name_manage.phone_fix_elements_20 != 'none':
		count_lists.append(stock_name_manage.phone_fix_elements_20)
	for j in range(1,len(count_lists)+1):
		title_lists.append(j)
	phone_fix_elements_zip = zip(title_lists,count_lists)
	response = render(request,'stock/stock_name_manage_order.html',locals())
	return response

def stock_name_manage_order_post(request,phone_name_num):
	select_orders = request.POST.getlist('select_order')
	stock_phone_manage_dict = {}
	select_orders_dict = {}
	stock_phone_manage = Stock_Phone_Manage.objects.get(phone_name_num = phone_name_num,alive=True)
	if stock_phone_manage.phone_fix_elements_1 != 'none':
		stock_phone_manage_dict.update({stock_phone_manage.phone_fix_elements_1:stock_phone_manage.phone_fix_elements_num_1})
	if stock_phone_manage.phone_fix_elements_2 != 'none':
		stock_phone_manage_dict.update({stock_phone_manage.phone_fix_elements_2:stock_phone_manage.phone_fix_elements_num_2})
	if stock_phone_manage.phone_fix_elements_3 != 'none':
		stock_phone_manage_dict.update({stock_phone_manage.phone_fix_elements_3:stock_phone_manage.phone_fix_elements_num_3})
	if stock_phone_manage.phone_fix_elements_4 != 'none':
		stock_phone_manage_dict.update({stock_phone_manage.phone_fix_elements_4:stock_phone_manage.phone_fix_elements_num_4})
	if stock_phone_manage.phone_fix_elements_5 != 'none':
		stock_phone_manage_dict.update({stock_phone_manage.phone_fix_elements_5:stock_phone_manage.phone_fix_elements_num_5})
	if stock_phone_manage.phone_fix_elements_6 != 'none':
		stock_phone_manage_dict.update({stock_phone_manage.phone_fix_elements_6:stock_phone_manage.phone_fix_elements_num_6})
	if stock_phone_manage.phone_fix_elements_7 != 'none':
		stock_phone_manage_dict.update({stock_phone_manage.phone_fix_elements_7:stock_phone_manage.phone_fix_elements_num_7})
	if stock_phone_manage.phone_fix_elements_8 != 'none':
		stock_phone_manage_dict.update({stock_phone_manage.phone_fix_elements_8:stock_phone_manage.phone_fix_elements_num_8})
	if stock_phone_manage.phone_fix_elements_9 != 'none':
		stock_phone_manage_dict.update({stock_phone_manage.phone_fix_elements_9:stock_phone_manage.phone_fix_elements_num_9})
	if stock_phone_manage.phone_fix_elements_10 != 'none':
		stock_phone_manage_dict.update({stock_phone_manage.phone_fix_elements_10:stock_phone_manage.phone_fix_elements_num_10})
	if stock_phone_manage.phone_fix_elements_11 != 'none':
		stock_phone_manage_dict.update({stock_phone_manage.phone_fix_elements_11:stock_phone_manage.phone_fix_elements_num_11})
	if stock_phone_manage.phone_fix_elements_12 != 'none':
		stock_phone_manage_dict.update({stock_phone_manage.phone_fix_elements_12:stock_phone_manage.phone_fix_elements_num_12})
	if stock_phone_manage.phone_fix_elements_13 != 'none':
		stock_phone_manage_dict.update({stock_phone_manage.phone_fix_elements_13:stock_phone_manage.phone_fix_elements_num_13})
	if stock_phone_manage.phone_fix_elements_14 != 'none':
		stock_phone_manage_dict.update({stock_phone_manage.phone_fix_elements_14:stock_phone_manage.phone_fix_elements_num_14})
	if stock_phone_manage.phone_fix_elements_15 != 'none':
		stock_phone_manage_dict.update({stock_phone_manage.phone_fix_elements_15:stock_phone_manage.phone_fix_elements_num_15})
	if stock_phone_manage.phone_fix_elements_16 != 'none':
		stock_phone_manage_dict.update({stock_phone_manage.phone_fix_elements_16:stock_phone_manage.phone_fix_elements_num_16})
	if stock_phone_manage.phone_fix_elements_17 != 'none':
		stock_phone_manage_dict.update({stock_phone_manage.phone_fix_elements_17:stock_phone_manage.phone_fix_elements_num_17})
	if stock_phone_manage.phone_fix_elements_18 != 'none':
		stock_phone_manage_dict.update({stock_phone_manage.phone_fix_elements_18:stock_phone_manage.phone_fix_elements_num_18})
	if stock_phone_manage.phone_fix_elements_19 != 'none':
		stock_phone_manage_dict.update({stock_phone_manage.phone_fix_elements_19:stock_phone_manage.phone_fix_elements_num_19})
	if stock_phone_manage.phone_fix_elements_20 != 'none':
		stock_phone_manage_dict.update({stock_phone_manage.phone_fix_elements_20:stock_phone_manage.phone_fix_elements_num_20})
	for i in range(len(select_orders)):
		select_orders_dict.update({select_orders[i]:stock_phone_manage_dict[select_orders[i]]})
		for j in range(i+1,len(select_orders)):
			if select_orders[i] == select_orders[j]:
				alert_text = '錯誤!!有料件重複!!'
				response = render(request,'stock/return_page.html',locals())
				return response
	try:
		if select_orders[0] != 'none':
			Stock_Phone_Manage.objects.filter(alive=True,phone_name_num=phone_name_num).update(phone_fix_elements_1=select_orders[0],phone_fix_elements_num_1=stock_phone_manage_dict[select_orders[0]])
		if select_orders[1] != 'none':
			Stock_Phone_Manage.objects.filter(alive=True,phone_name_num=phone_name_num).update(phone_fix_elements_2=select_orders[1],phone_fix_elements_num_2=stock_phone_manage_dict[select_orders[1]])
		if select_orders[2] != 'none':
			Stock_Phone_Manage.objects.filter(alive=True,phone_name_num=phone_name_num).update(phone_fix_elements_3=select_orders[2],phone_fix_elements_num_3=stock_phone_manage_dict[select_orders[2]])
		if select_orders[3] != 'none':
			Stock_Phone_Manage.objects.filter(alive=True,phone_name_num=phone_name_num).update(phone_fix_elements_4=select_orders[3],phone_fix_elements_num_4=stock_phone_manage_dict[select_orders[3]])
		if select_orders[4] != 'none':
			Stock_Phone_Manage.objects.filter(alive=True,phone_name_num=phone_name_num).update(phone_fix_elements_5=select_orders[4],phone_fix_elements_num_5=stock_phone_manage_dict[select_orders[4]])
		if select_orders[5] != 'none':
			Stock_Phone_Manage.objects.filter(alive=True,phone_name_num=phone_name_num).update(phone_fix_elements_6=select_orders[5],phone_fix_elements_num_6=stock_phone_manage_dict[select_orders[5]])
		if select_orders[6] != 'none':
			Stock_Phone_Manage.objects.filter(alive=True,phone_name_num=phone_name_num).update(phone_fix_elements_7=select_orders[6],phone_fix_elements_num_7=stock_phone_manage_dict[select_orders[6]])
		if select_orders[7] != 'none':
			Stock_Phone_Manage.objects.filter(alive=True,phone_name_num=phone_name_num).update(phone_fix_elements_8=select_orders[7],phone_fix_elements_num_8=stock_phone_manage_dict[select_orders[7]])
		if select_orders[8] != 'none':
			Stock_Phone_Manage.objects.filter(alive=True,phone_name_num=phone_name_num).update(phone_fix_elements_9=select_orders[8],phone_fix_elements_num_9=stock_phone_manage_dict[select_orders[8]])
		if select_orders[9] != 'none':
			Stock_Phone_Manage.objects.filter(alive=True,phone_name_num=phone_name_num).update(phone_fix_elements_10=select_orders[9],phone_fix_elements_num_10=stock_phone_manage_dict[select_orders[9]])
		if select_orders[10] != 'none':
			Stock_Phone_Manage.objects.filter(alive=True,phone_name_num=phone_name_num).update(phone_fix_elements_11=select_orders[10],phone_fix_elements_num_11=stock_phone_manage_dict[select_orders[10]])
		if select_orders[11] != 'none':
			Stock_Phone_Manage.objects.filter(alive=True,phone_name_num=phone_name_num).update(phone_fix_elements_12=select_orders[11],phone_fix_elements_num_12=stock_phone_manage_dict[select_orders[11]])
		if select_orders[12] != 'none':
			Stock_Phone_Manage.objects.filter(alive=True,phone_name_num=phone_name_num).update(phone_fix_elements_13=select_orders[12],phone_fix_elements_num_13=stock_phone_manage_dict[select_orders[12]])
		if select_orders[13] != 'none':
			Stock_Phone_Manage.objects.filter(alive=True,phone_name_num=phone_name_num).update(phone_fix_elements_14=select_orders[13],phone_fix_elements_num_14=stock_phone_manage_dict[select_orders[13]])
		if select_orders[14] != 'none':
			Stock_Phone_Manage.objects.filter(alive=True,phone_name_num=phone_name_num).update(phone_fix_elements_15=select_orders[14],phone_fix_elements_num_15=stock_phone_manage_dict[select_orders[14]])
		if select_orders[15] != 'none':
			Stock_Phone_Manage.objects.filter(alive=True,phone_name_num=phone_name_num).update(phone_fix_elements_16=select_orders[15],phone_fix_elements_num_16=stock_phone_manage_dict[select_orders[15]])
		if select_orders[16] != 'none':
			Stock_Phone_Manage.objects.filter(alive=True,phone_name_num=phone_name_num).update(phone_fix_elements_17=select_orders[16],phone_fix_elements_num_17=stock_phone_manage_dict[select_orders[16]])
		if select_orders[17] != 'none':
			Stock_Phone_Manage.objects.filter(alive=True,phone_name_num=phone_name_num).update(phone_fix_elements_18=select_orders[17],phone_fix_elements_num_18=stock_phone_manage_dict[select_orders[17]])
		if select_orders[18] != 'none':
			Stock_Phone_Manage.objects.filter(alive=True,phone_name_num=phone_name_num).update(phone_fix_elements_19=select_orders[18],phone_fix_elements_num_19=stock_phone_manage_dict[select_orders[18]])
		if select_orders[19] != 'none':
			Stock_Phone_Manage.objects.filter(alive=True,phone_name_num=phone_name_num).update(phone_fix_elements_20=select_orders[19],phone_fix_elements_num_20=stock_phone_manage_dict[select_orders[19]])
	except:
		pass
	count = len(select_orders)
	print(select_orders)
	print(count)
	print(select_orders_dict)
	print(stock_phone_manage_dict)
	response = redirect('/stock/manage/'+phone_name_num)
	return response

def stock_fix_manu(request):
	stock_fix_manu_lists = Stock_Fix_Manu.objects.filter(alive=True)
	count_lists = []
	for i in range(1,len(stock_fix_manu_lists)+1):
		count_lists.append(i)
	stock_fix_manu_lists_zip = zip(count_lists,stock_fix_manu_lists)
	response = render(request,'stock/stock_fix_manu_table.html',locals())
	return response 

def stock_fix_manu_post(request):
	alpha_list = random.sample('abcdefghijklmnopqrstuvwxyz',3)
	stock_fix_manu_name = request.POST['stock_fix_manu_name']
	stock_fix_manu_phone = request.POST['stock_fix_manu_phone']
	stock_fix_manu_note = request.POST['stock_fix_manu_note']
	stock_fix_manu_num = alpha_list[0]+alpha_list[1]+alpha_list[2]+str(random.randint(1000,9999))
	Stock_Fix_Manu.objects.create(stock_fix_manu_num=stock_fix_manu_num,stock_fix_manu_name=stock_fix_manu_name,stock_fix_manu_phone=stock_fix_manu_phone,stock_fix_manu_note=stock_fix_manu_note)
	response = redirect('/manage/stock_fix_manu/')
	return response

def stock_fix_manu_del_post(request,num):
	Stock_Fix_Manu.objects.filter(stock_fix_manu_num=num,alive=True).update(alive=False)
	response = redirect('/manage/stock_fix_manu/')
	return response

def stock_phone_purchase_logfile(request):
	try:
		date_text = (datetime.datetime.today() - datetime.timedelta(days=30)).strftime("%m/%d/%Y")+' - '+datetime.datetime.today().strftime("%m/%d/%Y")
		phone_brand_lists = Phone_Brand.objects.filter(alive=True)
		stock_fix_manu_lists = Stock_Fix_Manu.objects.filter(alive=True)
		date_month_lists = ['1','2','3','6','12']
		date_month_text_lists = ['1個月','2個月','3個月','6個月','1年']
		date_month_text_zip = zip(date_month_lists,date_month_text_lists)
		
		reservation = request.POST['reservation']
		phone_brand_choice = request.POST['phone_brand_choice']
		stock_fix_manu_choice = request.POST['stock_fix_manu_choice']
		date_month = request.POST['date_month']
		phone_name_lists = []
		stock_phone_purchase_lists = Stock_Phone_Purchase_Log.objects.all()
		stock_num_lists = []

		if date_month == 'none':
			start_date_list = reservation.split('-')[0].replace(' ','').split('/')
			start_date = datetime.date(int(start_date_list[2]),int(start_date_list[0]),int(start_date_list[1]))
			print(start_date)
		elif date_month == '12':
			start_date_list = datetime.datetime.today().strftime("%m/%d/%Y").split('/')
			print('start_date_list=',start_date_list)
			start_date_list[2] = int(start_date_list[2])-1
			start_date = datetime.date(int(start_date_list[2]),int(start_date_list[0]),int(start_date_list[1]))
			print(start_date)
		else:
			start_date_list = datetime.datetime.today().strftime("%m/%d/%Y").split('/')
			print('start_date_list=',start_date_list)
			start_date_list[0] = int(start_date_list[0])-int(date_month)
			if start_date_list[0] <= 0 :
				start_date_list[0] = start_date_list[0] + 12
				start_date_list[2] = int(start_date_list[2])-1
				print('aa')
			print('bb')
			start_date = datetime.date(int(start_date_list[2]),int(start_date_list[0]),int(start_date_list[1]))
			print(start_date)
		print('cc')
		end_date_list = reservation.split('-')[1].replace(' ','').split('/')
		end_date = datetime.date(int(end_date_list[2]),int(end_date_list[0]),int(end_date_list[1])+1)

		if stock_fix_manu_choice == 'none':
			stock_fix_manu_choice = ''
			stock_fix_manu_text = '全部'
			print('dd')
		else:
			stock_fix_manu_choice = Stock_Fix_Manu.objects.get(stock_fix_manu_num = stock_fix_manu_choice).stock_fix_manu_name
			stock_fix_manu_text = stock_fix_manu_choice
			print('ee')

		if phone_brand_choice == 'none':
			phone_brand_choice = ''
			phone_brand_text = '全部'
			print('ff')
		else:
			phone_brand_text = Phone_Brand.objects.get(phone_brand_num = phone_brand_choice).phone_brand_name
			print('gg')

		stock_phone_purchase_lists =  Stock_Phone_Purchase_Log.objects.filter(phone_name_num__contains=phone_brand_choice,stock_fix_manu_num__contains=stock_fix_manu_choice,create_at__range=(start_date,end_date)).order_by('-create_at')
		print('stock_phone_purchase_lists=',stock_phone_purchase_lists)

		
		for stock_phone_purchase in stock_phone_purchase_lists:
			# stock_phone_purchase_log = Logfile_Stock_Phone_Purchase_Log.objects.all()
			phone_name_lists.append(str(Phone_name.objects.get(phone_name_num = stock_phone_purchase.phone_name_num).phone_brand_name) + '/' +str(Phone_name.objects.get(phone_name_num = stock_phone_purchase.phone_name_num).phone_name))
			stock_num_text = ''
			phone_name_num = stock_phone_purchase.phone_name_num
			# stock_manage = Stock_Phone_Manage.objects.get(alive=True,phone_name_num=phone_name_num)
			# stock_manage_phone_fix_elements = []
			# if stock_manage.phone_fix_elements_1 != 'none':
			# 	stock_manage_phone_fix_elements.append(stock_manage.phone_fix_elements_1)
			# if stock_manage.phone_fix_elements_2 != 'none':
			# 	stock_manage_phone_fix_elements.append(stock_manage.phone_fix_elements_2)
			# if stock_manage.phone_fix_elements_3 != 'none':
			# 	stock_manage_phone_fix_elements.append(stock_manage.phone_fix_elements_3)
			# if stock_manage.phone_fix_elements_4 != 'none':
			# 	stock_manage_phone_fix_elements.append(stock_manage.phone_fix_elements_4)
			# if stock_manage.phone_fix_elements_5 != 'none':
			# 	stock_manage_phone_fix_elements.append(stock_manage.phone_fix_elements_5)
			# if stock_manage.phone_fix_elements_6 != 'none':
			# 	stock_manage_phone_fix_elements.append(stock_manage.phone_fix_elements_6)
			# if stock_manage.phone_fix_elements_7 != 'none':
			# 	stock_manage_phone_fix_elements.append(stock_manage.phone_fix_elements_7)
			# if stock_manage.phone_fix_elements_8 != 'none':
			# 	stock_manage_phone_fix_elements.append(stock_manage.phone_fix_elements_8)
			# if stock_manage.phone_fix_elements_9 != 'none':
			# 	stock_manage_phone_fix_elements.append(stock_manage.phone_fix_elements_9)
			# if stock_manage.phone_fix_elements_10 != 'none':
			# 	stock_manage_phone_fix_elements.append(stock_manage.phone_fix_elements_10)
			# if stock_manage.phone_fix_elements_11 != 'none':
			# 	stock_manage_phone_fix_elements.append(stock_manage.phone_fix_elements_11)
			# if stock_manage.phone_fix_elements_12 != 'none':
			# 	stock_manage_phone_fix_elements.append(stock_manage.phone_fix_elements_12)
			# if stock_manage.phone_fix_elements_13 != 'none':
			# 	stock_manage_phone_fix_elements.append(stock_manage.phone_fix_elements_13)
			# if stock_manage.phone_fix_elements_14 != 'none':
			# 	stock_manage_phone_fix_elements.append(stock_manage.phone_fix_elements_14)
			# if stock_manage.phone_fix_elements_15 != 'none':
			# 	stock_manage_phone_fix_elements.append(stock_manage.phone_fix_elements_15)
			# if stock_manage.phone_fix_elements_16 != 'none':
			# 	stock_manage_phone_fix_elements.append(stock_manage.phone_fix_elements_16)
			# if stock_manage.phone_fix_elements_17!= 'none':
			# 	stock_manage_phone_fix_elements.append(stock_manage.phone_fix_elements_17)
			# if stock_manage.phone_fix_elements_18 != 'none':
			# 	stock_manage_phone_fix_elements.append(stock_manage.phone_fix_elements_18)
			# if stock_manage.phone_fix_elements_19 != 'none':
			# 	stock_manage_phone_fix_elements.append(stock_manage.phone_fix_elements_19)
			# if stock_manage.phone_fix_elements_20 != 'none':
			# 	stock_manage_phone_fix_elements.append(stock_manage.phone_fix_elements_20)
			print('stock_phone_purchase.part_name=',stock_phone_purchase.part_name)
			print('stock_phone_purchase.part_num=',stock_phone_purchase.part_num)
			for i in range(len(stock_phone_purchase.part_num.split(','))):
				stock_num_text = stock_num_text + stock_phone_purchase.part_name.split(',')[i] + stock_phone_purchase.part_num.split(',')[i] +' '
				print('stock_num_text===', stock_num_text)
			stock_num_lists.append(stock_num_text)
		# print('stock_num_text=',stock_num_text)
		part_num_lists = []
		count_lists = []
		for i in range(1,len(stock_phone_purchase_lists)+1):
			count_lists.append(i)
		stock_phone_purchase_lists_zip = zip(count_lists,stock_num_lists,stock_phone_purchase_lists,phone_name_lists)
	except:
		date_text = (datetime.datetime.today() - datetime.timedelta(days=30)).strftime("%m/%d/%Y")+' - '+datetime.datetime.today().strftime("%m/%d/%Y")
		phone_brand_lists = Phone_Brand.objects.filter(alive=True)
		stock_fix_manu_lists = Stock_Fix_Manu.objects.filter(alive=True)
		date_month_lists = ['1','2','3','6','12']
		date_month_text_lists = ['1個月','2個月','3個月','6個月','1年']
		date_month_text_zip = zip(date_month_lists,date_month_text_lists)
	response = render(request,'stock/stock_phone_purchase.html',locals())
	return response 

def stock_phone_manage_ship(request):
	try:
		reservation = request.POST['reservation']
		status = request.POST['status']
		phone_brand_choice = request.POST['phone_brand_choice']
		stock_fix_manu_choice = request.POST['stock_fix_manu_choice']
		date_month = request.POST['date_month']
		print(reservation)
		print(status)
		print(phone_brand_choice)
		print(stock_fix_manu_choice)
		print(date_month)
		stock_num_lists = []
		phone_name_lists = []
		start_date_list = datetime.datetime.today().strftime("%m/%d/%Y").split('/')
		print('start_date_list=',start_date_list)
		
		print(start_date_list)
		if date_month == 'none':
			start_date_list = reservation.split('-')[0].replace(' ','').split('/')
			start_date = datetime.date(int(start_date_list[2]),int(start_date_list[0]),int(start_date_list[1]))
			print(start_date)
		elif date_month == '12':
			start_date_list = datetime.datetime.today().strftime("%m/%d/%Y").split('/')
			print('start_date_list=',start_date_list)
			start_date_list[2] = int(start_date_list[2])-1
			start_date = datetime.date(int(start_date_list[2]),int(start_date_list[0]),int(start_date_list[1]))
			print(start_date)
		else:
			start_date_list = datetime.datetime.today().strftime("%m/%d/%Y").split('/')
			print('start_date_list=',start_date_list)
			start_date_list[0] = int(start_date_list[0])-int(date_month)
			if start_date_list[0] <= 0 :
				start_date_list[0] = start_date_list[0] + 12
				start_date_list[2] = int(start_date_list[2])-1
			start_date = datetime.date(int(start_date_list[2]),int(start_date_list[0]),int(start_date_list[1]))
			print(start_date)
		end_date_list = reservation.split('-')[1].replace(' ','').split('/')
		end_date = datetime.date(int(end_date_list[2]),int(end_date_list[0]),int(end_date_list[1])+1)
		print('start_date=',start_date,'end_date=',end_date)
		print('stock_fix_manu_choice=',stock_fix_manu_choice,'phone_brand_choice=',phone_brand_choice)
		if status == 'YES':
			status_text = '未出庫'
		elif status == 'NO':
			status_text = '已出庫'
		else:
			status_text = '全部'
		if stock_fix_manu_choice == 'none':
			stock_fix_manu_choice = ''
			stock_fix_manu_text = '全部'
		else:
			stock_fix_manu_choice = Stock_Fix_Manu.objects.get(stock_fix_manu_num = stock_fix_manu_choice).stock_fix_manu_name
			stock_fix_manu_text = stock_fix_manu_choice
		if phone_brand_choice == 'none':
			phone_brand_choice = ''
			phone_brand_text = '全部'
		else:
			phone_brand_text = Phone_Brand.objects.get(phone_brand_num = phone_brand_choice).phone_brand_name
		print('stock_fix_manu_choice=',stock_fix_manu_choice,'phone_brand_choice=',phone_brand_choice)
		# stock_phone_purchase_ng = Stock_Phone_Purchase_Ng.objects.filter(phone_name_num__contains=phone_brand_choice,stock_fix_manu_num__contains=stock_fix_manu_choice,create_at__range=(start_date,end_date))
		# print('stock_phone_purchase_ng=',stock_phone_purchase_ng)
		if status == 'YES':
			print(status)
			stock_phone_ng_lists = Stock_Phone_Purchase_Ng.objects.filter(phone_name_num__contains=phone_brand_choice,stock_fix_manu_num__contains=stock_fix_manu_choice,create_at__range=(start_date,end_date),alive=False)
			print('stock_phone_ng_lists=',stock_phone_ng_lists)
		elif status == 'NO':
			print(status)
			stock_phone_ng_lists = Stock_Phone_Purchase_Ng.objects.filter(phone_name_num__contains=phone_brand_choice,stock_fix_manu_num__contains=stock_fix_manu_choice,create_at__range=(start_date,end_date),alive=True)
			print('stock_phone_ng_lists=',stock_phone_ng_lists)
		else:
			print(status)
			stock_phone_ng_lists =  Stock_Phone_Purchase_Ng.objects.filter(phone_name_num__contains=phone_brand_choice,stock_fix_manu_num__contains=stock_fix_manu_choice,create_at__range=(start_date,end_date))
			print('stock_phone_ng_lists=',stock_phone_ng_lists)
		for stock_phone_ng in stock_phone_ng_lists:
			# stock_phone_ng_log = Logfile_Stock_Phone_Purchase_Log.objects.all()
			phone_name_lists.append(str(Phone_name.objects.get(phone_name_num = stock_phone_ng.phone_name_num).phone_brand_name) + '/' +str(Phone_name.objects.get(phone_name_num = stock_phone_ng.phone_name_num).phone_name))
			stock_num_text = ''
			phone_name_num = stock_phone_ng.phone_name_num
			stock_manage = Stock_Phone_Manage.objects.get(alive=True,phone_name_num=phone_name_num)
			stock_manage_phone_fix_elements = []
			if stock_manage.phone_fix_elements_1 != 'none':
				stock_manage_phone_fix_elements.append(stock_manage.phone_fix_elements_1)
			if stock_manage.phone_fix_elements_2 != 'none':
				stock_manage_phone_fix_elements.append(stock_manage.phone_fix_elements_2)
			if stock_manage.phone_fix_elements_3 != 'none':
				stock_manage_phone_fix_elements.append(stock_manage.phone_fix_elements_3)
			if stock_manage.phone_fix_elements_4 != 'none':
				stock_manage_phone_fix_elements.append(stock_manage.phone_fix_elements_4)
			if stock_manage.phone_fix_elements_5 != 'none':
				stock_manage_phone_fix_elements.append(stock_manage.phone_fix_elements_5)
			if stock_manage.phone_fix_elements_6 != 'none':
				stock_manage_phone_fix_elements.append(stock_manage.phone_fix_elements_6)
			if stock_manage.phone_fix_elements_7 != 'none':
				stock_manage_phone_fix_elements.append(stock_manage.phone_fix_elements_7)
			if stock_manage.phone_fix_elements_8 != 'none':
				stock_manage_phone_fix_elements.append(stock_manage.phone_fix_elements_8)
			if stock_manage.phone_fix_elements_9 != 'none':
				stock_manage_phone_fix_elements.append(stock_manage.phone_fix_elements_9)
			if stock_manage.phone_fix_elements_10 != 'none':
				stock_manage_phone_fix_elements.append(stock_manage.phone_fix_elements_10)
			if stock_manage.phone_fix_elements_11 != 'none':
				stock_manage_phone_fix_elements.append(stock_manage.phone_fix_elements_11)
			if stock_manage.phone_fix_elements_12 != 'none':
				stock_manage_phone_fix_elements.append(stock_manage.phone_fix_elements_12)
			if stock_manage.phone_fix_elements_13 != 'none':
				stock_manage_phone_fix_elements.append(stock_manage.phone_fix_elements_13)
			if stock_manage.phone_fix_elements_14 != 'none':
				stock_manage_phone_fix_elements.append(stock_manage.phone_fix_elements_14)
			if stock_manage.phone_fix_elements_15 != 'none':
				stock_manage_phone_fix_elements.append(stock_manage.phone_fix_elements_15)
			if stock_manage.phone_fix_elements_16 != 'none':
				stock_manage_phone_fix_elements.append(stock_manage.phone_fix_elements_16)
			if stock_manage.phone_fix_elements_17!= 'none':
				stock_manage_phone_fix_elements.append(stock_manage.phone_fix_elements_17)
			if stock_manage.phone_fix_elements_18 != 'none':
				stock_manage_phone_fix_elements.append(stock_manage.phone_fix_elements_18)
			if stock_manage.phone_fix_elements_19 != 'none':
				stock_manage_phone_fix_elements.append(stock_manage.phone_fix_elements_19)
			if stock_manage.phone_fix_elements_20 != 'none':
				stock_manage_phone_fix_elements.append(stock_manage.phone_fix_elements_20)
			for i in range(len(stock_phone_ng.part_num.split(','))):
				stock_num_text = stock_num_text + stock_manage_phone_fix_elements[i] + stock_phone_ng.part_num.split(',')[i] +' '
			stock_num_lists.append(stock_num_text)
		print('stock_num_text=',type(stock_num_text))
		part_num_lists = []
		count_lists = []

		date_text = (datetime.datetime.today() - datetime.timedelta(days=30)).strftime("%m/%d/%Y")+' - '+datetime.datetime.today().strftime("%m/%d/%Y")
		phone_brand_lists = Phone_Brand.objects.filter(alive=True)
		stock_fix_manu_lists = Stock_Fix_Manu.objects.filter(alive=True)
		date_month_lists = ['1','2','3','6','12']
		date_month_text_lists = ['1個月','2個月','3個月','6個月','1年']
		date_month_text_zip = zip(date_month_lists,date_month_text_lists)

		for i in range(1,len(stock_phone_ng_lists)+1):
			count_lists.append(i)
		stock_phone_ng_lists_zip = zip(count_lists,stock_num_lists,stock_phone_ng_lists,phone_name_lists)
	except:
		date_text = (datetime.datetime.today() - datetime.timedelta(days=30)).strftime("%m/%d/%Y")+' - '+datetime.datetime.today().strftime("%m/%d/%Y")
		phone_brand_lists = Phone_Brand.objects.filter(alive=True)
		stock_fix_manu_lists = Stock_Fix_Manu.objects.filter(alive=True)
		date_month_lists = ['1','2','3','6','12']
		date_month_text_lists = ['1個月','2個月','3個月','6個月','1年']
		date_month_text_zip = zip(date_month_lists,date_month_text_lists)
		 # (datetime.datetime.today() - datetime.timedelta(months=1)).strftime("%Y/%m/%d")
		# 01/01/2016 - 01/25/2016

	response = render(request,'stock/stock_phone_ship.html',locals())
	return response 

def stock_phone_ship_form(request):
	conut_list = []
	stock_phone_purchase_ng_num_lists = []
	phone_name_num_lists = []
	purchase_num_lists = request.POST.getlist('table_records')
	print('purchase_num_lists=',purchase_num_lists,type(purchase_num_lists))
	stock_phone_purchase_ng_lists = Stock_Phone_Purchase_Ng.objects.filter(purchase_num__in=purchase_num_lists,alive=True)
	for stock_phone_purchase_ng_list in stock_phone_purchase_ng_lists:
		text = ''
		part_name_list = stock_phone_purchase_ng_list.part_name.split(',')
		part_num_list = stock_phone_purchase_ng_list.part_num.split(',')
		for i in range(len(part_name_list)):
			phone_name_num_lists.append(str(Phone_name.objects.get(phone_name_num=stock_phone_purchase_ng_list.phone_name_num,alive=True).phone_brand_name)+'/'+str(Phone_name.objects.get(phone_name_num=stock_phone_purchase_ng_list.phone_name_num,alive=True).phone_name))
			print('part_name_list',part_name_list[i])
			print('part_num_list',part_num_list[i])
			if i == int(len(part_name_list) - 1):
				text = text + part_name_list[i] + '[' + part_num_list[i] + ']'
			else:
				text = text + part_name_list[i] + '[' + part_num_list[i] + '],'
		stock_phone_purchase_ng_num_lists.append(text)
	for i in range(1,len(stock_phone_purchase_ng_lists)+1):
		conut_list.append(i)

	# purchase_num_lists = table_records.replace(' ','').split(',')
	# print('table_records=',table_records,type(table_records))
	stock_phone_purchase_ng_all_lists = zip(phone_name_num_lists,stock_phone_purchase_ng_num_lists,stock_phone_purchase_ng_lists)
	response = render(request,'stock/stock_phone_ship_form.html',locals())
	return response

def stock_phone_ship_form_post(request):
	log_user = request.user.username
	purchase_num = request.POST.getlist('purchase_num')
	finish_comment = request.POST.getlist('finish_comment')
	phone_name_num = request.POST.getlist('phone_name_num')
	for i in range(len(phone_name_num)):
		Stock_Phone_Purchase_Ng.objects.filter(purchase_num = purchase_num[i],phone_name_num = phone_name_num[i]).update(alive=False,finish_comment=finish_comment[i],update_at=datetime.datetime.now())
	print('phone_name_num',phone_name_num,'finish_comment',finish_comment,'purchase_num',purchase_num)
	Stock_Phone_Purchase_Records.objects.create(purchase_num = purchase_num,log_user=log_user)
	response = redirect('/manage/stock_phone_ship/')
	return response



def stock_phone_manage_ship_post(request,purchase_num):
	finish_comment = request.POST['finish_comment']
	Stock_Phone_Purchase_Ng.objects.filter(purchase_num=purchase_num,alive=True).update(alive=False,finish_comment=finish_comment,update_at=datetime.datetime.now())
	response = redirect('/manage/stock_phone_ship/')
	return response

def stock_phone_ship_info(request,purchase_num):
	phone_name_num = purchase_num[8:15]
	stock_num_text = ''
	# stock_phone_ng =  Stock_Phone_Purchase_Ng.objects.get(purchase_num=purchase_num,alive=False)
	stock_phone_ng =  Stock_Phone_Purchase_Ng.objects.get(purchase_num=purchase_num)
	stock_manage = Stock_Phone_Manage.objects.get(alive=True,phone_name_num=phone_name_num)
	stock_manage_phone_fix_elements = []
	if stock_manage.phone_fix_elements_1 != 'none':
		stock_manage_phone_fix_elements.append(stock_manage.phone_fix_elements_1)
	if stock_manage.phone_fix_elements_2 != 'none':
		stock_manage_phone_fix_elements.append(stock_manage.phone_fix_elements_2)
	if stock_manage.phone_fix_elements_3 != 'none':
		stock_manage_phone_fix_elements.append(stock_manage.phone_fix_elements_3)
	if stock_manage.phone_fix_elements_4 != 'none':
		stock_manage_phone_fix_elements.append(stock_manage.phone_fix_elements_4)
	if stock_manage.phone_fix_elements_5 != 'none':
		stock_manage_phone_fix_elements.append(stock_manage.phone_fix_elements_5)
	if stock_manage.phone_fix_elements_6 != 'none':
		stock_manage_phone_fix_elements.append(stock_manage.phone_fix_elements_6)
	if stock_manage.phone_fix_elements_7 != 'none':
		stock_manage_phone_fix_elements.append(stock_manage.phone_fix_elements_7)
	if stock_manage.phone_fix_elements_8 != 'none':
		stock_manage_phone_fix_elements.append(stock_manage.phone_fix_elements_8)
	if stock_manage.phone_fix_elements_9 != 'none':
		stock_manage_phone_fix_elements.append(stock_manage.phone_fix_elements_9)
	if stock_manage.phone_fix_elements_10 != 'none':
		stock_manage_phone_fix_elements.append(stock_manage.phone_fix_elements_10)
	if stock_manage.phone_fix_elements_11 != 'none':
		stock_manage_phone_fix_elements.append(stock_manage.phone_fix_elements_11)
	if stock_manage.phone_fix_elements_12 != 'none':
		stock_manage_phone_fix_elements.append(stock_manage.phone_fix_elements_12)
	if stock_manage.phone_fix_elements_13 != 'none':
		stock_manage_phone_fix_elements.append(stock_manage.phone_fix_elements_13)
	if stock_manage.phone_fix_elements_14 != 'none':
		stock_manage_phone_fix_elements.append(stock_manage.phone_fix_elements_14)
	if stock_manage.phone_fix_elements_15 != 'none':
		stock_manage_phone_fix_elements.append(stock_manage.phone_fix_elements_15)
	if stock_manage.phone_fix_elements_16 != 'none':
		stock_manage_phone_fix_elements.append(stock_manage.phone_fix_elements_16)
	if stock_manage.phone_fix_elements_17!= 'none':
		stock_manage_phone_fix_elements.append(stock_manage.phone_fix_elements_17)
	if stock_manage.phone_fix_elements_18 != 'none':
		stock_manage_phone_fix_elements.append(stock_manage.phone_fix_elements_18)
	if stock_manage.phone_fix_elements_19 != 'none':
		stock_manage_phone_fix_elements.append(stock_manage.phone_fix_elements_19)
	if stock_manage.phone_fix_elements_20 != 'none':
		stock_manage_phone_fix_elements.append(stock_manage.phone_fix_elements_20)
	for i in range(len(stock_phone_ng.part_num.split(','))):
		stock_num_text = stock_num_text + stock_manage_phone_fix_elements[i] + stock_phone_ng.part_num.split(',')[i] +' '

	# stock_phone_ng = Stock_Phone_Purchase_Ng.objects.get(purchase_num=purchase_num,alive=False)
	phone_brand_name_text = Phone_name.objects.get(phone_name_num = stock_phone_ng.phone_name_num).phone_brand_name
	phone_name_text = Phone_name.objects.get(phone_name_num = stock_phone_ng.phone_name_num).phone_name
	response = render(request,'stock/stock_phone_ship_info.html',locals())
	return response