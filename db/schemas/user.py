def user_schema(user)-> dict:
    return{ "_id": str(user["_id"]),
            "username": user["username"],
            "email": user["email"]}