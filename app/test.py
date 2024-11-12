"""
The code provided simulates traffic in a system by performing login and logout actions
for a specified duration.
"""

import requests
import datetime

from app.schema import UserLogin
import time
import random
from app.utils import run_query


# utility function to get active users
def get_active_users(is_active):
    query = "SELECT fullname, email, password, role, location FROM users WHERE is_active=%s"
    return run_query(query, (is_active,), False)


# function to simulate traffic
def mock_traffic():
    start_time = datetime.datetime.now()
    end_time = start_time + datetime.timedelta(minutes=5)

    count = 1
    while datetime.datetime.now() < end_time:
        print("...")
        login_users(count)
        logout_users(count)
        count += random.randint(0, 4)
        time.sleep(5)


# function to simulate login actions for a specified number of users
def login_users(count):
    user_list = get_active_users(is_active=0)
    if user_list:
        for i in range(count + random.randint(0, 10)):
            _, email, password, _, _ = user_list[i]
            user = UserLogin(email=email, password=password)
            response = requests.post("http://localhost:8001/user/login", user.json())
            if response.status_code == 200:
                print("login")
            else:
                print("login error")


# function to simulate logout actions for a specified number of users
def logout_users(count):
    user_list = get_active_users(is_active=1)
    if user_list:
        for i in range(count + random.randint(0, 7)):
            _, email, password, _, _ = user_list[i]
            user = UserLogin(email=email, password=password)
            response = requests.post("http://localhost:8001/user/logout", user.json())
            if response.status_code == 200:
                print("logout")
            else:
                print("logout error")


if __name__ == '__main__':
    mock_traffic()
