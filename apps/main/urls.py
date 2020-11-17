from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^aboutus$', views.aboutus),
    url(r'^services$', views.services),
    url(r'^quote$', views.quote),
    url(r'^quotedone$', views.quotedone),
    url(r'^processquote$', views.processquote),
    url(r'^green$', views.green),
    url(r'^contact$', views.contact),
    url(r'^processcontact$', views.processcontact),
    url(r'^contactdone$', views.contactdone),
    url(r'^pay$', views.pay),
    url(r'^processpayment$', views.processpayment),
    url(r'^paymentdone$', views.paymentdone),
    url(r'^careers$', views.careers),


    

]