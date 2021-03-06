from django.urls import path
from shop.views import Product_List, Product_Detail
from shop.views import Product_List_View, Product_Detail_View
from shop.views import Product_Category_List_View, Category_List_View, Shop_main
from shop.views import Category_Create_View


app_name='shop'

urlpatterns = [

    path('api/prod-list', Product_List_View.as_view()),
    path('api/prod-detail/<int:id>/', Product_Detail_View.as_view()),
    path('api/prod-category-list', Category_List_View.as_view()),
    path('api/prod-category-list-by/<int:id>/', Product_Category_List_View.as_view()),

    path('api/prod-category-add', Category_Create_View.as_view()),

    path('', Product_List, name='ProductList' ),
    # path('', Shop_main, name='ProductList' ),


    path('<category_slug>/', Product_List, name='ProductListByCategory' ),
    path('<int:id>/<slug:slug>/', Product_Detail, name='ProductDetail' ),

    path('<category_slug>/', Product_List_View.as_view(), name='prod_list'),
    path('<int:id>/<slug:slug>/', Product_Detail_View.as_view(), name='prod_detail'),


]