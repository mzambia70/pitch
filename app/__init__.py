from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_uploads import UploadSet,configure_uploads,IMAGES  #type of file to upload
from flask_mail import Mail
from flask_simplemde import SimpleMDE

from flask_login import LoginManager



bootstrap = Bootstrap()
db = SQLAlchemy()
mail = Mail()
simple = SimpleMDE()


login_manager = LoginManager()
login_manager.session_protection = 'strong'  #provide diff security levels and setign it i strong 
login_manager.login_view = 'auth.login'
photos = UploadSet('photos',IMAGES)




def create_app(config_name):

    app = Flask(__name__)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Creating the app configurations

    app.config.from_object(config_options[config_name])

    # Initializing flask extensions
    bootstrap.init_app(app)
    app.config['SECRET_KEY'] ="SECRET_KEY"
    db.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    simple.init_app(app)


    # Registering the blueprint in our create app function
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')  #addin a prefix  to all the routes registered with the blueprint


    #configure UploadSet
    configure_uploads(app,photos)



    return app