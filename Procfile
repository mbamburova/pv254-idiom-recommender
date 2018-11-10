web: gunicorn 'src.app:create_app("production")'
release: python migrate.py db upgrade
