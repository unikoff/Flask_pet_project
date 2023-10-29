from flask_login import UserMixin


class UserLog(UserMixin):
    def __init__(self, username, password, email):
        self.active = True
        self.anonim = False
        self.username = username
        self.password = password
        self.email = email

    def user_from(self):
        return self.email

