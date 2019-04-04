import os
import waitress
from flask import render_template, Flask, request

from app.lib_for_HW2 import total_rulons


def start():
    app = Flask(__name__)

    @app.route('/')
    def frontpage():
        room_length = request.args.get('room_length')
        room_widht = request.args.get('room_widht')
        room_height = request.args.get('room_height')

        if room_length and room_height and room_widht:
            rolls = total_rulons(float(room_length), float(room_widht), float(room_height))
            return render_template('index.html', title='Calculate wallpaper', total_rulons=rolls)
        return render_template('index.html', title='Calculate wallpaper')

    if os.getenv('APP_ENV') == 'PROD' and os.getenv('PORT'):
        waitress.serve(app, port=os.getenv('PORT'))
    else:
        app.run(port=9876, debug=True)

    app.run(port=9876, debug=True)


if __name__ == '__main__':
    start()
