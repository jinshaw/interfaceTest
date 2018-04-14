import requests
p={"mobile":"15858122395","code":"1234"}
r= requests.get("http://d.baiwandian.cn/login",params=p)
print(r.url)
print(r.history)