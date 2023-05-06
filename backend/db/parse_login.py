def create_mongodb_uri(server, port, username=None, password=None, auth_db=None):
    """
    Dado credenciais do MongoDB, retorna uma URI formatada corretamente para conexão.
    :param server: o host do servidor
    :param port: a porta em que o servidor se encontra
    :param username: (opcional) o nome de usuário
    :param password: (opcional) a senha do usuário
    :param auth_db: (opcional) o banco de dados de autenticação
    :return: a URI correamente formatada
    """
    if not username:
        return f"mongodb://{server}:{port}"
    else:
        return f"mongodb://{username}:{password}@{server}:{port}/?authMechanism=DEFAULT&authSource={auth_db}"
