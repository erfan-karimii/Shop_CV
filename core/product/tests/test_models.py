from django.test import TestCase 
from product.models import Product , Category , TagProduct , Size , Color ,GalleryImage , Comment
from model_bakery import baker


class TestCategoryModel(TestCase):
    def setUp(self) :
        self.cat1 = baker.make(Category,name='test', _create_files=True)
        
    def test_def_str(self):
        self.assertEqual(str(self.cat1),"test")

class TestTagProductModel(TestCase):
    def setUp(self) :
        self.tag1 = baker.make(TagProduct,name='test')
        
    def test_def_str(self):
        self.assertEqual(str(self.tag1),"test")

class TestProductModel(TestCase):
    def setUp(self) :
        self.product =  baker.make(Product,info='test',name='product_test',_fill_optional=True,_create_files=True)
        
    def test_def_str(self):
        self.assertEqual(str(self.product),"product_test")
    
    def test_def_main_discount_call(self):
        after_discount_price = self.product.price - (self.product.price * (self.product.discount/100))
        self.assertEqual(after_discount_price,self.product.main_discount_call())

class TestSizeModel(TestCase):
    def setUp(self) :
        obj = baker.make(Product,info='test',name='product_test',_fill_optional=True,_create_files=True)
        self.size = baker.make(Size,size='test',product=obj)
        
    def test_def_str(self):
        self.assertEqual(str(self.size),"test")

class TestColorModel(TestCase):
    def setUp(self) :
        obj = baker.make(Product,info='test',name='product_test',_fill_optional=True,_create_files=True)
        self.color = baker.make(Color,color='test',product=obj)
        
    def test_def_str(self):
        self.assertEqual(str(self.color),"product_test test")

class TestGalleryImageModel(TestCase):
    def setUp(self) :
        obj = baker.make(Product,info='test',name='product_test',_fill_optional=True,_create_files=True)
        self.gallery_image = baker.make(GalleryImage,product=obj,_create_files=True)
        
    def test_def_str(self):
        self.assertEqual(str(self.gallery_image),str(self.gallery_image.image))

class TestCommentModel(TestCase):
    def setUp(self) :
        obj = baker.make(Product,info='test',name='product_test',_fill_optional=True,_create_files=True)
        self.comment = baker.make(Comment,username='test',product=obj)
        
    def test_def_str(self):
        self.assertEqual(str(self.comment),"test")


