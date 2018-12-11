from django.contrib import admin
from mainpage.models import Phone_Brand,Phone_name
# Register your models here.
class Phone_BrandAdmin(admin.ModelAdmin):
	list_display = ('id','phone_brand_num','phone_brand_name','alive')
admin.site.register(Phone_Brand,Phone_BrandAdmin)

class Phone_nameAdmin(admin.ModelAdmin):
	list_display = ('id','phone_name_num','phone_brand_name','phone_name','phone_color','alive','created_at')
admin.site.register(Phone_name,Phone_nameAdmin)