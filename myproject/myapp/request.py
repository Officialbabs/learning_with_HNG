import requests
r = requests.get("https://api.github.com/users/Officialbabs")
data = r.json()
for k,v in data.items():
    print(f"key:{k}, value: {v}")
g = requests.get("http://hngix.slack.com/api/search/users?slack_name= Oluwasegun Babalola&track=backend/")
# data = g.json()
# for i,j in data.itmes():
#     print(f"keys : {i} value: {j}")
# "https://api.hngix.slack.com/team/U05RBE77YP8"
print(g.content)