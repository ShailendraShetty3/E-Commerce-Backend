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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', UserListCreateView.as_view(), name='user-list-create'),
    path('users/<int:id>/', UserDetail.as_view(), name='user-detail')
]
