from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', include('buses.urls')),
    path('', include('customers.urls')),
    path('', include('accounts.urls')),
]
