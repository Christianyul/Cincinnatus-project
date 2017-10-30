from app import create_app
# from flask_scss  import Scss
app = create_app('default')
# Scss(app, static_dir='app/static', asset_dir='app/static')
app.run()
