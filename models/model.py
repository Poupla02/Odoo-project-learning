from odoo import models, fields, api


class Commande(models.Model):
    _name = "gest_commande.commande"
    _description = "Commande"
    _rec_name = "date_commande"
    date_commande = fields.Date(string="Date", required=True)
    # time = fields.Float(string="Time", compute="_compute_time")
    ofc_in_time = fields.Float(string="Heure", digits=(12, 2), copy=False)
    quantite = fields.Integer(string="Quantité", required=True)
    user_id = fields.Many2one("res.partner", string="Client")
    vendeur = fields.Many2one("res.users", string="Vendeur")
    menu_id = fields.Many2one("gest_commande.menu")
    total = fields.Integer(string="Somme total", compute="sommeTotal")

    @api.onchange('quantite','menu_id')
    def sommeTotal(self):
        for rec in self:
            if rec.menu_id:
                test = rec.quantite * rec.menu_id.prix
                self.total = test
            # if rec.quantite and rec.menu_id:
            #     test = rec.quantite * rec.menu_id.prix
            #     # rec.total = test
            # else:
            #     pass


class Menu(models.Model):
    _name = "gest_commande.menu"
    _description = "Menu"
    _rec_name = "nom_plat"
    nom_plat = fields.Char(string="Nom du plat", required=True)
    prix = fields.Integer(string="Prix", required=False)
    description_plat = fields.Char(string="Description", required=False)
    commande_id = fields.One2many("gest_commande.commande", "menu_id")
