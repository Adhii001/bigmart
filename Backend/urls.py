from django.urls import path
from Backend import views

urlpatterns=[
    path('Index_page/',views.index_page,name="index_page"),
    path('category/',views.category,name="category"),
    path('save_category/', views.save_category, name="save_category"),
    path('display_category/', views.display_category, name="display_category"),
    path('edit_category/<int:c_id>/', views.edit_category, name="edit_category"),
    path('update_category/<int:c_id>/', views.update_category, name="update_category"),
    path('delete_category/<int:c_id>/', views.delete_category, name="delete_category"),
    path('admin_login/', views.admin_login, name="admin_login"),
    path('login_page/',views.login_page,name="login_page"),
    path('admin_logout/', views.admin_logout, name="admin_logout"),
    path('add_product/', views.product_page, name="add_product"),
    path('save_product/', views.save_product, name="save_product"),
    path('display_product/', views.display_product, name="display_product"),
    path('edit_product/<int:pro_id>/', views.edit_product, name="edit_product"),
    path('update_product/<int:pro_id>/', views.update_product, name="update_product"),
    path('delete_product/<int:pro_id>/', views.delete_product, name="delete_product"),
    path('contact_data/', views.contact_info, name="contact_data"),
    path('delete_cinfo/<int:i_id>/', views.delete_cinfo, name="delete_cinfo"),
]