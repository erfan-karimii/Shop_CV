from django.test import TestCase , Client
from django.urls import reverse
from contactus.models import ContactUsKeeper , Newsletter

class TestContactUsView(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('contactus:contact-us')
    
    def test_get_url(self):
        resp = self.client.get(self.url)
        self.assertEqual(resp.status_code,200)
        self.assertIn('SiteSetting' , resp.context)
        self.assertTemplateUsed(resp,'contact.html')

class TestValidateContactUsView(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('contactus:save-contact-us')
    
    def test_validate_contact_us(self):
        resp = self.client.post(self.url,data={'full_name':'ali alizade', 'email':"test@test.com", 'subject':'test','message':'this is test'})
        self.assertEqual(ContactUsKeeper.objects.count(),1)
        self.assertEqual(resp.status_code,302)
        self.assertRedirects(resp, '/contact-us/', status_code=302,target_status_code=200)

class TestValidateContactUsView(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('contactus:save-newsletter-email')
    
    def test_validate_contact_us(self):
        resp = self.client.post(self.url,data={'email':"test@test.com"})
        self.assertEqual(Newsletter.objects.count(),1)
        self.assertEqual(resp.status_code,302)
        self.assertRedirects(resp, '/', status_code=302,target_status_code=200)

