from django.db import models
from django.utils import timezone
# Create your models here.

class User_Log_Info(models.Model):
	costomer_sn = models.CharField(max_length=20)
	type_log = models.CharField(max_length=10)
	sign_user = models.CharField(max_length=10)
	log_text = models.TextField()
	field_1 = models.CharField(default = '', max_length=10)
	field_2 = models.CharField(default = '', max_length=10)
	created_at = models.DateTimeField(default=timezone.now)