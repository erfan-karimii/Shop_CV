from django.test import TestCase , Client
from django.urls import reverse
from cart.views import total_priceCA
from product.models import Product , Color,Size
from model_bakery import baker
from django.http import Http404
from http.cookies import SimpleCookie


class TestGetOederIDView(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('cart:get_order_id')
    
    def test_get_url(self):
        resp = self.client.get(self.url)
        self.assertJSONEqual(
            str(resp.content, encoding='utf8'),
            {'order_id': 1})

class TestTotalPriceCalculator(TestCase):
    def setUp(self):
        self.product_obj = baker.make(Product,info='test',price=1000,discount=0, _fill_optional=True, _create_files=True)
        self.color_obj = baker.make(Color,color='#ffffff',product=self.product_obj,Ekhtelaf=100)
        self.size_obj = baker.make(Size,size='L',product=self.product_obj, Ekhtelaf=200)


    def test_total_price_ca_with_origin_value(self):
        result = total_priceCA(1,self.product_obj.orgin_color,self.product_obj.orgin_size)
        self.assertIsInstance(result,int)
        self.assertEqual(result,1000)
    
    def test_total_price_ca_with_not_origin_value(self):
        result = total_priceCA(1,self.color_obj.color,self.size_obj.size)
        self.assertIsInstance(result,int)
        self.assertEqual(result,1300)
    
    def test_total_price_ca_with_not_right_value(self):
        with self.assertRaises(Http404):
            total_priceCA(1,'#ffffff','F')
            total_priceCA(1,'#aaaaaa','L')

class TestAddUserOrder(TestCase):
    def setUp(self):
        self.url = reverse('cart:add_user_order')
        self.product_obj = baker.make(Product,info='test',price=1000,discount=0,product_count=2, _create_files=True)
        self.client = Client()
        self.cookie = SimpleCookie({"Order":"1","OrderDetail":"{}"})
        
    def test_add_user_order(self):
        data={'product_id':1, 'color':self.product_obj.orgin_color, 'size':self.product_obj.orgin_size ,'count':1}
        self.client.cookies = self.cookie
        resp = self.client.post(self.url,data=data)
        self.assertRedirects(resp, '/cart/', status_code=302,target_status_code=200)

class TestUserOpenOrder(TestCase):
    def setUp(self):
        self.url = reverse('cart:user_open_order')
        self.product_obj = baker.make(Product,info='test',price=1000,discount=0,product_count=2, _create_files=True)
        self.client = Client()
        self.cookie = SimpleCookie({"OrderDetail":"{\"1\":{\"id\":\"1\",\"color\":\"test\",\"size\":\"test\",\"count\":1}}"})
        
    def test_user_open_order(self):
        self.client.cookies = self.cookie
        resp = self.client.get('/cart/')
        print(self.url)
        # self.assertEqual(resp.status_code,200)
        # self.assertTemplateUsed(resp,'cart.html')

    
