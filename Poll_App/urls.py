from django.urls import path
from .views import *


urlpatterns = [
    
    path('',home,name="home"),
    path('create',create,name="create"),
    path('vote/<int:poll_id>',vote,name="vote"),
    path('results/<int:poll_id>',results,name="results"),
]
