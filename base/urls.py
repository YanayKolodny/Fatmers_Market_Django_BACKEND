from django.urls import path
from .viewsFolder.authViews import MyTokenObtainPairView, registration, logOutUser
from .viewsFolder.productViews import AddProductToStand, delProd, updProd, getUserProds, getAllProds, getStandProds, getCategoryProds
from .viewsFolder.categoryViews import delCategory, updCategory, addNewCategory, getStandCategories, getAllCategories, addCategory
from .viewsFolder.standViews import addNewStand, delStand, getUserStand, getAllStands, getAreasStands, updUserToStaff, updStandInfo
from .viewsFolder.orderViews import newOrder, getAllOrderedProds, getAllOrders, getUserOrders, getStandOrders, getOrderProducts
from .viewsFolder.areaViews import addNewArea, getAllAreas, delArea, updArea
from .viewsFolder.profileViews import updUserProfile, getProfile
from rest_framework_simplejwt.views import (TokenRefreshView)



urlpatterns = [

    # Registration:
    path('register/', registration),
    # LogIn:
    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # LogOut:
    path('logoutuser/', logOutUser, name='logOut'),

    # Area
    path('areas/addnewarea/', addNewArea),
    path('areas/getallareas/', getAllAreas),
    path('areas/del/<int:area_id>/', delArea),
    path('areas/upd/<int:area_id>/', updArea),

    # Profile
    path('profile/updprofile/<int:id>/', updUserProfile),
    path('profile/getprofile/<int:id>/', getProfile),

    # Stands
    path('stands/addnewstand/', addNewStand.as_view(), name='addNewStand'),
    path('user/status/<int:id>/', updUserToStaff),
    path('stands/getuserstand/', getUserStand),
    path('stands/getareasstands/<int:area_id>/', getAreasStands),
    path('stands/getallstands/', getAllStands),
    path('stands/deletestand/<int:id>/', delStand),
    path('stands/updstand/<int:id>/', updStandInfo),

    # Categories
    path('categories/getallcategories/', getAllCategories),
    path('categories/standcategories/<int:stand_id>/', getStandCategories),
    path('categories/addcategory/', addCategory.as_view(), name='addCategory'),
    path('categories/addnewcategory/', addNewCategory),
    path('categories/delcategory/<id>/', delCategory),
    path('categories/updcategory/<int:id>/', updCategory),
    
    # PRODUCTS
    path('products/allprods/', getAllProds, name="prods"),
    path('products/userprods/', getUserProds, name="userProds"),
    path('products/standprods/<int:stand_id>',getStandProds, name="standProds"),
    path('products/categoryprods/<int:category_id>',getCategoryProds, name="categoryProds"),    
    path('products/addnewstandprod/', AddProductToStand.as_view(), name="addNewStandProduct"), # Add product with photo
    path('products/delete/<id>/', delProd),
    path('products/update/<int:id>/', updProd),

    # Orders
    path('orders/neworder/', newOrder),
    path('orders/getallorders/', getAllOrders),
    path('orders/getallorderedprods/', getAllOrderedProds),
    path('orders/getuserorders/<int:user_id>/', getUserOrders),
    path('orders/getstandorders/<int:stand_id>/', getStandOrders),
    path('orders/getorderproducts/<int:order_id>/', getOrderProducts)

]
