# object blueprint

class User:
    def __init__(self, username="guest", password="guest"):
        self.username = username    # attributes / properties
        self.password = password


user1 = User()
print(user1.username)
print(user1.password)

print("\n")

user2 = User("Captain", "helloworld")
print(user2.username)
password = user2.password
password_length = password.count('')
print("X" * password_length)
'''
# Help

help(user2)
                Get help with a blueprint of users2.

'''




'''
class PasswordLength:
    def __init__(self, user="guest", password="password") -> None:
        self.user = user
        self.password = password
        length = password.count('')
        encrypted_password = ("*" * length)


user1 = PasswordLength()

'''




'''
Attributes & Methods ;

'''

class life:
    def __init__(self, is_concious=False) -> None:
        self.is_concious = is_concious


ai = life(True)
print(ai.is_concious)

