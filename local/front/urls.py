from django.urls import path
from . import views

urlpatterns=[

    path('d',views.front),
    path('registration',views.registration_view),
    path('login2',views.login_view2),
    path('login1',views.login_view1),
    path('to_mail',views.to_mail),
    path('link_to_mail',views.link_to_mail),
    path('change_password',views.change_password),
    path('otp_to_mail',views.otp_to_mail),

]
