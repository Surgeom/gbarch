from main import Application
from urls import routes
from frontcontrollers import secret_front, other_front

app = Application(routes, [secret_front, other_front])

# gunicorn run:app
