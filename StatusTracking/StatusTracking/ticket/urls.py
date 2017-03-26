from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'pages/login/$', views.login,name='login'),
    url(r'pages/logout/$', views.logout,name='logout'),
    url(r'pages/profile/$', views.profile,name='profile'),
	url(r'pages/ic_request/$', views.ic_request,name='ic_request'),
	url(r'pages/service_call/$', views.service_call,name='service_call'),
	url(r'pages/scope_of_supply/$', views.scope_of_supply,name='scope_of_supply'),
	url(r'pages/product_model/$', views.product_model,name='product_model'),
	url(r'pages/email/(?P<ic_request>[-\w]+)$', views.email,name='email'),
	url(r'pages/email_pm/(?P<service_call>[-\w]+)$', views.email_pm,name='email_pm'),
	url(r'pages/reporting/$', views.reporting,name='reporting'),
	url(r'pages/your_ic_request/$', views.your_ic_request,name='your_ic_request'),
	url(r'pages/your_service_call/$', views.your_service_call,name='your_service_call'),
	url(r'pages/ic_info/(?P<ic1>[-\w]+)$', views.ic_info,name='ic_info'),
	url(r'pages/sc_info/(?P<sc1>[-\w]+)$', views.sc_info,name='sc_info'),
	url(r'pages/home/$', views.profile,name='home'),
]
