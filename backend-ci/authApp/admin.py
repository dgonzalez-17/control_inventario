from django.contrib import admin
from .models.cliente import Customer
from .models.factura import Invoice
from .models.proveedor import Proveedor
from .models.product import Product
from .models.administrador import Administrator
from .models.logistica import Logistic
from .models.vendedor import Seller
# Register your models here.
admin.site.register(Customer)
admin.site.register(Invoice)
admin.site.register(Proveedor)
admin.site.register(Product)
admin.site.register(Administrator)
admin.site.register(Logistic)
admin.site.register(Seller)
