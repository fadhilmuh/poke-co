from django.urls import path
from main.views import (show_main, create_item, 
                        show_xml, show_json, 
                        show_xml_by_id, show_json_by_id, 
                        register, login_user,
                        logout_user, delete_item, add_item, subtract_item,
                        get_product_json, add_product_ajax, delete_product_ajax, update_product_qty_ajax,
                        create_product_flutter, show_json_user
                        )

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-item', create_item, name='create_item'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('delete_item/<int:item_id>/', delete_item, name='delete_item'),
    path('add_item/<int:item_id>/', add_item, name='add_item'),
    path('subtract_item/<int:item_id>/', subtract_item, name='subtract_item'),
    path('get-product/', get_product_json, name='get_product_json'),
    path('create-product-ajax/', add_product_ajax, name='add_product_ajax'),
    path('delete_product_ajax/', delete_product_ajax, name='delete_product_ajax'),
    path('update_product_qty_ajax/', update_product_qty_ajax, name='update_product_qty_ajax'),
    path('create-flutter/', create_product_flutter, name='create_product_flutter'),
    path('json-user/<str:uname>/', show_json_user, name='show_json_user'),
]