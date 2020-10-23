from django.urls import path
from . import views  # 可引用同级目录中的views.py
urlpatterns = [
    path('', views.home, name='home'),  # '' 表示根目录 http://127.0.0.1:8000/
    path('user/', views.user, name='user'),  # views.XXX 在views.py中定义XXX函数进行前端配置
]
