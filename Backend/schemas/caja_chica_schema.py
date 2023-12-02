from utils.ma import ma
from marshmallow import fields


class CajaChicaSchema(ma.Schema):
    id_caja_chica = fields.Integer()
    id_predio = fields.Integer()
    id_personal = fields.Integer()
    periodo = fields.String()
    importe = fields.Float()
    id_estado = fields.Integer()
    fecha_registro = fields.Date()
    casas_nohabitadas = fields.Integer()
