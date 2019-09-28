from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^grant_wish/(?P<my_num>\d+)$', views.grantWish),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^wishes$', views.wishingApp),
    url(r'^likebutton$', views.likeButton),
    url(r'^wishes/new$', views.newWish),
    url(r'^wishes/create$', views.createWish),
    url(r'^wishes/edit/(?P<my_num>\d+)$', views.editWish),
    url(r'^edit/update$', views.editWisUpdate),
    url(r'^wishes/granted/(?P<my_num>\d+)$', views.grantedWishs),
    url(r'^delete/(?P<my_num>\d+)$', views.delete), # Function
    url(r'^logout$', views.logOut), # Function
]
