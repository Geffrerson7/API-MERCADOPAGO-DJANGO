from django.urls import path
from .views import *

urlpatterns = [
    path('proccess_payment/', ProcessPaymentAPIView.as_view(),name='proccess_payment'), 
    ]