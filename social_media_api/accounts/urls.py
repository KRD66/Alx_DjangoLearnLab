from django.contrib import admin
from django.urls import path,include
from .views import RegisterView, LoginView,UserViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'users', UserViewSet)  # Handles user-related operations


urlpatterns =  [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('unfollow/<int:user_id>/', UserViewSet.as_view({'post': 'unfollow'}), name='unfollow-user'),
    path('follow/<int:user_id>/', UserViewSet.as_view({'post': 'follow'}), name='follow-user'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('api/', include('posts.urls'))
    
    
]
