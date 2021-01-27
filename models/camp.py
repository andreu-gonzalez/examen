from odoo import models, fields, api
from random import choice
from odoo.exceptions import ValidationError
from datetime import date, datetime
class camp(models.Model):
    _name = 'empresa.camp'
    _description = 'empresa.camp'
    name = fields.Date(string="campaña",required=True)
    fecha= fields.Datetime(default=datetime.now())
    cantidad = fields.Float(string="cantidad",default=0.00)
    socio = fields.Many2one("empresa.socios")
    producto = fields.Many2one("empresa.productos")

    def eliminarelhistorial(self):
        self.ensure_one()
        for rec in self.socio:
            rec.unlink()
        return True   

    
   
    def saldo(self):
        self.ensure_one()
        suma = 0
        for i in self.producto:
            suma += i.productos.precio*i.cantidad
        self.socio.saldo = suma 

    def kilosn(self):
        self.ensure_one()
        suma=0
        for rec in self.producto:
            suma+=rec.productos.kilo
        self.producto.kilo=suma    
        return True         