# -*- coding: utf-8 -*-
# Copyright (c) 2017, sathishpy@gmail.com and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe import _

def set_cost_center(inv, method):
    if (inv.doctype == "Sales Invoice"):
        for item in inv.items:
            item.cost_center = frappe.db.get_value("Branch", inv.branch, "cost_center")
            item.warehouse = frappe.db.get_value("Branch", inv.branch, "finished_goods")
            print("Selling goods from warehouse {0} of {1}".format(item.warehouse, inv.branch))
    if (inv.doctype == "Journal Entry"):
        for account in inv.accounts:
            account.cost_center = frappe.db.get_value("Branch", inv.branch, "cost_center")
    if (inv.doctype == "Purchase Receipt"):
        for item in inv.items:
            item.cost_center = frappe.db.get_value("Branch", inv.branch, "cost_center")
            item.warehouse = frappe.db.get_value("Branch", inv.branch, "stores")
            print("Accepting goods to warehouse {0} of {1}".format(item.warehouse, inv.branch))
    if (inv.doctype == "Purchase Invoice"):
        for item in inv.items:
            item.cost_center = frappe.db.get_value("Branch", inv.branch, "cost_center")
