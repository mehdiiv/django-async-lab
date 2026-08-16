import asyncio
import time
import httpx
from rest_framework.response import Response
from django.http import JsonResponse
from asgiref.sync import sync_to_async
from rest_framework.views import APIView
from .services import (
    get_weather_sync,
    get_payment_sync,
    get_user_sync,
    get_orders_sync,
    get_orders_async,
    get_payment_async,
    get_user_async,
    get_weather_async,
    call_api_sync,
    call_api_async,
)
from .models import Task
from .services import get_tasks_sync


class SyncView(APIView):
    def get(self, request):
        start = time.perf_counter()

        time.sleep(2)
        operation_a = "A completed"

        time.sleep(2)
        operation_b = "B completed"

        time.sleep(2)
        operation_c = "C completed"

        elapsed = time.perf_counter() - start

        return Response({
            "operations": [
                operation_a,
                operation_b,
                operation_c,
            ],
            "elapsed_seconds": round(elapsed, 2),
        })

    
async def async_view(request):
    start = time.perf_counter()

    await asyncio.sleep(2)
    operation_a = "A completed"

    await asyncio.sleep(2)
    operation_b = "B completed"

    await asyncio.sleep(2)
    operation_c = "C completed"

    elapsed = time.perf_counter() - start

    return JsonResponse({
        "operations": [
            operation_a,
            operation_b,
            operation_c,
        ],
        "elapsed_seconds": round(elapsed, 2),
    })

async def operation_a():
    await asyncio.sleep(2)
    return "A completed"


async def operation_b():
    await asyncio.sleep(2)
    return "B completed"


async def operation_c():
    await asyncio.sleep(2)
    return "C completed"

async def async_sequential_view(request):
    start = time.perf_counter()

    result_a = await operation_a()
    result_b = await operation_b()
    result_c = await operation_a()

    elapsed = time.perf_counter() - start

    return JsonResponse({
        "operations": [
            result_a,
            result_b,
            result_c,
        ],
        "elapsed_seconds": round(elapsed, 2),
    })

async def async_concurrent_view(request):
    start = time.perf_counter()

    result = await asyncio.gather(
        operation_a(),
        operation_b(),
        operation_c(),
    )

    elapsed = time.perf_counter() - start

    return JsonResponse({
        "oprations": result,
        "elapsed_seconds": round(elapsed, 2),
    })

def external_sync_view(request):
    start = time.perf_counter()

    weather = get_weather_sync()
    payment = get_payment_sync()
    user = get_user_sync()
    orders = get_orders_sync()

    elapsed = time.perf_counter() - start

    return JsonResponse({
        "results": {
            "weather": weather,
            "payment": payment,
            "user": user,
            "orders": orders,
        },
        "elapsed_seconds": round(elapsed, 2),
    })


async def external_async_sequential_view(request):
    start = time.perf_counter()

    weather = await get_weather_async()
    payment = await get_payment_async()
    user = await get_user_async()
    orders = await get_orders_async()

    elapsed = time.perf_counter() - start

    return JsonResponse({
        "results": {
            "weather": weather,
            "payment": payment,
            "user": user,
            "orders": orders,
        },
        "elapsed_seconds": round(elapsed, 2),
    })

async def external_async_concurrent_view(request):
    start = time.perf_counter()

    weather, payment, user, orders = await asyncio.gather(
        get_weather_async(),
        get_payment_async(),
        get_user_async(),
        get_orders_async(),
    )

    elapsed = time.perf_counter() - start

    return JsonResponse({
        "results": {
            "weather": weather,
            "payment": payment,
            "user": user,
            "orders": orders,
        },
        "elapsed_seconds": round(elapsed, 2),
    })

async def fake_external_api(request):
    await asyncio.sleep(2)
    
    return JsonResponse({
        "message": "External API response",
        "status": "success",
    })

def http_sync_test(request):
    start = time.perf_counter()

    result1 = call_api_sync()
    result2 = call_api_sync()
    result3 = call_api_sync()
    result4 = call_api_sync()

    elapsed = time.perf_counter() - start

    return JsonResponse({
        "results": [
            result1,
            result2,
            result3,
            result4,
        ],
        "elapsed_seconds": round(elapsed, 2),
    })

async def http_async_concurrent_test(request):
    start = time.perf_counter()

    async with httpx.AsyncClient() as client:
        results = await asyncio.gather(
            call_api_async(client),
            call_api_async(client),
            call_api_async(client),
            call_api_async(client),
        )

    elapsed = time.perf_counter() - start

    return JsonResponse({
        "results": results,
        "elapsed_seconds": round(elapsed, 2),
    })

async def http_async_concurrent_test(request):
    start = time.perf_counter()

    async with httpx.AsyncClient() as client:
        results = await asyncio.gather(
            call_api_async(client),
            call_api_async(client),
            call_api_async(client),
            call_api_async(client),
        )

    elapsed = time.perf_counter() - start

    return JsonResponse({
        "results": results,
        "elapsed_seconds": round(elapsed, 2),
    })

async def http_async_sequential_test(request):
    start = time.perf_counter()

    async with httpx.AsyncClient() as client:
        result1 = await call_api_async(client)
        result2 = await call_api_async(client)
        result3 = await call_api_async(client)
        result4 = await call_api_async(client)

    elapsed = time.perf_counter() - start

    return JsonResponse({
        "results": [
            result1,
            result2,
            result3,
            result4,
        ],
        "elapsed_seconds": round(elapsed, 2),
    })

def database_sync_view(request):
    tasks = Task.objects.all()

    data = [
        {
            "id": task.id,
            "title": task.title,
            "created_at": task.created_at,
        }
        for task in tasks
    ]

    return JsonResponse({
        "tasks": data,
    })

async def database_async_view(request):
    tasks = await sync_to_async(
        get_tasks_sync
    )()

    return JsonResponse({
        "tasks": tasks,
    })


def blocking_view(request):
    start = time.perf_counter()

    time.sleep(5)

    elapsed = time.perf_counter() - start

    return JsonResponse({
        "type": "blocking",
        "message": "Finished after blocking sleep",
        "elapsed_seconds": round(elapsed, 2),
    })

async def non_blocking_view(request):
    start = time.perf_counter()

    await asyncio.sleep(5)

    elapsed = time.perf_counter() - start

    return JsonResponse({
        "type": "non-blocking",
        "message": "Finished after non-blocking sleep",
        "elapsed_seconds": round(elapsed, 2),
    })