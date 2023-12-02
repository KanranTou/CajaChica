from utils.db import db


class CajaChica(db.Model):
    __tablename__ = "caja_chica"
    id_caja_chica = db.Column(db.Integer, primary_key=True)
    id_predio = db.Column(db.Integer, db.ForeignKey("predio.id_predio"))
    id_personal = db.Column(db.Integer, db.ForeignKey("personal.id_personal"))
    periodo = db.Column(db.String)
    importe = db.Column(db.Double)
    id_estado = db.Column(db.Integer, db.ForeignKey("estado.id_estado"))
    fecha_registro = db.Column(db.Date)
    casas_nohabitadas = db.Column(db.Integer)

    def __init__(
        self,
        id_caja_chica,
        id_predio,
        id_personal,
        periodo,
        importe,
        id_estado,
        fecha_registro,
        casas_nohabitadas,
    ):
        self.id_caja_chica = id_caja_chica
        self.id_predio = id_predio
        self.id_personal = id_personal
        self.periodo = periodo
        self.importe = importe
        self.id_estado = id_estado
        self.fecha_registro = fecha_registro
        self.casas_nohabitadas = casas_nohabitadas
