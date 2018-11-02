from src.app import create_app

if __name__ == '__main__':
    env_name = 'production'
    app = create_app(env_name)
    app.run()
