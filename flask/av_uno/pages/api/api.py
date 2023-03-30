from flask import Flask
from flask_login import LoginManager
from prisma import Prisma, register
from prisma.models import User
import uuid, hashlib, datetime



app = Flask(__name__)
app.config['AVPASS_CLIENT_ID'] = '64008b39-9a69-4a65-b54d-bff3081cb626'
app.config['AVPASS_CLIENT_SECRET'] = '271367673dc870f17dd253a8792b9d9b3ff76d252608d0906ac917e53ccfbaf3'

# Connect to the database and register it.
db = Prisma()
db.connect()
register(db)

# Define app
app = Flask(__name__,template_folder='pages/',static_folder='./assets/')
app.REMEMBER_COOKIE_DURATION = datetime.timedelta(days=30)
app.config["REMEMBER_COOKIE_DURATION"] = datetime.timedelta(days=30)

# Setup login manager and secret_key.
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

app.secret_key = hashlib.sha3_256(str(uuid.uuid4()).encode()).hexdigest()
@app.login_manager.user_loader
def load_user(_id):
    if _id is not None:
      user = User.prisma().find_first(where={'id': _id})
      return user
    else:
      return None

# Blueprint Registration

#BLUEPRINT IMPORTS

from api_routes.index import home_route
from auth.auth import auth_blueprint

#END OF BLUEPRINT IMPORTS

app.register_blueprint(home_route, url_prefix='/')
app.register_blueprint(auth_blueprint, url_prefix='/auth')

# END OF REGISTRATION

if __name__ == '__main__':
    app.run(debug=True, port=80)