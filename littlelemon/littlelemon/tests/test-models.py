from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuItemSerializer

class MenuTest(TestCase):
    
    #def createMenu(self):
        
    
    def test_fields(self):
        self.menu = Menu.objects.create(
            title = "soup",
            price = 7,
            inventory = 10
        )
        self.assertIsInstance(self.menu.title, str)
    
    def test_get_item(self):
        Menu.objects.create(
            title = "soup",
            price = 7,
            inventory = 10
        )
        item = Menu.objects.get(title="soup")
        itemstr = item.get_item()
        self.assertEqual(itemstr, "soup : 7")
        
        
class MenuViewTest(TestCase):
    # def setUp(self):
    #     Menu.objects.create(title = "soup", price = 7, inventory = 10)
    #     Menu.objects.create(title = "curry", price = 12, inventory = 50)
        
    def test_getall(self):
        Menu.objects.create(title = "soup", price = 7, inventory = 10)
        Menu.objects.create(title = "curry", price = 12, inventory = 50)
        item = Menu.objects.get(title="soup")
        item_serial = MenuItemSerializer(item)
        #print(item_serial.data)
        self.assertEqual(str(item_serial.data), "{'id': 1, 'title': 'soup', 'price': '7.00', 'inventory': 10}")
        