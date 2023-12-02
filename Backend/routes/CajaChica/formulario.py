from flask import (
    Blueprint,
    render_template as rt,
    request,
    redirect,
    url_for,
    make_response,
    jsonify,
)
from models.caja_chica import CajaChica
from schemas.caja_chica_schema import CajaChicaSchema
from utils.db import db
from utils.id import formatear_id
from utils.json import model_to_dict
from datetime import datetime

cajachica = Blueprint("cajachica", __name__, url_prefix="/cajachica")


# Crear una nueva caja chica
@cajachica.route("/crear", methods=["POST"])
def crear_caja_chica():
    caja_chica_schema = CajaChicaSchema()

    try:
        data = request.json
        nueva_caja_chica = CajaChica(**data)

        # Agregar la nueva caja chica a la base de datos
        db.session.add(nueva_caja_chica)
        db.session.commit()

        return caja_chica_schema.jsonify(nueva_caja_chica), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 400


# Obtener todas las cajas chicas
@cajachica.route("/obtener", methods=["GET"])
def obtener_todas_cajas_chicas():
    caja_chica_schema = CajaChicaSchema(many=True)
    cajas_chicas = CajaChica.query.all()

    return caja_chica_schema.jsonify(cajas_chicas), 200


# Obtener una caja chica por su ID
@cajachica.route("/formulario/<int:id_caja_chica>", methods=["GET"])
def obtener_caja_chica_por_id(id_caja_chica):
    caja_chica_schema = CajaChicaSchema()
    caja_chica = CajaChica.query.get(id_caja_chica)

    if caja_chica:
        return caja_chica_schema.jsonify(caja_chica), 200
    else:
        return jsonify({"mensaje": "Caja chica no encontrada"}), 404
