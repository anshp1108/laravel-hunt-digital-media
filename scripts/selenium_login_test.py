#!/usr/bin/env python3
"""
Quick Selenium script to open the local Laravel login page, fill email and password
with random values, submit the form, wait briefly and exit.

Usage:
  # create virtualenv (optional)
  python3 -m venv .venv && source .venv/bin/activate
  pip install selenium webdriver-manager

  # run (headless by default)
  python scripts/selenium_login_test.py

Environment:
  TARGET_URL - optional, defaults to http://da.adlynk.in:8000
  HEADLESS   - set to '0' to see the browser window, defaults to headless

Note: This script uses Chrome via webdriver-manager. Ensure Chrome is installed.
"""
from __future__ import annotations

import os
import random
import string
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def random_email() -> str:
    local = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    return f"{local}@example.com"


def random_password() -> str:
    return ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=12))


def main() -> None:
    url = os.environ.get('TARGET_URL', 'http://da.adlynk.in:8000')
    headless = os.environ.get('HEADLESS', '1') != '0'

    print(f"Opening {url} (headless={headless})")

    options = webdriver.ChromeOptions()
    if headless:
        # Use new headless mode where available
        options.add_argument('--headless=new')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument('--window-size=1280,800')

    # Start Chrome with webdriver-manager provided binary
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    try:
        driver.get(url)
        time.sleep(1)  # allow page to load

        email_value = random_email()
        password_value = random_password()

        print(f"Filling email={email_value} password={password_value}")

        # Try common selectors from this project
        try:
            email_el = driver.find_element(By.ID, 'email')
        except Exception:
            # fallback to name
            email_el = driver.find_element(By.NAME, 'email_address')

        password_el = driver.find_element(By.ID, 'password')

        email_el.clear()
        email_el.send_keys(email_value)
        password_el.clear()
        password_el.send_keys(password_value)

        # Submit the form - click the submit button
        submit_btn = driver.find_element(By.CSS_SELECTOR, 'button[type=submit]')
        submit_btn.click()

        print('Form submitted — waiting 3s to observe any result...')
        time.sleep(3)

    finally:
        driver.quit()
        print('Done — driver quit')


if __name__ == '__main__':
    main()
