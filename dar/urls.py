from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('user.urls')),
    path('category/', include('product.urls')),
    path('order/', include('order.urls')),
    path('', include('main.urls')),

]
