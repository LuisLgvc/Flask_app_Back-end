from api import init_app

if __name__ == '__main__':
    api = init_app()
    api.run(debug=True)