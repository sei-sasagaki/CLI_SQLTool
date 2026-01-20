from db_config import User

print("""
===== Welcome to CRM Application =====
[S]how: Show all users info
[A]dd: Add new user
[Q]uit: Quit The Application
======================================
""")

while True:
    cmd = input("\nYour command > ")  # コマンドを受け取る

    if cmd == "S":  # ユーザーの一覧表示
        users = User.select()
        for user in users:
            print(f"Name: {user.name} Age: {user.age}")
    elif cmd == "A":  # 新規ユーザーの追加
        new_name = input("New user name > ")
        new_age = int(input("New user age > "))
        new_user = User(name=new_name, age=new_age)
        new_user.save()
        print(f"Add new user: {new_name}")
    elif cmd == "Q":  # 終了
        print("Bye!")
        break
    else:
        print(f"{cmd.lower()}: command not found")
