from django.test import TestCase , Client
from aboutus.models import AboutUsProperty,AboutUsProgressBar
from model_bakery import baker

class TestAboutUsPropertyModel(TestCase):
    def setUp(self) :
        self.aboutus_property =  baker.make(AboutUsProperty,title='test')
        
    def test_def_str(self):
        self.assertEqual(str(self.aboutus_property),"test")

class TestAboutUsProgressBarModel(TestCase):
    def setUp(self) :
        self.aboutus_progress_bar =  baker.make(AboutUsProgressBar,title='test')
        
    def test_def_str(self):
        self.assertEqual(str(self.aboutus_progress_bar),"test")