from django.urls import path
from . import views

urlpatterns = [
    path('request/', views.request_new, name="request"),
    path('status/', views.status, name="status"),
    path('login/', views.login, name='login'),
    path('verifycaptcha/', views.verify_captcha, name="verify_captcha")
]
