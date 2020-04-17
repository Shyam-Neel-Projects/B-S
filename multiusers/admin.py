from django.contrib import admin
from multiusers.models import ApprovImg, Category, Product, User, Order, OrderItem


admin.site.site_header = 'B & S Admin Dashboard'

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'stock', 'available', 'created_at', 'updated_at','updated_by']
    list_filter = ['available', 'created_at', 'updated_by']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}
  

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email', 'address', 'postal_code', 'city', 'paid', 'created',
                    'updated']
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline]


admin.site.register(Order, OrderAdmin)    
admin.site.register(Category, CategoryAdmin) 
admin.site.register(Product, ProductAdmin)
admin.site.register(User)
