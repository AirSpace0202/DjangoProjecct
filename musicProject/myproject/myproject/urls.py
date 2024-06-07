from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', include('loginapp.urls')),  # 映射loginapp的url
    path('musicapp/', include('musicapp.urls')),
    path('', include('loginapp.urls')),  # 默认登录页面
]