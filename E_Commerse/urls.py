from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.login_view, name='login'), 
    path('signup/', views.signup_view, name='signup'),
    path('home/',views.homepage,name='home'),
    path('product/<int:product_id>/', views.Productpage, name='product'),
    path('product/<int:product_id>/related/', views.Productpage, name='related_product'),
    path('profile/', views.user_profile, name='profile'), 
    path('add_cart/<int:product_id>/',views.add_to_cart,name='add_cart'),     
    path('categorysearch/<int:category_id>/',views.Categorypage,name = 'categorysearch'),
    path('remove_item/<int:item_id>/', views.remove_cart_item, name='remove_item'),
    path('about',views.about,name="about"),
    path('contact',views.contact,name="contact"),
    path('productlist',views.new_arrival,name='productlist'),
    path('order/<int:product_id>/',views.orderpage,name='order'),
    path('address',views.add_address,name='address'),
    path('order_confirm/<int:order_id>/',views.order_confirmation,name='order_confirm'),
    path('productsearch',views.productSearch,name = 'productsearch'),
    path('vieworders/',views.vieworders,name='vieworders'),
]