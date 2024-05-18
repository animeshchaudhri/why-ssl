import requests

def detect_captive_portal(url):
    try:
        response = requests.get(url, allow_redirects=False, verify=True)
        if response.status_code == 302 or response.status_code == 307:
            # Captive portal detected
            return True, response.headers['Location']
        else:
            # No captive portal detected
            return False, None
    except requests.RequestException as e:
        print("Error:", e)
        return False, None

def login_to_captive_portal(captive_portal_url, username, password):
    login_url = captive_portal_url  # Assuming the login form is directly at the captive portal URL

    # Form data to be submitted
    payload = {
        "user": 2210991964,
        "passwd": "nXwLTpf6",
        "ok": "Login"
    }

    try:
        # Send POST request with login credentials
        response = requests.post(login_url, data=payload)
        
        # Check if login was successful (you may need to adjust this based on the actual response)
        if response.status_code == 200 and "Welcome" in response.text:
            print("Login successful!")
        else:
            print("Login failed. Check your credentials or the portal configuration.")
    except requests.RequestException as e:
        print("Error:", e)

# Example usage
url_to_test = "http://google.com"
username = "@"
password = "@"

is_captive_portal, captive_portal_url = detect_captive_portal(url_to_test)

if is_captive_portal:
    ans=captive_portal_url[ 0:captive_portal_url.find("=&url=http://google.com")]
    print("Captive portal detected. Redirect URL:", ans)
    login_to_captive_portal(ans, username, password)
else:
    print("No captive portal detected.")