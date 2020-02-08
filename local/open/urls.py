from django.urls import path
from.import views

from open.views import date_time_view

urlpatterns=[

path('datetime',views.date_time_view),

]
