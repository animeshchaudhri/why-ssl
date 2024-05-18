
# Captive Portal Detection and Login Script

This script provides functionality to detect captive portals and log in to them using provided credentials. It uses the requests library in Python to make HTTP requests.

## Requirements

Ensure you have the requests library installed. You can install it using pip:

```bash
pip install requests
```

## Functions
```detect_captive_portal(url)```

Detects if a given URL is behind a captive portal.


**Parameters:**

- `url` (str): The URL to check for a captive portal.

**Returns:**

A tuple containing a boolean and a string. The boolean indicates if a captive portal was detected. If a captive portal is detected, the string contains the redirect URL. Otherwise, the string is None.

**Example:**
```python
is_captive_portal, captive_portal_url = detect_captive_portal("http://google.com")
if is_captive_portal:
   print("Captive portal detected. Redirect URL:", captive_portal_url)
else:
   print("No captive portal detected.")
```
### `login_to_captive_portal(captive_portal_url, username, password)`

Attempts to log in to the detected captive portal using the provided credentials.

**Parameters:**

- `captive_portal_url` (str): The URL of the captive portal's login page.
- `username` (str): The username for the captive portal.
- `password` (str): The password for the captive portal.

**Returns:**

None

**Example:**

```python
login_to_captive_portal("http://example.com/login", "your_username", "your_password")
url_to_test = "http://google.com"
username = "your_username"
password = "your_password"

is_captive_portal, captive_portal_url = detect_captive_portal(url_to_test)
if is_captive_portal:
    print("Captive portal detected. Redirect URL:", captive_portal_url)
    login_to_captive_portal(captive_portal_url, username, password)
else:
    print("No captive portal detected.")

```