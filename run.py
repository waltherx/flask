from flask import Flask
from flask_cors import CORS
 
from route import phone
from route import enfermedad
from route import alergia
from route import persona
from route import hospital
from route import siniestro

app = Flask(__name__)

#CORS(app, resources={"*": {"origins": "http://localhost:9300"}})

def page_not_found(error):
    return "<h1>Pagina no encontrada</h1>", 404


if __name__ == "__main__":
    # Blueprints
    app.register_blueprint(phone.PhoneApi, url_prefix="/api/phone")
    app.register_blueprint(alergia.AlergiaApi, url_prefix="/api/alergia")
    app.register_blueprint(enfermedad.EnfermedadApi, url_prefix="/api/enfermedad")
    app.register_blueprint(persona.PersonaApi, url_prefix="/api/persona")
    app.register_blueprint(hospital.HospitalApi, url_prefix="/api/hospital")
    app.register_blueprint(siniestro.SiniestroApi, url_prefix="/api/siniestro")
    # Error handlers
    app.register_error_handler(404, page_not_found)

    app.run(debug=True)