import time
import requests
from concurrent.futures import ThreadPoolExecutor

URLS = [
    "https://www.example.com",
    "https://www.example.org",
    "https://www.example.net",
    "https://www.example.edu",
]

def fetch_url(url):
    response = requests.get(url)
    return len(response.content)  # Return content size

def main():
    start_time = time.time()  # Start time for performance measurement
    with ThreadPoolExecutor(max_workers=len(URLS)) as executor:
        results = list(executor.map(fetch_url, URLS))

    end_time = time.time()  # End time for performance measurement
    print("Parallel Execution Time (ThreadPoolExecutor):", end_time - start_time)
    print("Content sizes:", results)  # Print content sizes for verification

if __name__ == "__main__":
    main()