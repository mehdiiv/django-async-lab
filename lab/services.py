import asyncio
import time
import requests
import httpx
from .models import Task


FAKE_API_URL = "http://127.0.0.1:8000/api/fake-api/"

def get_weather_sync():
    time.sleep(2)

    return {
        "service": "Weather API",
        "status": "success",
    }


def get_payment_sync():
    time.sleep(2)

    return {
        "service": "Payment API",
        "status": "success",
    }


def get_user_sync():
    time.sleep(2)

    return {
        "service": "User API",
        "status": "success",
    }


def get_orders_sync():
    time.sleep(2)

    return {
        "service": "Orders API",
        "status": "success",
    }


async def get_weather_async():
    await asyncio.sleep(2)

    return {
        "service": "Weather API",
        "status": "success",
    }


async def get_payment_async():
    await asyncio.sleep(2)

    return {
        "service": "Payment API",
        "status": "success",
    }


async def get_user_async():
    await asyncio.sleep(2)

    return {
        "service": "User API",
        "status": "success",
    }


async def get_orders_async():
    await asyncio.sleep(2)

    return {
        "service": "Orders API",
        "status": "success",
    }

def get_external_api_sync():
    response = requests.get(
        "https://httpbin.org/delay/2",
        timeout=5,
    )

    response.raise_for_status()

    return response.json()


def call_api_sync():
    response = requests.get(
        FAKE_API_URL,
        timeout=10,
    )

    response.raise_for_status()

    return response.json()

async def call_api_async(client):
    response = await client.get(
        FAKE_API_URL,
        timeout=10,
    )

    response.raise_for_status()

    return response.json()

from .models import Task


def get_tasks_sync():
    return list(
        Task.objects.values(
            "id",
            "title",
            "created_at",
        )
    )