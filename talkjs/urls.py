from django.urls import include, re_path
from .views import (
    current_session,
    private_message_to_talkjs_chat, 
    quick_message_to_talkjs_chat,
    create_talkjs_chat,
    invite_to_talkjs_chat,
    leave_talkjs_chat
)

urlpatterns = [
    re_path(r'private/(?P<other_id>[\d]+)/', private_message_to_talkjs_chat, name='talk-private'),
    re_path('session/current/', current_session, name='talk-current-session'),
    re_path(r'quick/(?P<conversationId>\w+)/', quick_message_to_talkjs_chat, name='talk-quick-message'),
    re_path('chat/', create_talkjs_chat, name='talk-create-chat'),
    re_path(r'leave/(?P<conversationId>\w+)/', leave_talkjs_chat, name='talk-leave-chat'),
    re_path(r'invitation/(?P<conversationId>\w+)/', invite_to_talkjs_chat, name='talk-invitation'),
]