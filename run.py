from app import create_app
# from flask_scss  import Scss
from flaskext.auth import Auth


app = create_app('default')
auth = Auth(app)
# Scss(app, static_dir='app/static', asset_dir='app/static')

app.run()
