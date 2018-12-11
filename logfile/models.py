from django.db import models
from django.utils import timezone
# Create your models here.

class Stock_Phone_Purchase_Log(models.Model):
	purchase_num = models.CharField(max_length=20)
	phone_name_num = models.CharField(max_length=10)
	log_user =  models.CharField(max_length=15)
	purchase_type = models.CharField(max_length=10)
	part_name = models.CharField(max_length=200)
	part_num = models.CharField(max_length=100)
	stock_fix_manu_num = models.CharField(max_length=10)
	comment = models.CharField(max_length=300)
	create_at = models.DateTimeField(default=timezone.now)

class Stock_Phone_Purchase_Records(models.Model):
	purchase_num = models.CharField(max_length=50)
	log_user =  models.CharField(max_length=15)
	create_at = models.DateTimeField(default=timezone.now)