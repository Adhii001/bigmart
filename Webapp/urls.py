from django.urls import path
from Webapp import views

urlpatterns=[
    path('',views.home_page,name="home"),
    path('about/',views.about_page,name="about"),
    path('contact/', views.contact_page, name="contact"),
    path('product/',views.product_page,name="product"),
    path('save_contact/', views.save_contact, name="save_contact"),
    path('products_filtered/<cat_name>/', views.products_filtered, name="products_filtered"),
    path('single_product/<int:pro_id>/', views.single_product, name="single_product"),
    path('registration_page/', views.registration_page, name="registration_page"),
    path('save_registration/', views.save_registration, name="save_registration"),



]