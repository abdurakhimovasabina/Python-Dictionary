def get_active_users(users: dict[str, dict[str, bool | str]]) -> list[str]:

    active = []

    for name, info in users.items():
        if info.get("active"):
            active.append(name)
            
    return active

users = {
    "Ali": {"active": True, "email": "ali@mail.com"},
    "Vali": {"active": False, "email": "vali@mail.com"},
    "Soli": {"active": True, "email": "soli@mail.com"}
}
print(get_active_users(users))