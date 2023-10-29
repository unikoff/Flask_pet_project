from flask_login import UserMixin
import requests
import json


def random_active():
    url = "https://www.boredapi.com/api/activity"
    try:
        response = requests.request("GET", url)
        status_code = response.status_code
        if status_code == 200:
            result = json.loads(response.text)
            print(result)
    except:
        return "Error connect"
    return result['activity']


class Db_plus(UserMixin):

    def __init__(self, db, table):
        self.db = db
        self.table = table
        self.active = True

    def find_id(self, user_id):
        self.__user = self.db.session.execute(self.db.select(self.table).
                                              filter_by(id=user_id)).scalar_one()
        return self

    def find_user(self, user_email):
        if self.exist_user(user_email):
            self.__user = self.db.session.execute(self.db.select(self.table).
                                                  filter_by(email=user_email)).scalar_one()
            return self

    def new_user(self, username, email, password):
        try:
            user = self.table(username=username, email=email, password=password)
            self.db.session.add(user)
            self.db.session.flush()
            self.db.session.commit()
        except:
            return False
        return True

    def exist_user(self, user_email):
        return self.db.session.query(self.table).filter_by(email=user_email).first() is not None

    def get_id(self):
        return str(self.__user.id)

    def get_name(self):
        return str(self.__user.username)

    def get_email(self):
        return str(self.__user.email)

    def get_psw(self):
        return str(self.__user.password)


if __name__ == '__main__':
    print(random_active())