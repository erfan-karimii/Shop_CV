from django.contrib.auth import get_user_model
from django.test import TestCase , Client 
from django.urls import reverse
from http.cookies import SimpleCookie
from django.contrib.auth.hashers import make_password


class TestRegisterView(TestCase):
    def setUp(self):
        User = get_user_model()
        User.objects.create_user(phone_number='09123456789', password='1234')
        self.client = Client()
        self.url = reverse('account:registerView')
    
    def test_register_view_unauthenticated(self):
        resp = self.client.get(self.url)
        self.assertEqual(resp.status_code,200)
        self.assertTemplateUsed(resp,'account/register.html')
    
    def test_register_view_authenticated(self):
        is_verified = self.client.login(phone_number='09123456789', password='1234')
        resp = self.client.get(self.url)
        self.assertTrue(is_verified)
        self.assertRedirects(resp, '/', status_code=302,target_status_code=200)

class TestSendSMS(TestCase):
    def setUp(self):
        self.user_model = get_user_model()
        self.client = Client()
        self.url = reverse('account:send')

    def test_send_sms_GET(self):
        resp = self.client.get(self.url)
        self.assertRedirects(resp, '/account/register/', status_code=302,target_status_code=200)
    
    def test_send_sms_POST(self):
        resp = self.client.post(self.url,data={'phone_number':'09123456789'})
        self.assertEqual(resp.status_code,200)
        self.assertEqual(self.user_model.objects.count(),1)

class TestVerifyChecked(TestCase):
    def setUp(self):
        self.user_model = get_user_model()
        self.client = Client()
        self.url = reverse('account:verify')
        self.cookie = SimpleCookie({'phone_number_cookie':'09123456789'})
        User = get_user_model()
        User.objects.create_user(phone_number='09123456789', password='1234',token='8888')
    
    def test_verify_checked_GET(self):
        resp = self.client.get(self.url)
        self.assertEqual(resp.status_code,200)
        self.assertTemplateUsed(resp,'account/verify.html')

    def test_verify_checked_POST_without_cookies(self):
        resp = self.client.post(self.url)
        self.assertEqual(resp.status_code,302)
        self.assertRedirects(resp, '/account/register/', status_code=302,target_status_code=200)
    
    def test_verify_checked_POST_with_cookies_no_token(self):
        self.client.cookies = self.cookie
        resp = self.client.post(self.url)
        self.assertEqual(resp.status_code,302)
        self.assertRedirects(resp, '/account/VerifyChecked/', status_code=302,target_status_code=200)
        
    def test_verify_checked_POST_with_cookies_and_token(self):
        self.client.cookies = self.cookie
        resp = self.client.post(self.url,data={'token':'8888'})
        self.assertEqual(resp.status_code,302)
        self.assertRedirects(resp, '/account/complateform/', status_code=302,target_status_code=200)

class TestCompeleteProfile(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('account:comp')
        self.cookie = SimpleCookie({'phone_number_cookie':'09123456789'})
        self.user = get_user_model().objects.create_user(phone_number='09123456789',password='old-password',is_verified=True)

    def test_compelete_profile_GET(self):
        resp = self.client.get(self.url)
        self.assertEqual(resp.status_code,200)
        self.assertTemplateUsed(resp,'account/complateprofile.html')
    
    def test_compelete_profile_POST_without_cookie(self):
        resp = self.client.post(self.url)
        self.assertEqual(resp.status_code,302)
        self.assertRedirects(resp, '/account/register/', status_code=302,target_status_code=200)
    
    def test_compelete_profile_POST_with_cookie_no_data(self):
        self.client.cookies = self.cookie
        resp = self.client.post(self.url)
        self.assertRedirects(resp, '/', status_code=302,target_status_code=200)
        self.assertTrue(self.user.check_password("old-password"))
    
    def test_compelete_profile_POST_with_cookie_and_data(self):
        self.client.cookies = self.cookie
        resp = self.client.post(self.url,data={'password':'new-password'})
        self.assertEqual(resp.status_code,302)
        self.assertRedirects(resp, '/', status_code=302,target_status_code=200)

class TestSendResetSMS(TestCase):
    def setUp(self):
        self.url = reverse('account:send2')
        self.client = Client()
        self.user = get_user_model().objects.create_user(phone_number='09123456789',password='old-password',is_verified=True)


    def test_send_reset_sms_GET(self):
        resp = self.client.get(self.url)
        self.assertEqual(resp.status_code,200)
        self.assertTemplateUsed(resp,'account/eghdam.html')
    
    def test_send_reset_sms_POST(self):
        resp = self.client.post(self.url,data={'phone_number':'09123456789'})
        self.assertEqual(resp.status_code,200)
        self.assertTemplateUsed(resp,'account/verify2.html')
