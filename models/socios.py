from odoo import models, fields, api
from random import choice
from odoo.exceptions import ValidationError
from datetime import datetime, date
class socios(models.Model):
    _name = 'empresa.socios'
    _description = 'empresa.socios'
    _sql_constraints = [('socios_name_uniq','UNIQUE (name)','No puede haber dos socios con el mismo identificador'),]
    soci_id = fields.Integer(string="socio_id", required=True, index=True,help="id del socio")  
    name = fields.Char(string="nombre",required=True,help="nombre del socio")
    apellidos = fields.Char(string="apellidos",required=True,help="apellidos del socio")
    dni = fields.Char(string="DNI", required=True)
    foto = fields.Binary(string="Foto", required=False)
    telf = fields.Char(string="Teléfono", size=9)
    email = fields.Char(string="Email", required=True)
    saldo = fields.Float(string="saldo",help="saldo del socio",readonly=True)
    fecha = fields.Date(string="Fecha",default=date.today())
    facturas = fields.One2many("empresa.camp","socio", string="Registro")
    @api.constrains("dni")
    def validoDNI(self):
        if len(self.dni)!=9:
            raise ValidationError("El DNI debe tener 9 caracteres")
        else:
            try:
                n=int(self.dni[:-1])
            except ValueError:
                raise ValidationError("Los primeros 8 dígitos deben ser números")

            palabra='TRWAGMYFPDXBNJZSQVHLCKE'

            if self.dni[-1].upper() == palabra[n%23]:
                return True
            else:
                
                raise ValidationError("La letra no coincide con el DNI")
    @api.constrains("telf")
    def valdartlf(self):
       if len(self.telf)!=9:
           raise ValidationError("tiene que ser de 9")


    @api.constrains("email")
    def _comprobarEmail(self):
        if "@" and "." not in self.email:
            raise ValidationError("El email no es correcto. Debe contener al menos @ y .")    