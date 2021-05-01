from flask import Flask
import sys
from dashboard import views


app = Flask(__name__)
app.register_blueprint(views.blueprint, url_prefix="/dashboard")


@app.route("/", methods=['GET'])
def root():
    return "Wellcome !!!"

if __name__ == '__main__':
    try:
        port = int(sys.argv[1])
    except (TypeError, IndexError):
        port = 8080
    app.run(debug=True, port=port)