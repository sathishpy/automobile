# -*- coding: utf-8 -*-
# Copyright (c) 2017, Sathisha Poojary and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from datetime import datetime
from datetime import timedelta

class AutoVehicle(Document):
	def autoname(self):
		self.name = self.vehicle_model + "-" + self.chassis_number

	def add_dealer_services(self):
		service_types = frappe.db.sql("select name, expiry_days from `tabAuto Service Type` where expiry_days != 0", as_dict=True)
		for service_type in service_types:
			service_item = self.append("available_services", {})
			service_item.service_type = service_type.name
			sale_date = datetime.strptime(self.sale_date, "%Y-%m-%d")
			service_item.expiry_date = sale_date + timedelta(days=service_type.expiry_days)
