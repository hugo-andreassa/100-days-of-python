class User:

    def __init__(self, id: int, username: str):
        print("Creating new user...")
        self.id = id
        self.username = username


user_1 = User(5, "Hugo")
print(user_1)
