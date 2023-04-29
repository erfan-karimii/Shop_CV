from django.test import TestCase 
from contactus.models import Newsletter,ContactUsKeeper
from model_bakery import baker


class TestNewsletterModel(TestCase):
    def setUp(self) :
        self.news = baker.make(Newsletter,email='test@test.com',)
        
    def test_def_str(self):
        self.assertEqual(str(self.news),"test@test.com")

class TestContactUsKeeperModel(TestCase):
    def setUp(self) :
        self.contact = baker.make(ContactUsKeeper,subject='test subject',)
        
    def test_def_str(self):
        self.assertEqual(str(self.contact),"test subject")