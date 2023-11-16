from dotenv import load_dotenv
import os

load_dotenv()


def postgresql():
    return f"{os.getenv('config')}://{os.getenv('user')}:{os.getenv('password')}@localhost:5432/"