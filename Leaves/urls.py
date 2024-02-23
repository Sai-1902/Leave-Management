
from django.urls import path
from Leaves import views

urlpatterns = [
    path('request/', views.leave_request ,name='leave_request'),
    path('list/', views.leave_list, name='leave_list'),
    path('count/', views.leave_count, name='leave_count'),
]