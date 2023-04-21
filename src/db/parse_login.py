def create_mongodb_uri(server, port, username, password, auth_db):
    if not username:
        return f"mongodb://{server}:{port}"
    else:
        return f"mongodb://{username}:{password}@{server}:{port}/?authMechanism=DEFAULT&authSource={auth_db}"
