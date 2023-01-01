from django.urls import path
from . import views


app_name='account'

urlpatterns = [
    path("register/",views.registerView,name='registerView'),
    path('sendsms1/',views.send_sms_test,name='send'),
    path('VerifyChecked/',views.VerifyChecked,name='verify'),
    path('complateprofile/',views.ComplateProfileView,name='comp'),
    path('complateform/',views.ComplateProfile,name='complate'),
    path('logout/',views.LogOut,name='logout'),
    path('resetpassword/',views.respass,name='resetpasswordsms'),
]


