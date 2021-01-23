from flask import Flask
from views.user import userbp
from views.main import mainbp

import os
app = Flask(__name__)
app.secret_key = os.urandom(24)
app.register_blueprint(userbp)
app.register_blueprint(mainbp)



if __name__ == '__main__':
    app.run(debug=True)
