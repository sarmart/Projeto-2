class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def str(self, username, password):
        return self.username == username and self.password == password

