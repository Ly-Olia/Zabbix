"""
This code defines a RESTful API with three routes
to handle user signup, login, and logout requests.
"""

from fastapi import FastAPI, Body, HTTPException, status
from fastapi.openapi.models import Response

from app.schema import User, UserLogin
from app.utils import run_query, check_user, set_active

app = FastAPI()


# Define a POST route for user signup
@app.post("/user/signup", tags=["user"], status_code=status.HTTP_200_OK)
def user_sighup(user: User = Body(default=None)):
    try:
        # SQL query to insert a new user into the database
        sql = """INSERT INTO users (fullname, email, password, role, location)
                     VALUES (%s, %s, %s, %s, %s)"""
        val = (user.fullname, user.email, user.password, user.role.value, user.location.value)
        run_query(sql, val, is_update=False)
        return user.json()
    except Exception as error:
        # If an error occurs during the signup process, return a JSON response with an error message and status code 500
        return Response(content={"error": str(error)}, media_type="application/json",
                        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Define a POST route for user login
@app.post("/user/login", tags=["user"], status_code=status.HTTP_200_OK)
def user_login(user: UserLogin = Body(default=None)):
    # check if the user exists in the system
    if check_user(user):
        # set the user's status as active
        set_active(user, True)
        return user.json()
    else:
        # If the user credentials are invalid, raise an HTTPException with a 403 Forbidden status code and error message
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail={"error": "Invalid login details!"})


# Define a POST route for user logout
@app.post("/user/logout", tags=["user"], status_code=status.HTTP_200_OK)
def user_logout(user: UserLogin = Body(default=None)):
    if check_user(user):
        # set the user's status as inactive
        set_active(user, False)
        return user.json()
    else:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail={"error": "Logout failed"})
