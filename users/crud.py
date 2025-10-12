from users.schemas import CreateUser


def create_user(user_in: CreateUser) -> dict:
    user = user_in.model_dump()
    return {"success": True, "user": user}


def get_product(session, product_id):
    return None
