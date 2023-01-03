from django.urls import path 
from .views import contact_us_view , validate_contact_us , validate_newsletter

app_name='contactus'

urlpatterns = [
    path('contact-us/',contact_us_view,name='contact-us'),
    path('save-contact-us/',validate_contact_us,name='save-contact-us'),
    path('save-newsletter-email/',validate_newsletter,name='save-newsletter-email'),

]
