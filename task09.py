users = [
  {"id": 1, "active": True},
  {"id": 2, "active": True},
]

for i in users:
    if i['active'] == True:
        i["active"] = False

print(users)