from django.db import models
from django.utils import timezone

# Create your models here.

class Stock_Phone_Parts(models.Model):
	phone_fix_parts_1 = models.CharField(max_length=10)
	phone_fix_parts_num_1 = models.IntegerField(default='')
	phone_fix_parts_2 = models.CharField(max_length=10)
	phone_fix_parts_num_2 = models.IntegerField(default='')
	phone_fix_parts_3 = models.CharField(max_length=10)
	phone_fix_parts_num_3 = models.IntegerField(default='')
	phone_fix_parts_4 = models.CharField(max_length=10)
	phone_fix_parts_num_4 = models.IntegerField(default='')
	phone_fix_parts_5 = models.CharField(max_length=10)
	phone_fix_parts_num_5 = models.IntegerField(default='')
	phone_fix_parts_6 = models.CharField(max_length=10)
	phone_fix_parts_num_6 = models.IntegerField(default='')
	phone_fix_parts_7 = models.CharField(max_length=10)
	phone_fix_parts_num_7 = models.IntegerField(default='')
	phone_fix_parts_8 = models.CharField(max_length=10)
	phone_fix_parts_num_8 = models.IntegerField(default='')
	phone_fix_parts_9 = models.CharField(max_length=10)
	phone_fix_parts_num_9 = models.IntegerField(default='')
	phone_fix_parts_10 = models.CharField(max_length=10)
	phone_fix_parts_num_10 = models.IntegerField(default='')
	phone_fix_parts_11 = models.CharField(max_length=10)
	phone_fix_parts_num_11 = models.IntegerField(default='')
	phone_fix_parts_12 = models.CharField(max_length=10)
	phone_fix_parts_num_12 = models.IntegerField(default='')
	phone_fix_parts_13 = models.CharField(max_length=10)
	phone_fix_parts_num_13 = models.IntegerField(default='')
	phone_fix_parts_14 = models.CharField(max_length=10)
	phone_fix_parts_num_14 = models.IntegerField(default='')
	phone_fix_parts_15 = models.CharField(max_length=10)
	phone_fix_parts_num_15 = models.IntegerField(default='')
	phone_fix_parts_16 = models.CharField(max_length=10)
	phone_fix_parts_num_16 = models.IntegerField(default='')
	phone_fix_parts_17 = models.CharField(max_length=10)
	phone_fix_parts_num_17 = models.IntegerField(default='')
	phone_fix_parts_18 = models.CharField(max_length=10)
	phone_fix_parts_num_18 = models.IntegerField(default='')
	phone_fix_parts_19 = models.CharField(max_length=10)
	phone_fix_parts_num_19 = models.IntegerField(default='')
	phone_fix_parts_20 = models.CharField(max_length=10)
	phone_fix_parts_num_20 = models.IntegerField(default='')	
	update_at = models.DateTimeField(default=timezone.now)

class Stock_Phone_Fix_Parts(models.Model):
	phone_fix_parts = models.CharField(max_length=20,default='')
	phone_fix_parts_num = models.IntegerField(default=0)
	phone_fix_parts_round = models.IntegerField(default=0)
	create_at = models.DateTimeField(default=timezone.now)

class Stock_Phone_Manage(models.Model):
	phone_name_num = models.CharField(max_length=10)
	phone_fix_elements_1 = models.CharField(max_length=10,default='none')
	phone_fix_elements_num_1 = models.IntegerField(default=0)
	phone_fix_elements_2 = models.CharField(max_length=10,default='none')
	phone_fix_elements_num_2 = models.IntegerField(default=0)
	phone_fix_elements_3 = models.CharField(max_length=10,default='none')
	phone_fix_elements_num_3 = models.IntegerField(default=0)
	phone_fix_elements_4 = models.CharField(max_length=10,default='none')
	phone_fix_elements_num_4 = models.IntegerField(default=0)
	phone_fix_elements_5 = models.CharField(max_length=10,default='none')
	phone_fix_elements_num_5 = models.IntegerField(default=0)
	phone_fix_elements_6 = models.CharField(max_length=10,default='none')
	phone_fix_elements_num_6 = models.IntegerField(default=0)
	phone_fix_elements_7 = models.CharField(max_length=10,default='none')
	phone_fix_elements_num_7 = models.IntegerField(default=0)
	phone_fix_elements_8 = models.CharField(max_length=10,default='none')
	phone_fix_elements_num_8 = models.IntegerField(default=0)
	phone_fix_elements_9 = models.CharField(max_length=10,default='none')
	phone_fix_elements_num_9 = models.IntegerField(default=0)
	phone_fix_elements_10 = models.CharField(max_length=10,default='none')
	phone_fix_elements_num_10 = models.IntegerField(default=0)
	phone_fix_elements_11 = models.CharField(max_length=10,default='none')
	phone_fix_elements_num_11 = models.IntegerField(default=0)
	phone_fix_elements_12 = models.CharField(max_length=10,default='none')
	phone_fix_elements_num_12 = models.IntegerField(default=0)
	phone_fix_elements_13 = models.CharField(max_length=10,default='none')
	phone_fix_elements_num_13 = models.IntegerField(default=0)
	phone_fix_elements_14 = models.CharField(max_length=10,default='none')
	phone_fix_elements_num_14 = models.IntegerField(default=0)
	phone_fix_elements_15 = models.CharField(max_length=10,default='none')
	phone_fix_elements_num_15 = models.IntegerField(default=0)
	phone_fix_elements_16 = models.CharField(max_length=10,default='none')
	phone_fix_elements_num_16 = models.IntegerField(default=0)
	phone_fix_elements_17 = models.CharField(max_length=10,default='none')
	phone_fix_elements_num_17 = models.IntegerField(default=0)
	phone_fix_elements_18 = models.CharField(max_length=10,default='none')
	phone_fix_elements_num_18 = models.IntegerField(default=0)
	phone_fix_elements_19 = models.CharField(max_length=10,default='none')
	phone_fix_elements_num_19 = models.IntegerField(default=0)
	phone_fix_elements_20 = models.CharField(max_length=10,default='none')
	phone_fix_elements_num_20 = models.IntegerField(default=0)
	phone_story = models.CharField(max_length=10)
	alive = models.BooleanField(default=True)
	update_at = models.DateTimeField(default=timezone.now)



class Stock_Phone_Amount(models.Model):
	phone_name_num = models.CharField(max_length=10)
	phone_fix_elements_num = models.CharField(max_length=100)
	phone_story = models.CharField(max_length=10)
	alive = models.BooleanField(default=True)
	update_at = models.DateTimeField(default=timezone.now)
	create_at = models.DateTimeField(default=timezone.now)

class Stock_Fix_Manu(models.Model):
	stock_fix_manu_num = models.CharField(max_length=10)
	stock_fix_manu_name = models.CharField(max_length=30)
	stock_fix_manu_phone = models.CharField(max_length=10)
	stock_fix_manu_note = models.CharField(max_length=50)
	alive = models.BooleanField(default=True)
	create_at = models.DateTimeField(default=timezone.now)

class Stock_Phone_Purchase_Ng(models.Model):
	purchase_num = models.CharField(max_length=20)
	phone_name_num = models.CharField(max_length=10)
	log_user =  models.CharField(max_length=15)
	purchase_type = models.CharField(max_length=10)
	part_name = models.CharField(max_length=200)
	part_num = models.CharField(max_length=100)
	stock_fix_manu_num = models.CharField(max_length=10)
	comment = models.CharField(max_length=300)
	finish_comment = models.CharField(max_length=300)
	alive = models.BooleanField(default=True)
	update_at = models.DateTimeField(default=timezone.now)
	create_at = models.DateTimeField(default=timezone.now)