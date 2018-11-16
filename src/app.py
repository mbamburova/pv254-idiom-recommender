from flask import Flask, Blueprint

from .config import app_config
from .models import db, ma
from .views.GeneratedQuestionView import generated_questions_blueprint
from .views.IdiomView import idioms_blueprint
from .views.UserView import users_blueprint
from .views.UserAnswerView import user_answers_blueprint


def create_app(env_name):
    app = Flask(__name__)

    app.config.from_object(app_config[env_name])

    db.init_app(app)
    ma.init_app(app)

    # BLUEPRINTS
    app.register_blueprint(generated_questions_blueprint)
    app.register_blueprint(idioms_blueprint)
    app.register_blueprint(users_blueprint)
    app.register_blueprint(user_answers_blueprint)

    @app.route('/', methods=['GET'])
    def index():
        return 'Congratulations! Your first endpoint is working'

    return app
