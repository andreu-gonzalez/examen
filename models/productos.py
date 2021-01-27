from odoo import models, fields, api
from random import choice
from odoo.exceptions import ValidationError

class productos(models.Model):
    _name = 'empresa.productos'
    _description = 'empresa.productos'
    _sql_constraints = [('productos_name_uniq','UNIQUE (name)','No puede haber dos socios con el mismo identificador'),]
    name = fields.Char(string="nombre", required=True, index=True,help="nombre")  
    descripcion = fields.Char(string="decripcion", required=True, index=True,help="descripcion")  
    precio = fields.Float(string="precio",help="saldo del socio")
    kilostotales = fields.Float(string="kilos",help="saldo del socio",default=0.00,readonly=True)
    pro = fields.One2many("empresa.camp","producto", string="Registro")
    @api.constrains("kilototales")
    def eliminarelkilos(self):
        self.ensure_one()
        for rec in self.kilostotales:
            rec.unlink()
        return True    


    @api.constrains("precio")
    def validadorprecio(self):
        if self.precio <=0:
            raise ValidationError("El precio tiene que ser mayor que 0")
        

   