import store
from django.contrib import admin
from store.models import Category, Merchant, Product, Store

# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    list_per_page = 24


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'availibility', 'updated', 'created')
    prepopulated_fields = {'slug': ('name',)}
    raw_id_fields = ('category',)
    list_editable = ('price', 'availibility')
    list_per_page = 24

@admin.register(Merchant)
class MerchantAdmin(admin.ModelAdmin):
    list_display = ('user','joindate')


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ('name','address','contact','lat','long','start','end','merchant','rating','total_orders')
