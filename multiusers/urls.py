from django.urls import include, path
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from .views import multiusers, wholesaler, customer, pharmacist

urlpatterns = [
    path('', multiusers.home, name='home'),

    path('customer/', include(([
        path('', customer.homey, name='homey'),
        
        #url to fetch all products
        url(r'^product_list/$', customer.product_list, name='product_list'),
    	
    	#products we be filtered by a given category
    	url(r'^(?P<category_slug>[-\w]+)/$', customer.product_list, name='product_list_by_category'),
    	
    	#url for specific product
    	url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', customer.product_detail, name='product_detail'),

        url(r'^create/$', customer.order_create, name='order_create'),

        url(r'^$', customer.cart_detail, name='cart_detail'),
    
        url(r'^add/(?P<product_id>\d+)/$', customer.cart_add, name='cart_add'),
    
        url(r'^remove/(?P<product_id>\d+)/$', customer.cart_remove, name='cart_remove'),
        
    ], 'shop'), namespace='customer')),


    path('wholesaler/', include(([
        path('', wholesaler.homey, name='homey'),
        path('w_p.html', wholesaler.WProduct_list, name='WProduct_list'),

        
    ], 'shop'), namespace='wholesaler')),


    path('pharmacist/', include(([
        path('', pharmacist.homey, name='homey'),
        path('p_w.html', pharmacist.pharmapp, name='pharmapp'),
        
        
    ], 'shop'), namespace='pharmacist')),

]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
