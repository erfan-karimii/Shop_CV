from django.test import TestCase , Client
from django.urls import reverse


class TestAboutUsView(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('aboutus:about-us')
    
    def test_get_url(self):
        resp = self.client.get(self.url)
        self.assertEqual(resp.status_code,200)
        self.assertTrue('AboutUsGeneral' in resp.context)
        self.assertTrue('AboutUsProperty' in resp.context)
        self.assertTrue('AboutUsProgressBar' in resp.context)
        self.assertTemplateUsed('about.html')

