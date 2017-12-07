# -*- coding: utf-8 -*-
# Copyright (c) 2017, Sathisha Poojary and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class AutoVehicle(Document):
	def autoname(self):
		self.name = self.vehicle_model + "-" + self.vehicle_no
