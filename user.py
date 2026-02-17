import hashlib

class User:

    def __init__(self, username=None, password=None, email=None, birthday=None):
        self.username = username
        self.password = self._encrypt_password(password)
        self.email = email
        self.birthday = birthday

    def __str__(self):
        return f"Username: {self.username}\nPassword: {self.password}\nemail: {self.email}\nDOB: {self.birthday}"

    def __repr__(self):
        return f"{self.__class__}({self.__dict__})"

    def __eq__(self, other):
        """Tests if two usernames are the same"""
        return self.username == other.username

    def _encrypt_password(self,password):
        password = password.encode('utf-8')
        return hashlib.sha256(password).hexdigest()


if __name__ == "__main__":
    pete = User("Peter", "password",
                "pete@some.com", "2005-01-01")
    print(pete)
    fred = User(username="Peter", password="password", email="fred@some.com", birthday="2/17/2006")
    print(pete == fred)
    #print(repr(pete))

    print(help(User))