
from flask_cors import CORS
from Application.app import app

from Application.patient_routes import app2
from Application.routes import app1

app.register_blueprint(app1)
app.register_blueprint(app2)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

if __name__ == "__main__":
    app.run(debug=True)