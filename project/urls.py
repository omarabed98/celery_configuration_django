from django.contrib import admin
from django.urls import path

from currency.views import mass_email_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mass_email_view),
]
