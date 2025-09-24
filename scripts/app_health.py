#!/usr/bin/env python3

import requests
from datetime import datetime

APP_URL = "http://localhost:4499"
TIMEOUT = 5

def check_app():
    try:
        response = requests.get(APP_URL, timeout=TIMEOUT)
        if response.status_code == 200:
            print(f"{datetime.now()} - Application is UP ✅  (Status: {response.status_code})")
        else:
            print(f"{datetime.now()} - Application is DOWN ❌  (Status: {response.status_code})")
    except requests.exceptions.RequestException as e:
        print(f"{datetime.now()} - Application is DOWN ❌  (Error: {e})")

if __name__ == "__main__":
    check_app()
