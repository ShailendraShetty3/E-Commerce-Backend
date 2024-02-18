# from django.contrib import admin
# from django.urls import path, include
# from ecommerce.views import UserList


# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('user/', UserList.as_view()),
#     # path('user/<int:id>/', UserDetail.as_view(), name='user-detail'),

# ]

from django.contrib import admin
from django.urls import path
from .views import UserListCreateView, UserDetail
from .views import SocialListCreateView, SocialDetail
from .views import CartListCreateView, CartDetail
from .views import CartItemsListCreateView
from .views import OrderListCreateView, OrderDetail
from .views import CredentialListCreateView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="E Commerce API ",
        default_version='v1',
        description="E-Commerce",
        terms_of_service="https://www.yourapp.com/terms/",
        contact=openapi.Contact(email="xyz@gmail.com"),
        license=openapi.License(name="Your License"),
    ),
    public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', UserListCreateView.as_view(), name='user-list-create'),
    path('users/<int:id>/', UserDetail.as_view(), name='user-detail'),
    path('social/', SocialListCreateView.as_view(), name='social-list-create'),
    path('social/<int:id>/', SocialDetail.as_view(), name='social-detail'),
    path('cart/', CartListCreateView.as_view(), name='cart-list-create'),
    path('cart/<int:id>/', CartDetail.as_view(), name='social-detail'),

    path('cartItems/', CartItemsListCreateView.as_view(), name='cart-list-create'),

    path('order/', OrderListCreateView.as_view(), name='order-list-create'),
    path('order/<int:id>/', OrderDetail.as_view(), name='order-detail'),
    path('credential/', CredentialListCreateView.as_view(), name='order-list-create'),

    # Swagger documentation URLs
    path('swagger(?P<format>\.json|\.yaml)/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
