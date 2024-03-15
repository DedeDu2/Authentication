class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class Authentication:
    def __init__(self):
        self.users = {}

    def register(self, username, password):
        self.users[username] = User(username, password)

    def login(self, username, password):
        if username in self.users and self.users[username].password == password:
            return True
        else:
            return False

# Example usage:
auth = Authentication()
auth.register("user1", "password123")
authenticated = auth.login("user1", "password123")
print("Authenticated:", authenticated)
