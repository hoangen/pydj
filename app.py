from pydj.di.context import Context


class PyDJ:
    def __init__(self, port=150988):
        self.port = port
        self.ctx = Context()
        self.ctx.register_group()

    def run(self):
        print(f'running server at http://127.0.0.1:{self.port}')
        print(f'happy coding...')
        pass


if __name__ == '__main__':
    app = PyDJ()

    app.run()
