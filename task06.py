student = {
    'name': 'Ali',
    'age': 20,
    'status': 'Student'
}

poisk_key = input("Qanday kalit orqali ma`lumot qidiryabsiz? > ")



if poisk_key in student:
    print(student[poisk_key])

else:
    print("Topilmadi")