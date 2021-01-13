from django.urls import path
from.views import add_room as x1
from.views import costumer_fill_form as x2
from .views import  check_room_available as x3
from .views import search_room as x4
from .views import sign_in as x5
from .views import sign_up as x6
from .views import activity as x7
from.views import logout_ as x8
from.views import user_activity as x9

urlpatterns = [
    path('', x1, name='home'),
    path('fill_form', x2, name='fill_form'),
    path('check', x3, name='check'),
    path('search', x4, name='search'),
    path('sign_in', x5, name='sign_in'),
    path('sign_up', x6, name='sign_up'),
    path('activity', x7, name='activity'),
    path('logout', x8, name='logout'),
    path('user_activity', x9, name='user_activity'),
]

