from django.db import models
from django.utils import timezone

# Create your models here.

class Phone_Brand(models.Model):
	phone_brand_num = models.CharField(max_length=4)
	phone_brand_name = models.CharField(max_length=30)
	alive = models.BooleanField()

class Phone_name(models.Model):
	phone_name_num = models.CharField(max_length=10)
	phone_brand_name = models.CharField(max_length=30)
	phone_name = models.CharField(max_length=50)
	phone_color = models.CharField(max_length=50)
	stock = models.BooleanField()
	alive = models.BooleanField()
	update_at = models.DateTimeField(default=timezone.now)
	created_at = models.DateTimeField(default=timezone.now)

class Accessories_Name(models.Model):
	accessories_name = models.CharField(max_length=10)
	accessories_num = models.CharField(max_length=10)
	accessories_price = models.IntegerField()
	accessories_cost = models.IntegerField()
	accessories_note = models.CharField(max_length=50)
	alive = models.BooleanField(default=True)
	update_at = models.DateTimeField(default=timezone.now)
	created_at = models.DateTimeField(default=timezone.now)

class Fix_Part_Manage(models.Model):
	fix_part_name = models.CharField(max_length=10)
	fix_part_num = models.CharField(max_length=10)
	fix_part_note = models.CharField(max_length=50)
	alive = models.BooleanField(default=True)
	created_at = models.DateTimeField(default=timezone.now)

class Phone_Color(models.Model):
	phone_color_name = models.CharField(max_length=10)
	phone_color_num = models.CharField(max_length=10)
	phone_color_note = models.CharField(max_length=50)
	alive = models.BooleanField(default=True)
	created_at = models.DateTimeField(default=timezone.now)

class Stock_Phone_Amount_Manage(models.Model):
	phone_name_num = models.CharField(max_length=10)
	phone_fix_elements_num = models.CharField(max_length=100)
	phone_story = models.CharField(max_length=10)
	alive = models.BooleanField(default=True)
	update_at = models.DateTimeField(default=timezone.now)
	create_at = models.DateTimeField(default=timezone.now)

class Costomer_Manage(models.Model):
	costomer_sn = models.CharField(max_length=20)
	customer_name = models.CharField(max_length=10)
	customer_phone_num = models.CharField(max_length=15)
	phone_brand_num = models.CharField(max_length=30)
	phone_name_num = models.CharField(max_length=30)
	gender = models.BooleanField()
	phone_color = models.CharField(max_length=10)
	fix_part = models.CharField(max_length=50)
	phone_pw = models.CharField(max_length=10)
	total_price = models.IntegerField()
	deposit = models.IntegerField()
	plus_buy = models.CharField(max_length=50)
	plus_buy_price = models.CharField(max_length=50)
	sells = models.CharField(max_length=10)
	engineer = models.CharField(max_length=10,default='')
	finish_status = models.BooleanField(default=False)
	fix_part_sn_num = models.CharField(max_length=20,default='')
	bg_note = models.TextField()
	story = models.CharField(max_length=10)
	field_1 = models.CharField(max_length=20,default='')
	field_2 = models.CharField(max_length=20,default='')
	customer_receive = models.BooleanField(default=False)
	alive = models.BooleanField(default=True)
	update_at = models.DateTimeField(default=timezone.now)
	receive_at = models.DateTimeField(default=timezone.now)
	created_at = models.DateTimeField(default=timezone.now)