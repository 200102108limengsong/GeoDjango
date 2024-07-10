from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app_test1/', include('app_test1.urls')),
    path('', include('app_test1.urls')),  # 将根路径映射到应用的 URL 配置
]
