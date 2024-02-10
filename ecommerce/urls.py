from django.contrib import admin
from django.urls import path, include
from ecommerce.views import UserList, UserDetail
# from rest_framework.urlpatterns import format_suffix_patterns
# from drf_yasg.views import get_schema_view
# from drf_yasg import openapi

# schema_view = get_schema_view(
#     openapi.Info(
#         title="Your API",
#         default_version='v1',
#         description="Your API description",
#         terms_of_service="https://www.yourapp.com/terms/",
#         contact=openapi.Contact(email="contact@yourapp.com"),
#         license=openapi.License(name="Your License"),
#     ),
#     public=True,
# )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', UserList.as_view(), name='user_list'),
    path('user/<int:id>/', UserDetail.as_view(), name='user-detail'),
    # path('employee/', EmployeeList.as_view(), name='employee-list'),
    # path('employee/<int:id>/', EmployeeDetail.as_view(), name='employee-detail'),
    # path("events/", include(("events.urls", "events"))),
    
    # Swagger documentation URLs
    # path('swagger(?P<format>\.json|\.yaml)', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    # path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

