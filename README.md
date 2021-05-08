# Flask-blog
Flask-blog is a web application created with Python3 and FLask framework following Corey Schafer's Flask tutorial on [Youtube](https://www.youtube.com/playlist?list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH).

## Installation
- Go to Flask-blog directory, setup a virtual environment, activate it and run:
```
pip install -r requirements.txt
```

- You will also need to create settings.py in Flask-blog directory and add some configuration values in order to run the application:
```python
SECRET_KEY = 'your_secret_key'  # read further
SQLALCHEMY_DATABASE_URI = 'path_to_your_db'  # e.g. 'sqlite:///site.db'
MAIL_SERVER = 'your_mail_server'  # e.g. 'smtp.gmail.com'
MAIL_PORT = your mail port  # e.g. 465
MAIL_USE_SSL = True  # if required
MAIL_USE_TLS = True  # if required
MAIL_USERNAME = 'your_username'
MAIL_PASSWORD = 'your_password'
```

- To create your SECRET_KEY open Python shell in a command-line and run this:
```python
import secrets
secrets.token_hex(16)
```
Save the key and add it to settings.py

- To create a new db file open Python shell in a command-line from Flask-blog directory, and enter the following:
```python
from flaskblog import db
from flaskblog.models import User, Post
from flaskblog import create_app

app = create_app()
app.app_context().push()
db.create_all()
```

## Run
- Run the application:
```
python run.py
```

or by exporting flaskblog to FLASK_APP in a command-line:
```
export FLASK_APP=flaskblog
flask run
```
