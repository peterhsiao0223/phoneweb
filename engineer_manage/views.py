from django.shortcuts import render,redirect
import datetime
# from engineer_fix.models import Costomer_Fix_Manage
from mainpage.models import Phone_Brand,Phone_name,Accessories_Name,Fix_Part_Manage,Phone_Color,Stock_Phone_Amount_Manage,Costomer_Manage
from engineer_manage.models import Costomer_Fix_Managment,Engineer_List_Managment,Story_List_Managment
from stock.models import Stock_Phone_Manage,Stock_Phone_Manage
from logfile.models import Stock_Phone_Purchase_Log
from user_log.models import User_Log_Info
from mainpage.models import Phone_Brand,Costomer_Manage
# Create your views here.

def costomer_fix_manage(request):
	engineer = request.user.username
	fix_sn_lists = []
	fix_sn_pass_lists = []
	percents = ['100','90','80','70','60','50','40','30','20','10']
	try:
		phone_brand_choice = request.POST['phone_brand_choice']
		status = request.POST['status']
		# customer_info = request.POST['customer_info']
		search_type_list = ['姓名','手機','序號','IMEI']
		reservation = request.POST['reservation']
		start_date_text = reservation.split('/')[2].split(' ')[0] + '/' +reservation.split('/')[0] + '/' + reservation.split('/')[1]
		start_date = datetime.datetime.combine(datetime.datetime.strptime(start_date_text,"%Y/%m/%d") , datetime.time.min)
		end_date_text = reservation.split('/')[4] + '/' + reservation.split('/')[2].split(' ')[2] + '/' + reservation.split('/')[3]
		end_date = datetime.datetime.combine(datetime.datetime.strptime(end_date_text,"%Y/%m/%d") , datetime.time.max)
		print('start_date=',start_date)
		print('end_date=',end_date)
		engineer_none_lists = []
		engineer_pass_lists = []
		if status == 'NO':
			fix_lists = Costomer_Fix_Managment.objects.filter(created_at__range = (start_date,end_date),finish_status = False ,alive=True,engineer_1 = engineer).order_by('-update_at')
		elif status == 'YES':
			fix_lists = Costomer_Fix_Managment.objects.filter(created_at__range = (start_date,end_date),finish_status = True ,alive=True,engineer_1 = engineer).order_by('-update_at')
		elif status == 'ALL':
			fix_lists = Costomer_Fix_Managment.objects.filter(created_at__range = (start_date,end_date),alive=True,engineer_1 = engineer).order_by('-update_at')
		
		if phone_brand_choice == 'none':
			phone_brand_choice_text = '全部'
		else:		
			phone_brand_choice_text = Phone_Brand.objects.get(phone_brand_num=phone_brand_choice,alive=True).phone_brand_name
			print('phone_brand_choice_text=',phone_brand_choice_text)
			fix_lists = fix_lists.filter(phone_name_num = phone_brand_choice_text)
		
		for fix_list in fix_lists:
			if fix_list.engineer_2 == '':
				fix_sn_lists.append(fix_list.costomer_sn)
			else:
				fix_sn_pass_lists.append(fix_list.costomer_sn)

		costomer_manage_lists = Costomer_Manage.objects.filter(costomer_sn__in = fix_sn_lists)
		costomer_manage_pass_lists = Costomer_Manage.objects.filter(costomer_sn__in = fix_sn_pass_lists)
		# costomer_manage_lists_info = 
		print('costomer_manage_lists=',costomer_manage_lists)
		print('ee')
		date_text = (datetime.datetime.today() - datetime.timedelta(days=30)).strftime("%m/%d/%Y")+' - '+datetime.datetime.today().strftime("%m/%d/%Y")
		phone_brand_lists = Phone_Brand.objects.filter(alive=True)
		fix_part_list_text = []
		fix_part_list_pass_text = []
		for costomer_manage_list in costomer_manage_lists:
			temp_text = ''
			temp_fix_text = []
			print('customer_name=',costomer_manage_list.customer_name,'update_at=',costomer_manage_list.update_at)
			fix_part_list = costomer_manage_list.fix_part.replace("'","").replace("[","").replace("]","").replace(' ','').split(',')
			if Costomer_Fix_Managment.objects.get(costomer_sn = costomer_manage_list.costomer_sn ).engineer_2 == '' :
				engineer_none_lists.append(costomer_manage_list.costomer_sn)
			# print('plus_buy_list=',plus_buy_list,'plus_buy_list_price=',plus_buy_list_price,'fix_part_list=',fix_part_list)

		
			for j in range(len(fix_part_list)):
				temp_fix_text.append(str(fix_part_list[j]))
			fix_part_list_text.append(temp_fix_text)

		for costomer_manage_list in costomer_manage_pass_lists:
			temp_text = ''
			temp_fix_text = []
			print('customer_name=',costomer_manage_list.customer_name,'update_at=',costomer_manage_list.update_at)
			fix_part_list = costomer_manage_list.fix_part.replace("'","").replace("[","").replace("]","").replace(' ','').split(',')
			if Costomer_Fix_Managment.objects.get(costomer_sn = costomer_manage_list.costomer_sn ).engineer_2 == '' :
				engineer_pass_lists.append(costomer_manage_list.costomer_sn)
			# print('plus_buy_list=',plus_buy_list,'plus_buy_list_price=',plus_buy_list_price,'fix_part_list=',fix_part_list)

		
			for k in range(len(fix_part_list)):
				temp_fix_text.append(str(fix_part_list[k]))
			fix_part_list_pass_text.append(temp_fix_text)
		
		costomer_manage_pass_info_lists = Costomer_Fix_Managment.objects.filter(costomer_sn__in = fix_sn_pass_lists)



		if status == 'ALL':
			status_text = '全部'
		elif status == 'YES':
			status_text = '已完工'
		elif status == 'NO':
			status_text = '未完工'
		engineer_none_lists_file = Costomer_Fix_Managment.objects.filter(costomer_sn__in = engineer_none_lists)
		print('engineer_none_lists=',engineer_none_lists)
		engineer_none_lists_2 = engineer_none_lists

		costomer_manage_lists_zip = zip(costomer_manage_lists,fix_part_list_text)
		costomer_manage_pass_lists_zip = zip(costomer_manage_pass_lists,fix_part_list_pass_text,costomer_manage_pass_info_lists)
		costomer_manage_pass_lists_2_zip = zip(costomer_manage_pass_lists,fix_part_list_pass_text,costomer_manage_pass_info_lists)
		engineer_none_lists_file_zip = zip(costomer_manage_lists,engineer_none_lists_file,engineer_none_lists,engineer_none_lists_2,fix_part_list_text)
		print('aa')
	except:
		date_text = (datetime.datetime.today() - datetime.timedelta(days=30)).strftime("%m/%d/%Y")+' - '+datetime.datetime.today().strftime("%m/%d/%Y")
		phone_brand_lists = Phone_Brand.objects.filter(alive=True)
		print('bb')
	engineer_list_1  = Engineer_List_Managment.objects.filter(story = 'story_1' , alive = True)
	engineer_list_2  = Engineer_List_Managment.objects.filter(story = 'story_2' ,alive = True)
	response = render(request,'engineer_fix/costomer_fix_manage.html',locals())
	return response

def costomer_fix_manage_post(request):
	engineer_text = 'peter'
	engineer_sn = request.POST['engineer_sn']
	engineer_choice = request.POST['engineer_choice']
	fix_part = request.POST.getlist('fix_part')
	percent_choice = request.POST['percent_choice']
	print('engineer_sn=',engineer_sn,'engineer_choice=',engineer_choice,'fix_part=',fix_part,'percent_choice=',percent_choice)
	fix_element = Costomer_Fix_Managment.objects.filter(costomer_sn = engineer_sn)
	fix_part_list = Costomer_Manage.objects.get(costomer_sn= engineer_sn).fix_part.replace('[','').replace(']','').replace("'","").split(',')
	# print(fix_part_list)
	fix_element.update(engineer_2 = engineer_choice , case_percent_2 = percent_choice ,case_percent_1 = 100 - int(percent_choice),engineer_fix_2 = fix_part ,engineer_fix_1 = list(set(fix_part_list).difference(set(fix_part))))
	response = redirect('/manage/costomer_fix_manage/')
	return response

def engineer_fix_info(request,costomer_sn):
	phone_brand_name_lists = []
	phone_brand_num_lists = []
	plus_buy_price_total = 0
	
	customer_lists = Costomer_Manage.objects.get(costomer_sn=costomer_sn,alive=True)
	phone_name_num_text = Phone_name.objects.get(phone_name=customer_lists.phone_name_num,alive=True).phone_name_num
	phone_brand_num_text = phone_name_num_text[:4]
	print('phone_name_num=',phone_name_num_text,'phone_brand_num=',phone_brand_num_text)
	phone_color_lists = Phone_Color.objects.filter(alive=True)
	# phone_name_lists = Phone_name.objects.filter(phone_name_num__startswith=phone_brand_num_text,alive=True)
	phones_fix = Fix_Part_Manage.objects.filter(alive=True)
	accessories_names = Accessories_Name.objects.filter(alive=True)
	# phone_brand_name = Phone_Brand.objects.get(phone_brand_num=phone_brand_choice,alive=True).phone_brand_name
	phone_brand_name = Phone_Brand.objects.get(phone_brand_num=phone_brand_num_text,alive=True).phone_brand_name
	phone_brand_name_alls = Phone_name.objects.filter(phone_brand_name=phone_brand_name,alive=True)
	phone_num = Phone_name.objects.get(phone_brand_name = customer_lists.phone_brand_num,phone_name = customer_lists.phone_name_num).phone_name_num
	print('phone_num=',phone_num)
	range_list = range(5)
	stock_lists = Stock_Phone_Manage.objects.filter(phone_name_num = phone_num , alive = True)
	for phone_brand_name_all in phone_brand_name_alls:
		phone_brand_name_lists.append(phone_brand_name_all.phone_name)
		phone_brand_num_lists.append(phone_brand_name_all.phone_name_num)
	phone_name_lists = zip(phone_brand_name_lists,phone_brand_num_lists)
	response = render(request,'engineer_fix/engineer_fix_info.html',locals())
	return response	

def engineer_fix_info_post(request):
	log_user = request.user.username
	costomer_sn = request.POST['costomer_sn']
	fix_element = request.POST.getlist('fix_element')
	fix_element_num = request.POST.getlist('fix_element_num')
	fix_element_else = request.POST['fix_element_else']
	log_text = request.POST['log_text']
	phone_name_num = request.POST['phone_name_num']
	part_num = ''
	part_name = ''
	for i in range(len(fix_element_num)):
		if i == (len(fix_element_num)-1):
			if fix_element_num[i] == '0' :
				pass
			else:
				part_num = part_num  + str(fix_element_num[i])
				part_name = part_name  + str(fix_element[i])
		else:
			if fix_element_num[i] == '0' :
				pass
			else:
				part_num = part_num  + str(fix_element_num[i]) + ','
				part_name = part_name  + str(fix_element[i]) + ','

	purchase_num = datetime.datetime.today().strftime("%Y%m%d") + str(phone_name_num) + '000'

	purchase_type = 'fix'
	stock_fix_manu_name = ''
	stock_num_plus = []

	Stock_Phone_Purchase_Log.objects.create(purchase_num=purchase_num,phone_name_num=phone_name_num,log_user=log_user,purchase_type=purchase_type,part_name=part_name,part_num=part_num,stock_fix_manu_num=stock_fix_manu_name,comment='',create_at=datetime.datetime.today())
	for k in range(len(fix_element)):
		stock_phone = Stock_Phone_Manage.objects.get(phone_name_num=phone_name_num)
		if stock_phone.phone_fix_elements_1 == fix_element[k] :
			total_num = Stock_Phone_Manage.objects.get(phone_name_num=phone_name_num,phone_fix_elements_1 = fix_element[k]).phone_fix_elements_num_1
			total_num = int(total_num) - int(fix_element_num[k])
			Stock_Phone_Manage.objects.filter(phone_name_num=phone_name_num,phone_fix_elements_1 = fix_element[k]).update(phone_fix_elements_num_1 = total_num )
		if stock_phone.phone_fix_elements_2 == fix_element[k] :
			total_num = Stock_Phone_Manage.objects.get(phone_name_num=phone_name_num,phone_fix_elements_2 = fix_element[k]).phone_fix_elements_num_2
			total_num = int(total_num) - int(fix_element_num[k])
			Stock_Phone_Manage.objects.filter(phone_name_num=phone_name_num,phone_fix_elements_2 = fix_element[k]).update(phone_fix_elements_num_2 = total_num )
		if stock_phone.phone_fix_elements_3 == fix_element[k] :
			total_num = Stock_Phone_Manage.objects.get(phone_name_num=phone_name_num,phone_fix_elements_3 = fix_element[k]).phone_fix_elements_num_3
			total_num = int(total_num) - int(fix_element_num[k])
			Stock_Phone_Manage.objects.filter(phone_name_num=phone_name_num,phone_fix_elements_3 = fix_element[k]).update(phone_fix_elements_num_3 = total_num )
		if stock_phone.phone_fix_elements_4 == fix_element[k] :
			total_num = Stock_Phone_Manage.objects.get(phone_name_num=phone_name_num,phone_fix_elements_4 = fix_element[k]).phone_fix_elements_num_4
			total_num = int(total_num) - int(fix_element_num[k])
			Stock_Phone_Manage.objects.filter(phone_name_num=phone_name_num,phone_fix_elements_4 = fix_element[k]).update(phone_fix_elements_num_4 = total_num )
		if stock_phone.phone_fix_elements_5 == fix_element[k] :
			total_num = Stock_Phone_Manage.objects.get(phone_name_num=phone_name_num,phone_fix_elements_5 = fix_element[k]).phone_fix_elements_num_5
			total_num = int(total_num) - int(fix_element_num[k])
			Stock_Phone_Manage.objects.filter(phone_name_num=phone_name_num,phone_fix_elements_5 = fix_element[k]).update(phone_fix_elements_num_5 = total_num )
		if stock_phone.phone_fix_elements_6 == fix_element[k] :
			total_num = Stock_Phone_Manage.objects.get(phone_name_num=phone_name_num,phone_fix_elements_6 = fix_element[k]).phone_fix_elements_num_6
			total_num = int(total_num) - int(fix_element_num[k])
			Stock_Phone_Manage.objects.filter(phone_name_num=phone_name_num,phone_fix_elements_6 = fix_element[k]).update(phone_fix_elements_num_6 = total_num )
		if stock_phone.phone_fix_elements_7 == fix_element[k] :
			total_num = Stock_Phone_Manage.objects.get(phone_name_num=phone_name_num,phone_fix_elements_7 = fix_element[k]).phone_fix_elements_num_7
			total_num = int(total_num) - int(fix_element_num[k])
			Stock_Phone_Manage.objects.filter(phone_name_num=phone_name_num,phone_fix_elements_7 = fix_element[k]).update(phone_fix_elements_num_7 = total_num )
		if stock_phone.phone_fix_elements_8 == fix_element[k] :
			total_num = Stock_Phone_Manage.objects.get(phone_name_num=phone_name_num,phone_fix_elements_8 = fix_element[k]).phone_fix_elements_num_8
			total_num = int(total_num) - int(fix_element_num[k])
			Stock_Phone_Manage.objects.filter(phone_name_num=phone_name_num,phone_fix_elements_8 = fix_element[k]).update(phone_fix_elements_num_8 = total_num )
		if stock_phone.phone_fix_elements_9 == fix_element[k] :
			total_num = Stock_Phone_Manage.objects.get(phone_name_num=phone_name_num,phone_fix_elements_9 = fix_element[k]).phone_fix_elements_num_9
			total_num = int(total_num) - int(fix_element_num[k])
			Stock_Phone_Manage.objects.filter(phone_name_num=phone_name_num,phone_fix_elements_9 = fix_element[k]).update(phone_fix_elements_num_9 = total_num )
		if stock_phone.phone_fix_elements_10 == fix_element[k] :
			total_num = Stock_Phone_Manage.objects.get(phone_name_num=phone_name_num,phone_fix_elements_10 = fix_element[k]).phone_fix_elements_num_10
			total_num = int(total_num) - int(fix_element_num[k])
			Stock_Phone_Manage.objects.filter(phone_name_num=phone_name_num,phone_fix_elements_10 = fix_element[k]).update(phone_fix_elements_num_10 = total_num )
		if stock_phone.phone_fix_elements_11 == fix_element[k] :
			total_num = Stock_Phone_Manage.objects.get(phone_name_num=phone_name_num,phone_fix_elements_11 = fix_element[k]).phone_fix_elements_num_11
			total_num = int(total_num) - int(fix_element_num[k])
			Stock_Phone_Manage.objects.filter(phone_name_num=phone_name_num,phone_fix_elements_11 = fix_element[k]).update(phone_fix_elements_num_11 = total_num )
		if stock_phone.phone_fix_elements_12 == fix_element[k] :
			total_num = Stock_Phone_Manage.objects.get(phone_name_num=phone_name_num,phone_fix_elements_12 = fix_element[k]).phone_fix_elements_num_12
			total_num = int(total_num) - int(fix_element_num[k])
			Stock_Phone_Manage.objects.filter(phone_name_num=phone_name_num,phone_fix_elements_12 = fix_element[k]).update(phone_fix_elements_num_12 = total_num )
		if stock_phone.phone_fix_elements_13 == fix_element[k] :
			total_num = Stock_Phone_Manage.objects.get(phone_name_num=phone_name_num,phone_fix_elements_13 = fix_element[k]).phone_fix_elements_num_13
			total_num = int(total_num) - int(fix_element_num[k])
			Stock_Phone_Manage.objects.filter(phone_name_num=phone_name_num,phone_fix_elements_13 = fix_element[k]).update(phone_fix_elements_num_13 = total_num )
		if stock_phone.phone_fix_elements_14 == fix_element[k] :
			total_num = Stock_Phone_Manage.objects.get(phone_name_num=phone_name_num,phone_fix_elements_14 = fix_element[k]).phone_fix_elements_num_14
			total_num = int(total_num) - int(fix_element_num[k])
			Stock_Phone_Manage.objects.filter(phone_name_num=phone_name_num,phone_fix_elements_14 = fix_element[k]).update(phone_fix_elements_num_14 = total_num )
		if stock_phone.phone_fix_elements_15 == fix_element[k] :
			total_num = Stock_Phone_Manage.objects.get(phone_name_num=phone_name_num,phone_fix_elements_15 = fix_element[k]).phone_fix_elements_num_15
			total_num = int(total_num) - int(fix_element_num[k])
			Stock_Phone_Manage.objects.filter(phone_name_num=phone_name_num,phone_fix_elements_15 = fix_element[k]).update(phone_fix_elements_num_15 = total_num )
		if stock_phone.phone_fix_elements_16 == fix_element[k] :
			total_num = Stock_Phone_Manage.objects.get(phone_name_num=phone_name_num,phone_fix_elements_16 = fix_element[k]).phone_fix_elements_num_16
			total_num = int(total_num) - int(fix_element_num[k])
			Stock_Phone_Manage.objects.filter(phone_name_num=phone_name_num,phone_fix_elements_16 = fix_element[k]).update(phone_fix_elements_num_16 = total_num )
		if stock_phone.phone_fix_elements_17 == fix_element[k] :
			total_num = Stock_Phone_Manage.objects.get(phone_name_num=phone_name_num,phone_fix_elements_17 = fix_element[k]).phone_fix_elements_num_17
			total_num = int(total_num) - int(fix_element_num[k])
			Stock_Phone_Manage.objects.filter(phone_name_num=phone_name_num,phone_fix_elements_17 = fix_element[k]).update(phone_fix_elements_num_17 = total_num )
		if stock_phone.phone_fix_elements_18 == fix_element[k] :
			total_num = Stock_Phone_Manage.objects.get(phone_name_num=phone_name_num,phone_fix_elements_18 = fix_element[k]).phone_fix_elements_num_18
			total_num = int(total_num) - int(fix_element_num[k])
			Stock_Phone_Manage.objects.filter(phone_name_num=phone_name_num,phone_fix_elements_18 = fix_element[k]).update(phone_fix_elements_num_18 = total_num )
		if stock_phone.phone_fix_elements_19 == fix_element[k] :
			total_num = Stock_Phone_Manage.objects.get(phone_name_num=phone_name_num,phone_fix_elements_19 = fix_element[k]).phone_fix_elements_num_19
			total_num = int(total_num) - int(fix_element_num[k])
			Stock_Phone_Manage.objects.filter(phone_name_num=phone_name_num,phone_fix_elements_19 = fix_element[k]).update(phone_fix_elements_num_19 = total_num )
		if stock_phone.phone_fix_elements_20 == fix_element[k] :
			total_num = Stock_Phone_Manage.objects.get(phone_name_num=phone_name_num,phone_fix_elements_20 = fix_element[k]).phone_fix_elements_num_20
			total_num = int(total_num) - int(fix_element_num[k])
			Stock_Phone_Manage.objects.filter(phone_name_num=phone_name_num,phone_fix_elements_20 = fix_element[k]).update(phone_fix_elements_num_20 = total_num )

	print('costomer_sn=',costomer_sn,'fix_element=',fix_element,'fix_element_num',fix_element_num)
	fix_element_text = Costomer_Fix_Managment.objects.filter(costomer_sn = costomer_sn)
	print('part_name=',part_name,'part_num=',part_num)
	Costomer_Fix_Managment.objects.filter(costomer_sn = costomer_sn,alive = True).update(stock_part_name = part_name,stock_part_num = part_num,finishd_at = datetime.datetime.today(),finish_status = True)
	Costomer_Manage.objects.filter(costomer_sn = costomer_sn,alive= True).update(finish_status = True,update_at =datetime.datetime.today())
	log_text_total = '=====完成維修===== 維修說明: ' + log_text
	User_Log_Info.objects.create(costomer_sn = costomer_sn,type_log = 'system' , sign_user = log_user , log_text = log_text_total ,created_at = datetime.datetime.today())

	# fix_part_list = Costomer_Manage.objects.get(costomer_sn= engineer_sn).fix_part.replace('[','').replace(']','').replace("'","").split(',')
	# print(fix_part_list)
	# fix_element.update(engineer_2 = engineer_choice , case_percent_2 = percent_choice ,case_percent_1 = 100 - int(percent_choice),engineer_fix_2 = fix_part ,engineer_fix_1 = list(set(fix_part_list).difference(set(fix_part))))
	response = redirect('/customer_form_info/'+costomer_sn)
	return response	
	
	
	# stock_manage_num = Stock_Phone_Manage.objects.filter(phone_name_num=phone_name_num,alive=True)
	# print('stock_manage_num=',stock_manage_num)
	# stock_manage_num_lists.append(stock_manage_num[0].phone_fix_elements_num_1)
	# stock_manage_num_lists.append(stock_manage_num[0].phone_fix_elements_num_2)
	# stock_manage_num_lists.append(stock_manage_num[0].phone_fix_elements_num_3)
	# stock_manage_num_lists.append(stock_manage_num[0].phone_fix_elements_num_4)
	# stock_manage_num_lists.append(stock_manage_num[0].phone_fix_elements_num_5)
	# stock_manage_num_lists.append(stock_manage_num[0].phone_fix_elements_num_6)
	# stock_manage_num_lists.append(stock_manage_num[0].phone_fix_elements_num_7)
	# stock_manage_num_lists.append(stock_manage_num[0].phone_fix_elements_num_8)
	# stock_manage_num_lists.append(stock_manage_num[0].phone_fix_elements_num_9)
	# stock_manage_num_lists.append(stock_manage_num[0].phone_fix_elements_num_10)
	# stock_manage_num_lists.append(stock_manage_num[0].phone_fix_elements_num_11)
	# stock_manage_num_lists.append(stock_manage_num[0].phone_fix_elements_num_12)
	# stock_manage_num_lists.append(stock_manage_num[0].phone_fix_elements_num_13)
	# stock_manage_num_lists.append(stock_manage_num[0].phone_fix_elements_num_14)
	# stock_manage_num_lists.append(stock_manage_num[0].phone_fix_elements_num_15)
	# stock_manage_num_lists.append(stock_manage_num[0].phone_fix_elements_num_16)
	# stock_manage_num_lists.append(stock_manage_num[0].phone_fix_elements_num_17)
	# stock_manage_num_lists.append(stock_manage_num[0].phone_fix_elements_num_18)
	# stock_manage_num_lists.append(stock_manage_num[0].phone_fix_elements_num_19)
	# stock_manage_num_lists.append(stock_manage_num[0].phone_fix_elements_num_20)

	# if purchase_type == 'add':
	# 	for i in range(len(part_num_lists)):
	# 		print('i=',i,'原:',int(stock_manage_num_lists[i]),'加總後:',int(part_num_lists[i]))
	# 		stock_num_plus.append(int(stock_manage_num_lists[i]) + int(part_num_lists[i]))
	# 		print(stock_num_plus)
	# elif purchase_type == 'ng':
	# 	for j in range(len(part_num_lists)):
	# 		print('j=',j,'原:',int(stock_manage_num_lists[j]),'相減後:',int(part_num_lists[j]))
	# 		stock_num_plus.append(int(stock_manage_num_lists[j]) - int(part_num_lists[j]))
	# 		print(stock_num_plus)
	# 	Stock_Phone_Purchase_Ng.objects.create(purchase_num=purchase_num,phone_name_num=phone_name_num,log_user=log_user,purchase_type=purchase_type,part_name=part_name,part_num=part_num,stock_fix_manu_num=stock_fix_manu_name,comment=comment,finish_comment='',update_at=datetime.datetime.today(),create_at=datetime.datetime.today())
	# print('stock_num_plus=',stock_num_plus)
	# try:
	# 	Stock_Phone_Manage.objects.filter(phone_name_num=phone_name_num,alive=True).update(phone_fix_elements_num_1=stock_num_plus[0])
	# except:
	# 	pass
	# try:
	# 	Stock_Phone_Manage.objects.filter(phone_name_num=phone_name_num,alive=True).update(phone_fix_elements_num_2=stock_num_plus[1])
	# except:
	# 	pass
	# try:
	# 	Stock_Phone_Manage.objects.filter(phone_name_num=phone_name_num,alive=True).update(phone_fix_elements_num_3=stock_num_plus[2])
	# except:
	# 	pass
	# try:
	# 	Stock_Phone_Manage.objects.filter(phone_name_num=phone_name_num,alive=True).update(phone_fix_elements_num_4=stock_num_plus[3])
	# except:
	# 	pass
	# try:
	# 	Stock_Phone_Manage.objects.filter(phone_name_num=phone_name_num,alive=True).update(phone_fix_elements_num_5=stock_num_plus[4])
	# except:
	# 	pass
	# try:
	# 	Stock_Phone_Manage.objects.filter(phone_name_num=phone_name_num,alive=True).update(phone_fix_elements_num_6=stock_num_plus[5])
	# except:
	# 	pass
	# try:
	# 	Stock_Phone_Manage.objects.filter(phone_name_num=phone_name_num,alive=True).update(phone_fix_elements_num_7=stock_num_plus[6])
	# except:
	# 	pass
	# try:
	# 	Stock_Phone_Manage.objects.filter(phone_name_num=phone_name_num,alive=True).update(phone_fix_elements_num_8=stock_num_plus[7])
	# except:
	# 	pass
	# try:
	# 	Stock_Phone_Manage.objects.filter(phone_name_num=phone_name_num,alive=True).update(phone_fix_elements_num_9=stock_num_plus[8])
	# except:
	# 	pass
	# try:
	# 	Stock_Phone_Manage.objects.filter(phone_name_num=phone_name_num,alive=True).update(phone_fix_elements_num_10=stock_num_plus[9])
	# except:
	# 	pass
	# try:
	# 	Stock_Phone_Manage.objects.filter(phone_name_num=phone_name_num,alive=True).update(phone_fix_elements_num_11=stock_num_plus[10])
	# except:
	# 	pass
	# try:
	# 	Stock_Phone_Manage.objects.filter(phone_name_num=phone_name_num,alive=True).update(phone_fix_elements_num_12=stock_num_plus[11])
	# except:
	# 	pass
	# try:
	# 	Stock_Phone_Manage.objects.filter(phone_name_num=phone_name_num,alive=True).update(phone_fix_elements_num_13=stock_num_plus[12])
	# except:
	# 	pass
	# try:
	# 	Stock_Phone_Manage.objects.filter(phone_name_num=phone_name_num,alive=True).update(phone_fix_elements_num_14=stock_num_plus[13])
	# except:
	# 	pass
	# try:
	# 	Stock_Phone_Manage.objects.filter(phone_name_num=phone_name_num,alive=True).update(phone_fix_elements_num_15=stock_num_plus[14])
	# except:
	# 	pass
	# try:
	# 	Stock_Phone_Manage.objects.filter(phone_name_num=phone_name_num,alive=True).update(phone_fix_elements_num_16=stock_num_plus[15])
	# except:
	# 	pass
	# try:
	# 	Stock_Phone_Manage.objects.filter(phone_name_num=phone_name_num,alive=True).update(phone_fix_elements_num_17=stock_num_plus[16])
	# except:
	# 	pass
	# try:
	# 	Stock_Phone_Manage.objects.filter(phone_name_num=phone_name_num,alive=True).update(phone_fix_elements_num_18=stock_num_plus[17])
	# except:
	# 	pass
	# try:
	# 	Stock_Phone_Manage.objects.filter(phone_name_num=phone_name_num,alive=True).update(phone_fix_elements_num_19=stock_num_plus[18])
	# except:
	# 	pass
	# try:
	# 	Stock_Phone_Manage.objects.filter(phone_name_num=phone_name_num,alive=True).update(phone_fix_elements_num_20=stock_num_plus[19])
	# except:
	# 	pass
	# try:
	# 	Stock_Phone_Manage.objects.filter(phone_name_num=phone_name_num,alive=True).update(phone_fix_elements_num_2=stock_num_plus[20])
	# except:
	# 	pass
	# # if stock_num_plus[2]:
	# 	# Stock_Phone_Manage.objects.filter(phone_name_num=phone_name_num,alive=True).update(phone_fix_elements_num_3=stock_num_plus[2])
	# 	# Stock_Phone_Amount_Manage.objects.filter(phone_name_num=phone_name_num).update()
	# print(stock_num_plus)
	# response = redirect('/stock/manage_purchase/')
	# return response

