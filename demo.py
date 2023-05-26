from pydj import PyDJ

if __name__ == '__main__':
    # By default, pydj scans components in 'app' module
    app = PyDJ(
        port=8085,
        modules=['glaucus']
    )

    print(app.ctx)
