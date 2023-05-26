from typing import List

from pydj.di.application_context import ApplicationContext


class PyDJ:
    def __init__(self, port: int = 8080, modules: List[str] = ['app']):
        self.port = port
        self.ctx = ApplicationContext(modules)

        self.run()

    def run(self):
        print(f'running server at http://127.0.0.1:{self.port}')
        print(f'happy coding...')
