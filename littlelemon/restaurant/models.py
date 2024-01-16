from django.db import models

class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField() #max_digits=6
    booking_date = models.DateTimeField()
    
    def __str__(self):
        return self.name
    
class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField() #max_digits=5

    def __str__(self):
        return f'{self.title} : {str(self.price)}'
    
    def get_item(self):
        return f'{self.title} : {str(self.price)}'