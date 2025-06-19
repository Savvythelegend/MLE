import requests

url = "https://example.com/some-protected-endpoint"  # change to target URL

headers = {
    "User-Agent": "Mozilla/5.0",  # mimic a browser
    "Cookie": "user_fingerprint_v2=681da1db3a601913f97daa5e29ad3b030da5cd196a45b56b03be2833e219da17; testcookie=1; _iidt=yiuHAttHxgLiK47bHJsCmZqqOzctcgMAXgzjAjeC+GD1RNGw21aqrBBdIp6anSYOmDVAwP3tuYZXUg==; prefill_data_v1=FnUoHaEufVkJnlMdZ/y1XvGuBq7zVKQQ11UCWMwsu1lf1foMyciSm4qpRcy+2094R8Qx4Ho+d00E+Iydp5N55SPk6xSLqGoCPH3r0K/YyJ4veWsogCAGZWtwTZ1JrGMM"
}

response = requests.get(url, headers=headers)

print(response.status_code)
print(response.text)
