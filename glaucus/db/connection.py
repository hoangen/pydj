class Connection:
    def __init__(self,
                 url: str = 'http://localhost',
                 port: int = 5432,
                 username: str = 'admin',
                 password: str = 'admin'
                 ) -> None:
        self.url = url
        self.port = port
        self.username = username
        self.password = password
