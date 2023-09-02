from django.contrib import admin
from django.urls import path
from currency.views import my_view, wallet, add
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", my_view, name="home"),
    path("wallet/", wallet, name="wallet"),
    path("add/", add, name="add"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
