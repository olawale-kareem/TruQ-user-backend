from django.urls import path
from .views import (SignUpView, UsersListView, LoginAPIView,
                    LogoutAPIView, LogoutAllUsersView, )

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='register-user'),
    path('users/', UsersListView.as_view(), name='all-users'),
    path('login/', LoginAPIView.as_view(), name='login-user'),
    path('logout/', LogoutAPIView.as_view(), name='logout-user'),
    path('logout-all-users/', LogoutAllUsersView.as_view(), name='logout-all-users'),

]
