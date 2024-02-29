from django.urls import path
from .views import find, read, index, write, clear_all

urlpatterns = [
    path('', index, name='textstash_index'),

    path('eternalsunshineofthespotlessmind', clear_all, name='clear_all'),

    path('read', find, name='find'),
    path('read/<str:title>/', read, name='get_text'),
    path('write', write, name='write_text'),
]