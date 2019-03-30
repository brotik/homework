import os
import waitress
from flask import render_template, Flask, request

from app.lib_for_HW2 import total_rulons


def start():
    app = Flask(__name__)

    @app.route('/')
    def index():
        if not request.args:
            return render_template('index.html', user_input={})

        rolls_required = total_rulons('room_lenght', 'room_width', 'room_hight')
        return render_template('index.html', user_input=request.args, rolls_required=rolls_required)

    if os.getenv('APP_ENV') == 'PROD' and os.getenv('PORT'):
        waitress.serve(app, port=os.getenv('PORT'))
    else:
        app.run(port=9876, debug=True)


if __name__ == '__main__':
    start()
