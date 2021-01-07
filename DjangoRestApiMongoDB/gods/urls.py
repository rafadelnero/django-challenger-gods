from django.conf.urls import url
from gods import views

urlpatterns = [ 
    url(r'^api/gods$', views.god_list),
    url(r'^api/gods/(?P<pk>[0-9]+)$', views.god_detail),
    url(r'^api/gods/greek$', views.god_list_greek)
]
