from django.urls import path
from . import views

urlpatterns = [
    path('request/', views.request_new, name="request"),
    path('submit/', views.submitted, name="submitted"),
    path('verifycaptcha/', views.verify_captcha, name="verify_captcha")
]
