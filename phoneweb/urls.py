"""phoneweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from mainpage.views import get_index,customer_form,customer_table,phone_brand,phone_brand_create,phone_name,phone_name_create,phone_name_edit,phone_name_edit_post,accessories_name,accessories_name_post,fix_part_manage,fix_part_manage_post,phone_color_manage,phone_color_manage_post,customer_review,customer_create_post,customer_form_edit,customer_table_engineer_post,customer_form_info,customer_form_notice,customer_form_recive,fix_part_del_post,accessories_name_del_post,phone_color_del_post,phone_name_del_post
from stock.views import demo,stock_manage,stock_manage_brand_search,get_phone_name_api,stock_manage_init,stock_manage_brand_purchase,stock_purchase,stock_purchase_post,stock_name_manage,stock_name_manage_edit,stock_name_manage_edit_post,stock_fix_manu,stock_fix_manu_post,stock_phone_purchase_logfile,stock_manage_ng_ship,stock_ng_ship,stock_phone_manage_ship,stock_phone_manage_ship_post,stock_phone_ship_info,stock_name_manage_order,stock_name_manage_order_post,stock_phone_ship_form,stock_phone_ship_form_post,stock_manage_ship,stock_ship,stock_fix_manu_del_post
from engineer_manage.views import costomer_fix_manage,costomer_fix_manage_post,engineer_fix_info,engineer_fix_info_post
from user_log.views import customer_form_info_post
from managment_page.views import post_login,post_logout,user_manage,user_add,user_add_post,user_profile,change_user_pw,stock_price_manage,stock_price_manage_edit,stock_price_manage_edit_post
from django.contrib.auth.views import login,logout

urlpatterns = [
    url(r'^accounts/login/$', login),
    url(r'^accounts/logout/$', logout),
    url(r'^login/post$', post_login),
    url(r'^logout/post$', post_logout),
    url(r'^manage/user_manage/$', user_manage),
    url(r'^manage/user_add/$', user_add),
    url(r'^manage/user_add/post$', user_add_post),
    url(r'^manage/profile$', user_profile),
    url(r'^manage/pw_rest/(\S+)$', change_user_pw),
	url(r'^$', get_index),
    url(r'^demo/$', demo),
	url(r'^customer_form/$', customer_form),
    url(r'^customer_form_edit/(\S+)$', customer_form_edit),
    url(r'^customer_form_info/(\S+)$', customer_form_info),
    url(r'^post/customer_form_notice/$', customer_form_notice),
    url(r'^post/customer_form_recive/$', customer_form_recive),
    url(r'^post/customer_info/$', customer_form_info_post),
    url(r'^customer_table/$', customer_table),
    url(r'^manage/phone_brand/$', phone_brand),
    url(r'^manage/phone_name/(\S+)$', phone_name),
    url(r'^manage/stock_phone_purchase_logfile/$',stock_phone_purchase_logfile),
    url(r'^manage/phone_name_edit/(\S+)/(\S+)$', phone_name_edit),
    url(r'^post/manage/phone_name_edit/(\S+)/(\S+)$', phone_name_edit_post),
    url(r'^post/manage/phone_name_del/(\S+)/(\S+)$', phone_name_del_post),

    # url(r'^manage/phone_phone/$', phone_name_edit_post),    
    url(r'^manage/accessories_name/$', accessories_name),
    url(r'^post/manage/accessories_name/$', accessories_name_post),
    url(r'^post/manage/accessories_name_del/(\S+)$', accessories_name_del_post),    
    url(r'^manage/fix_part_manage/$', fix_part_manage),
    url(r'^post/manage/fix_part_manage/$', fix_part_manage_post),
    url(r'^post/manage/fix_part_del/(\S+)$', fix_part_del_post),
    url(r'^manage/phone_color_manage/$', phone_color_manage),
    url(r'^post/manage/phone_color_manage/$', phone_color_manage_post),
    url(r'^post/manage/phone_color_del/(\S+)$', phone_color_del_post),
    url(r'^manage/stock_manage/$', stock_name_manage),
    url(r'^manage/stock_price_manage/$', stock_price_manage),
    url(r'^manage/stock_manage_edit/(\S+)$', stock_name_manage_edit),
    url(r'^manage/stock_price_manage_edit/(\S+)$', stock_price_manage_edit),
    url(r'^post/manage/stock_price_manage_edit/(\S+)$', stock_price_manage_edit_post),
    url(r'^post/manage/stock_name_manage_edit/(\S+)$', stock_name_manage_edit_post),
    url(r'^manage/stock_name_manage_order/(\S+)$',stock_name_manage_order),
    url(r'^post/manage/stock_name_manage_order/(\S+)$',stock_name_manage_order_post),
    url(r'^manage/stock_fix_manu/$', stock_fix_manu),
    url(r'^post/manage/stock_fix_manu/$', stock_fix_manu_post),
    url(r'^post/manage/stock_fix_manu_del/(\S+)$', stock_fix_manu_del_post),
    url(r'^post/customer_review/$', customer_review),    
    url(r'^post/phone_name_create/(\S+)$', phone_name_create),
    url(r'^post/phone_brand_create/$', phone_brand_create),
    url(r'^post/stock_purchase/(\S+)$', stock_purchase_post),
    # url(r'^post/stock_ship/(\S+)$', stock_ship_post),
    url(r'^stock/stock_manage_init/(\S+)$', stock_manage_init),
    url(r'^post/customer_create/$',customer_create_post),
    # url(r'^stock/manage/$', stock_purchase_post),
    url(r'^post/customer_table_engineer/(\S+)$',customer_table_engineer_post),
    url(r'^stock/manage/(\S+)$', stock_manage),
    url(r'^stock/manage_purchase/(\S+)$', stock_purchase),
    url(r'^stock/manage_brand/$', stock_manage_brand_search),
    url(r'^stock/manage_purchase/$',stock_manage_brand_purchase),
    url(r'^stock/manage_ng_ship/$',stock_manage_ng_ship),
    url(r'^stock/manage_ship/$',stock_manage_ship),
    url(r'^manage/stock_phone_ship/$',stock_phone_manage_ship),
    url(r'^manage/stock_phone_ship_form/$',stock_phone_ship_form),
    url(r'^post/manage/stock_phone_ship_form/$',stock_phone_ship_form_post),
    url(r'^manage/costomer_fix_manage/$',costomer_fix_manage),
    url(r'^post/costomer_fix_manage/$',costomer_fix_manage_post),
    url(r'^manage/engineer_fix_info/(\S+)$',engineer_fix_info),
    url(r'^post/engineer_fix_info/$',engineer_fix_info_post),
    url(r'^stock/manage_ng_ship/(\S+)$', stock_ng_ship),
    url(r'^stock/manage_ship/(\S+)$', stock_ship),
    url(r'^post/manage/stock_phone_ship/(\S+)$',stock_phone_manage_ship_post),
    url(r'^info/stock_phone_ship_info/(\S+)$',stock_phone_ship_info),
    url(r'^admin/', admin.site.urls),
    url(r'^get_phone_name_api/$', get_phone_name_api),
]