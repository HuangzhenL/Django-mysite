from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('show.urls')),  # 使用include,将不同app的url单独配置
]
