class User:

    def __init__(self, name, username, id):
        self.name = name
        self.username = username
        self.id = id
        self.followers = 0
        self.following = 0

    def follow(self, user):
        self.following += 1
        user.followers += 1


user_1 = User("Dennis", "deedadey", 1004562)
user_2 = User("Afia", "afiakonadu", "2389910")

user_2.follow(user_1)

print(user_1.username)
print(f"Followers {user_1.followers}")
print(f"Following {user_1.following}")

print(f"\n{user_2.username}")
print(f"Followers {user_2.followers}")
print(f"Following {user_2.following}")