from django.test import TestCase , Client
from django.urls import reverse
from product.models import Product , Comment , Category
from model_bakery import baker


class TestListView(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('product:listview')

    def test_listview_with_no_kwargs(self):
        response = self.client.get(self.url)
        self.assertEqual(response.context['number'],'2')
        self.assertEqual(response.context['op'],'-created')
        self.assertEqual(response.status_code,200)
    
    def test_listview_with_kwargs_none_value(self):
        url = self.url + '?show-number=&orderby='
        response = self.client.get(url)
        self.assertEqual(response.context['number'],'2')
        self.assertEqual(response.context['op'],'-created')
    
    def test_listview_with_kwargs_wrong_value(self):
        url = self.url + '?show-number=wRongData!&orderby=WronGdaTa@'
        response = self.client.get(url)
        self.assertEqual(response.context['number'],'2')
        self.assertEqual(response.context['op'],'-created')
    
    def test_listview_with_kwargs_right_value(self):
        url = self.url + '?show-number=3&orderby=-price'
        response = self.client.get(url)
        self.assertEqual(response.context['number'],'3')
        self.assertEqual(response.context['op'],'-price')


class TestDetailView(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('product:detailview',kwargs={'id':1})
    
    def test_detail_view_GET(self):
        baker.make(Product,info='test', _fill_optional=True, _create_files=True)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code,200)

      
class TestSearchView(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.url = reverse('product:SearchView')
        cat = baker.make(Category,name='Foo')
        cat2 = baker.make(Category,name='Hoo')
        baker.make(Product,info='test',name='Bar',category = cat,_fill_optional=True, _create_files=True)
        baker.make(Product,info='test',name='Baaz',category = cat,_fill_optional=True, _create_files=True)
        baker.make(Product,info='test',name='Haz',category = cat2,_fill_optional=True, _create_files=True)
    
    def test_searchview_no_kwargs(self):
        response = self.client.get('/search/')
        self.assertEqual(response.status_code,200)
        self.assertEqual(Category.objects.count(),2)
        self.assertEqual(Product.objects.count(),3)

    
    def test_searchview_right_kwargs(self):
        response = self.client.get(self.url + '?search=&category=')
        self.assertEqual(response.context['posts'].count(),3)

        response = self.client.get(self.url + '?search=b&category=')
        self.assertEqual(response.context['posts'].count(),2)

        response = self.client.get(self.url + '?search=A&category=2')
        self.assertEqual(response.context['posts'].count(),1)
    



