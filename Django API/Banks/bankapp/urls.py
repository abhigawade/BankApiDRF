from django.urls import path
from .views import BankModelView

urlpatterns = [
    path('banks/',BankModelView.as_view(), name='banks'),
    path('banks/<int:pk>/',BankModelView.as_view(), name='banks'),
]
