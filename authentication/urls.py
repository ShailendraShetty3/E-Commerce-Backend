# from django.urls import path
# from .views import UserListCreateView, UserRetrieveUpdateDestroyView, TokenPairView, TokenRefreshExtendedView

# urlpatterns = [
#     path('users/', UserListCreateView.as_view(), name='user-list-create'),
#     path('users/<int:pk>/', UserRetrieveUpdateDestroyView.as_view(), name='user-retrieve-update-destroy'),
#     # path('token/', TokenPairView.as_view(), name='token_obtain_pair'),
#     # path('token/refresh/', TokenRefreshExtendedView.as_view(), name='token_refresh'),
# ]





from django.contrib import admin
from django.urls import path, include
from authentication.views import UserRegistrationView
urlpatterns = [
    path('register/', UserRegistrationView.as_view()),
]
