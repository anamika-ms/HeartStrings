from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('index/',views.index,name='index'),
    path('user_register/',views.user_register,name='user_register'),
    path('user_login/',views.user_login,name='user_login'),
    path('profile/',views.profile,name='profile'),
    
    path('donation/',views.donation,name='donation.html'),
    path('add_recipient/',views.add_recipient,name='add_recipient.html'),
    path('add_donors/',views.add_donors,name='add_donors.html'),
    
    
    
    path('donors/',views.donors,name='donors.html'),
    path('blood/',views.bloodview,name='blood'),
    path('bonemarrow/',views.bonemarrowview,name='bonemarrow'),
    path('kidney/',views.kidneyview,name='kidney'),
    path('liver/',views.liverview,name='liver'),
    path('lungs/',views.lungsview,name='lungs'),
    # path('lungs/<str:organs>',views.lungsview,name='lungs_organ'),
    path('heart/',views.heartview,name='heart'),
    path('pancreas/',views.pancreasview,name='pancreas'),
    path('intestine/',views.intestineview,name='intestine'),
    path('eye/',views.eyeview,name='eye'),
    path('home/',views.home,name='home'),
    path('feedback/',views.feedback,name='feedback'),
    path('about/',views.about,name='about.html'),
    path('hospital_register/',views.hospital_register,name='hospital_register'),
    path('hospital_login/',views.hospital_login,name='hospital_login'),
    path('h_home/',views.h_home,name='h_home'),
    path('h_profile/',views.h_profile,name='h_profile'),
    # path('recipient_register/',views.recipient_register,name='recipient_register'),
    # path('recipient_login/',views.recipient_login,name='recipient_login'),
    # path('r_profile/',views.r_profile,name='r_profile'),    
    path('list_recipient',views.list_recipient,name='list_recipient'),
    path('search/',views.search,name='search'),

    path('admin_login/',views.admin_login,name='admin_login'),
    path('admin_home/',views.admin_home,name='admin_home'),
    path('users_list/',views.users_list,name='users_list'),
    path('delete_record1/<int:id>',views.delete_record1,name="delete_record1"),
    path('hospitals_list/',views.hospitals_list,name='hospitals_list'),
    path('delete_record2/<int:id>',views.delete_record2,name="delete_record2"),
    path('organs_list/',views.organs_list,name='organs_list'),
    path('delete_record3/<int:id>',views.delete_record3,name="delete_record3"),
    path('recipients_list/',views.recipients_list,name='recipients_list'),
    path('delete_record4/<int:id>',views.delete_record4,name="delete_record4"),
    
    path('my_donations/',views.my_donations,name='my_donations'),
    
    path('feedback_list/',views.feedback_list,name='feedback_list'),
    path('delete_record5/<int:id>',views.delete_record5,name="delete_record4"),

    path('edit_profile',views.edit_profile,name='edit_profile'),
    path('update_profile/',views.update_profile,name='update_profile'),
    path('update_status/', views.update_status, name='update_status'),
   
    ]

