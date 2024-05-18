import requests

# Define the URL
url = "https://192.168.100.1:6082/php/uid.php?vsys=1&rule=7&token=Bg0QBiH3Rhsj1mhfC8YokLyVguQ"

# Define the headers
headers = {
    "Host": "192.168.100.1:6082",
    "Cache-Control": "max-age=0",
    "Sec-Ch-Ua": '"Not-A.Brand";v="99", "Chromium";v="124"',
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": '"Windows"',
    "Upgrade-Insecure-Requests": "1",
    "Origin": "https://192.168.100.1:6082",
    "Content-Type": "application/x-www-form-urlencoded",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.6367.118 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-User": "?1",
    "Sec-Fetch-Dest": "document",
    "Referer": "https://192.168.100.1:6082/php/uid.php?vsys=1&rule=7&token=Bg0QBiH3Rhsj1mhfC8YokLyVguQ",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
    "Priority": "u=0, i",
    "Connection": "close"
}

# Define the data
data = {
    "inputStr": "",
    "escapeUser": "@,
    "preauthid": "",
    "user": "@",
    "passwd": "#",
    "ok": "Login"
}

# Define the cookies
cookies = {
    "SESSID": "f4MBAWZG6BGyzDHYAwmmAg=="
}

# Send the POST request
response = requests.post(url, headers=headers, cookies=cookies, data=data, verify=False)  # `verify=False` to ignore SSL warnings

# Print the response
print(response.status_code)
print(response.text)
