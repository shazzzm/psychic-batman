from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'inbox', views.inbox, name="inbox"),
    url(r'message', views.message, name="message"),
    url(r'sendMessage', views.sendMessage, name="send_message"),
    url(r'^$', views.index, name='index'),
]
