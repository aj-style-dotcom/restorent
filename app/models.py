from django.db import models
from django.contrib.auth.models import User


cat=(
    ('Brackfast','Brackfast'),
    ('Lunch','Lunch'),
    ('Dinner', 'Dinner'),
    ('Snacks', 'Snacks')
)

# Create your models here.
class productModel(models.Model):
    name=models.CharField(max_length=50)
    dic=models.TextField()
    prize=models.IntegerField()
    category=models.CharField(max_length=40, choices=cat)
    image=models.ImageField(upload_to="images")

    def __str__(self) -> str:
        return self.name+"\t\t"+str(self.prize)+"Rs."

class orderModel(models.Model):
    user=models.CharField(max_length=40)
    itemID=models.IntegerField()
    quantity=models.IntegerField()
    orderDate=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user