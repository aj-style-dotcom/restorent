from django.contrib import admin
from .models import productModel, orderModel
# Register your models here.


admin.site.register(productModel)
admin.site.register(orderModel)
