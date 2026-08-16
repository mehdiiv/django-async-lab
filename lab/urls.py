from django.urls import path

from .views import (
    SyncView,
    async_view,
    async_concurrent_view,
    async_sequential_view,
    external_async_sequential_view,
    external_async_concurrent_view,
    external_sync_view,
    fake_external_api,
    http_sync_test,
    http_async_sequential_test,
    http_async_concurrent_test,
    database_async_view,
    blocking_view,
    non_blocking_view,
    )


urlpatterns = [
    path("sync/", SyncView.as_view()),
    path("async/", async_view),
    path("async/sequential/", async_sequential_view),
    path("async/concurrent/", async_concurrent_view),
    path(
        "external/sync/",
        external_sync_view,
    ),

    path(
        "external/async/sequential/",
        external_async_sequential_view,
    ),

    path(
        "external/async/concurrent/",
        external_async_concurrent_view,
    ),
    path("fake-api/", fake_external_api),
    path("http/test/sync/", http_sync_test),
    path(
    "http/test/async/sequential/",
    http_async_sequential_test,
    ),
    path(
    "http/test/async/concurrent/",
    http_async_concurrent_test,
    ),
    path(
    "database/async/",
    database_async_view,
    ),
    path("blocking/", blocking_view),
    path("non-blocking/", non_blocking_view),
]