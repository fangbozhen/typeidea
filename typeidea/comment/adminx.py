from django.contrib import admin
import xadmin

from .models import Comment
from typeidea.custom_site import custom_site


@xadmin.sites.register(Comment)
class CommentAdmin(object):
    list_display = ('target', 'content', 'nickname', 'website', 'email', 'created_time')
