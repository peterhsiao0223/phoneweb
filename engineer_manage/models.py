from django.db import models
from django.utils import timezone
# Create your models here.

class Costomer_Fix_Managment(models.Model):
	costomer_sn = models.CharField(max_length=20)
	story = models.CharField(max_length=10)
	phone_name_num = models.CharField(max_length=10)
	customer_receive = models.BooleanField(default=False)
	case_percent_1 = models.CharField(max_length=3)
	engineer_1 = models.CharField(max_length=10,default='')
	engineer_fix_1 = models.CharField(max_length=50)
	case_percent_2 = models.CharField(max_length=3)
	engineer_2 = models.CharField(max_length=10,default='')
	engineer_fix_2 = models.CharField(max_length=50,default='')
	stock_part_name = models.CharField(max_length=50,default='')
	stock_part_num = models.CharField(max_length=20,default='')
	created_at = models.DateTimeField(default=timezone.now)
	update_at = models.DateTimeField()
	finish_status = models.BooleanField(default=False)
	finishd_at = models.DateTimeField()
	alive = models.BooleanField(default=True)

# class Engineer_List_(models.Model):
# 	engineer_num = models.CharField(max_length=10)
# 	engineer_name = models.CharField(max_length=10)
# 	story = models.CharField(max_length=10)
# 	created_at = models.DateTimeField()
# 	update_at = models.DateTimeField()
# 	alive = models.BooleanField(default=True)

# class Story_List(models.Model):
# 	story_num = models.CharField(max_length=10)
# 	story = models.CharField(max_length=10)
# 	created_at = models.DateTimeField()
# 	update_at = models.DateTimeField()
# 	alive = models.BooleanField(default=True)

class Engineer_List_Managment(models.Model):
	engineer_num = models.CharField(max_length=10)
	engineer_name = models.CharField(max_length=10)
	story = models.CharField(max_length=10)
	created_at = models.DateTimeField(default=timezone.now)
	update_at = models.DateTimeField(default=timezone.now)
	alive = models.BooleanField(default=True)

class Story_List_Managment(models.Model):
	story_num = models.CharField(max_length=10)
	story = models.CharField(max_length=10)
	created_at = models.DateTimeField(default=timezone.now)
	update_at = models.DateTimeField(default=timezone.now)
	alive = models.BooleanField(default=True)