from flask import Flask

from .config import app_config
from .models import db, ma

from.views.QuestionView import question_api as question_blueprint


def create_app(env_name):
    app = Flask(__name__)

    app.config.from_object(app_config[env_name])

    db.init_app(app)
    ma.init_app(app)

    app.register_blueprint(question_blueprint, url_prefix='/api/v1/questions')

    @app.route('/', methods=['GET'])
    def index():
        return 'Congratulations! Your first endpoint is workin'

    return app
