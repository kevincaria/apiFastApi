from typing import List

def user_schema(user)-> dict:
    return{ "_id": str(user["_id"]),
            "username": user["username"],
            "email": user["email"]}

def users_schema(users) -> List:
    return [user_schema(user) for user in users]