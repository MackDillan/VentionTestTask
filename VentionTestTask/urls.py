from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('auth/', include('djoser.urls')),
    #path('auth/token', obtain_auth_token, name='token'),
    #path('auth/token/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('', include('ApplicationTask.urls')),

]
