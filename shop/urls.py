from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'shop'

urlpatterns = [
	path('<int:category_id>', views.shop, name='shop'),
	path('buy/<int:product_id>', views.buy, name='buy'),
	path('product/<int:product_id>', views.product, name='product'),
	path('save_sell/<int:product_id>', views.save_sell, name='save_sell'),
]