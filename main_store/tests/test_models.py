
from django.test import TestCase
from django.contrib.auth.models import User
from main_store.models import Category, Product


class TestCategoriesModel(TestCase):

    def setUp(self):
        self.data1 = Category.objects.create(name='jumpers', slug='jumpers')

    def test_category_model_entry(self):
        """
        Test category model data insertion/types/field attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data, Category))

    def test_category_model_entry(self):
        """
        Test category model reutn name
        """
        data = self.data1
        self.assertEqual(str(data), 'jumpers')


class TestProductsModel(TestCase):
    def setUp(self):
        Category.objects.create(name='jumpers', slug='jumpers')
        User.objects.create(username='admin')
        self.data1 = Product.objects.create(
            category_id=1, title='jumper', created_by_id=1, slug='jumpers', price='55.00', image='24558967-2')

    def test_products_model_entry(self):
        """
        Testproduct model data insertion/types/field attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data, Product))
        self.assertEqual(str(data), 'jumper')


