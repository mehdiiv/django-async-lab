import time
import requests
from concurrent.futures import ThreadPoolExecutor


BASE_URL = "http://127.0.0.1:8000/api"


def send_request(url):
    start = time.perf_counter()

    response = requests.get(url)

    elapsed = time.perf_counter() - start

    return {
        "url": url,
        "status": response.status_code,
        "elapsed": round(elapsed, 2),
    }


def run_test(endpoint):
    url = f"{BASE_URL}/{endpoint}/"

    print(f"\nTesting: {url}")

    start = time.perf_counter()

    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = [
            executor.submit(send_request, url)
            for _ in range(5)
        ]

        results = [
            future.result()
            for future in futures
        ]

    total = time.perf_counter() - start

    for result in results:
        print(result)

    print(f"Total time: {total:.2f}s")


run_test("blocking")
run_test("non-blocking")