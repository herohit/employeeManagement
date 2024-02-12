from django.contrib import admin
from django.urls import path , re_path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('login',views.login),
    re_path('signup',views.signup),
    re_path('logout',views.logout),
    path('',views.getRoutes,name='getRoutes'),
    path('api/', include('api.urls')),
]
