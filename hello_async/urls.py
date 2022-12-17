from django.contrib import admin
from django.urls import path

from hello_async.views import index, async_view, sync_view, smoke_some_meats, burn_some_meats


urlpatterns = [
    path("admin/", admin.site.urls),
    path("smoke_some_meats/", smoke_some_meats),
    path("burn_some_meats/", burn_some_meats),
    path("async/", async_view),
    path("sync/", sync_view),
    path("", index),
]
