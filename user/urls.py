from django.conf.urls import url
from .views import (
    index,
    login,
    do_login,
    create_conversation,
    serve_conversation
)

urlpatterns = [
    url(r'^login/', login, name='login'),
    url(r'^login-do/', do_login, name='do_login'),
    url(r'^create-conversation/', create_conversation, name='create_conversation'),
    url(r'^conversation/(?P<conversation_id>[^/]+)/', serve_conversation, name='serve_conversation'),
    url(r'^', index, name='index'),
]