import logging

from pydj import PyDJ
from pydj.di.globals import registry

DEBUG = True

if __name__ == '__main__':
    if DEBUG:
        logging.basicConfig(level=logging.DEBUG)

    # By default, PyDJ scans all modules in your project, which is not ideal!
    app = PyDJ(
        port=8085,
        modules=['glaucus']
    )

    if DEBUG:
        for info in registry:
            print(info)

    print(app.ctx.xml())
