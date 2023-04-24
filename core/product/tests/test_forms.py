from django.test import TestCase  , Client
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
from model_bakery import baker
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.chrome.webdriver import WebDriver
from product.models import Product , Comment , Category
from selenium.webdriver.common.by import By

from product.forms import CommentForm
import datetime
from time import sleep

class TestDetailViewCommentForm(TestCase):
    def setUp(self):
        self.client = Client()
        self.obj = baker.make(Product,info='test',_fill_optional=True, _create_files=True)
        self.url = reverse('product:detailview',kwargs={'id':1})

    def test_detailview_comment_form_no_data(self):
        form = CommentForm({})
        self.assertFalse(form.is_valid()) 
        
    def test_detail_view_comment_right_data(self):
        baker.make(Product,info='test', _fill_optional=True, _create_files=True)
        data = {
            'product' : '1',
            'username' : 'Foo',
            'email' : 'test@test.com',
            'body' : 'Bazz',
            'point' : '1',
            'created' : datetime.datetime.now(),
        }
        response = self.client.post(self.url,data=data)
        self.assertEqual(Comment.objects.count(),1)
        self.assertEqual(response.status_code,200)
    
    def test_detail_view_comment_wrong_data(self):
        baker.make(Product,info='test', _fill_optional=True, _create_files=True)
        data = {
            'product' : '256',
            'username' : '',
            'email' : 'test.com',
            'body' : '',
            'point' : '10',
        }
        response = self.client.post(self.url,data=data)
        
        self.assertEqual(Comment.objects.count(),0)
        self.assertEqual(len(response.context['comment_form'].errors.keys()),5)
        self.assertEqual(response.status_code,200)

    
class TestDetailViewCommentFormWithSelenium(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(10)
        baker.make(Product,info='test',_fill_optional=True, _create_files=True)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_login(self):
        self.selenium.get(f"{self.live_server_url}/detail/1")
        Alert(self.selenium).accept()
        self.selenium.find_element('id','id_username').send_keys("erfan")
        self.selenium.find_element('id','id_email').send_keys("test@test.com")
        self.selenium.find_element('id','id_body').send_keys("this is a test text")
        element = self.selenium.find_element('id','submit')
        self.selenium.execute_script("arguments[0].scrollIntoView();", element)
        self.selenium.execute_script("arguments[0].click();", element)
        self.assertEqual(Comment.objects.count(),1)

