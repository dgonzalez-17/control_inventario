"""authProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from authApp import views
from authApp.views.cliente.clienteCreateView import CustomerCreateView
from authApp.views.cliente.clienteDetailView import CustomerDetailView
from authApp.views.cliente.clienteUpdateView import CustomerUpdateView
from authApp.views.cliente.clienteDeleteView import CustomerDeleteView
from authApp.views.proveedor.proveedorCreateView import ProveedorCreateView
from authApp.views.proveedor.proveedorDeleteView import ProveedorDeleteView
from authApp.views.proveedor.proveedorDetailView import ProveedorDetailView
from authApp.views.proveedor.proveedorUpdateView import ProveedorUpdateView
from authApp.views.logistica.logisticaCreateView import LogisticCreateView
from authApp.views.logistica.logisticaDeleteView import LogisticDeleteView
from authApp.views.logistica.logisticaDetailView import LogisticDetailView
from authApp.views.logistica.logisticaUpdateView import LogisticUpdateView
from authApp.views.vendedor.vendedorCreateView import SellerCreateView
from authApp.views.vendedor.vendedorDeleteView import SellerDeleteView
from authApp.views.vendedor.vendedorDetailView import SellerDetailView
from authApp.views.vendedor.vendedorUpdateView import SellerUpdateView
from authApp.views.producto.productCreateView import ProductCreateView
from authApp.views.producto.productDeleteView import ProductDeleteView
from authApp.views.producto.productDetailView import ProductDetailView
from authApp.views.producto.productUpdateView import ProductUpdateView
from authApp.views.administrador.administradorCreateView import AdministratorCreateView
from authApp.views.administrador.administradorDeleteView import AdministratorDeleteView
from authApp.views.administrador.administradorUpdateView import AdministratorUpdateView
from authApp.views.administrador.administradorDetailView import AdministratorDetailView
from authApp.views.administrador.administradorLoginView import AdministratorLoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cliente/crear', views.CustomerCreateView.as_view()),
    path('cliente/listar', views.CustomerDetailView.as_view()),
    path('cliente/actualizar/<int:customer_id>', views.CustomerUpdateView.as_view()),
    path('cliente/eliminar/<int:customer_id>', views.CustomerDeleteView.as_view()),
    path('proveedor/crear', views.ProveedorCreateView.as_view()),
    path('proveedor/eliminar/<int:proveedor_id>', views.ProveedorDeleteView.as_view()),
    path('proveedor/listar', views.ProveedorDetailView.as_view()),
    path('proveedor/actualizar/<int:proveedor_id>', views.ProveedorUpdateView.as_view()),
    path('logistica/crear', views.LogisticCreateView.as_view()),
    path('logistica/eliminar/<int:Logistics_id>', views.LogisticDeleteView.as_view()),
    path('logistica/listar', views.LogisticDetailView.as_view()),
    path('logistica/actualizar/<int:Logistics_id>', views.LogisticUpdateView.as_view()),
    path('vendedor/crear', views.SellerCreateView.as_view()),
    path('vendedor/eliminar/<int:seller_id>', views.SellerDeleteView.as_view()),
    path('vendedor/listar', views.SellerDetailView.as_view()),
    path('vendedor/actualizar/<int:seller_id>', views.SellerUpdateView.as_view()),
    path('producto/crear', views.ProductCreateView.as_view()),
    path('producto/eliminar/<int:producto_id>', views.ProductDeleteView.as_view()),
    path('producto/listar', views.ProductDetailView.as_view()),
    path('producto/actualizar/<int:producto_id>', views.ProductUpdateView.as_view()),
     path('administrador/crear', views.AdministratorCreateView.as_view()),
    path('administrador/eliminar/<int:administrator_id>', views.AdministratorDeleteView.as_view()),
    path('administrador/listar', views.AdministratorDetailView.as_view()),
    path('administrador/actualizar/<int:administrator_id>', views.AdministratorUpdateView.as_view()),
    path('administrador/iniciarsesion', views.AdministratorLoginView.as_view())
]
