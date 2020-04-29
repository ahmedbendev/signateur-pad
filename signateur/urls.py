from django.urls import path
from . import views
from .views import home
from . import api

urlpatterns = [
    path('',views.home,name='home'),
    path('save/', api.TestView.as_view(),name='save'),
]
