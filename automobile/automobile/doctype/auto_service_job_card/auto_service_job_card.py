# -*- coding: utf-8 -*-
# Copyright (c) 2017, Sathisha Poojary and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document
from datetime import datetime
from datetime import date
import copy

class AutoServiceJobCard(Document):
	def before_submit(self):
		if (self.start_time is None):
			frappe.throw(_("Jobcard starting time is missing"))
		if (self.end_time is None):
			frappe.throw(_("Jobcard finishing time is missing"))
		if (self.job_items is None or len(self.job_items) == 0):
			frappe.throw(_("No job items added to job card"))

	def populate_service_type(self):
		vehicle = frappe.get_doc("Auto Vehicle", self.vehicle)
		for service in vehicle.available_services:
			if (service.service_date is None and service.expiry_date > datetime.today().date()):
				self.service_type = service.service_type
				self.populate_service_items()
				break
		vehicle.save()

	def populate_service_items(self):
		service_type = frappe.get_doc("Auto Service Type", self.service_type)
		for item in service_type.service_items:
			new_item = copy.deepcopy(item)
			self.append("job_items", new_item)

	def on_submit(self):
		vehicle = frappe.get_doc("Auto Vehicle", self.vehicle)
		for service in vehicle.available_services:
			if (service.service_type != self.service_type): continue
			service.service_date = datetime.today().date()
			vehicle.save()
			break

@frappe.whitelist()
def make_sales_invoice(jobcard):
	jobdoc = frappe.get_doc("Auto Service Job Card", jobcard)
	si = frappe.new_doc("Sales Invoice")
	si.vehicle = jobdoc.vehicle
	si.odometer = jobdoc.odometer
	si.chassis_number = jobdoc.chassis_number
	si.service_center = jobdoc.service_center
	si.job_id = jobcard
	si.technician = jobdoc.technician
	si.customer = jobdoc.customer
	#disposal_account, depreciation_cost_center = get_disposal_account_and_cost_center(company)
	for jobitem in jobdoc.job_items:
		si.append("items", 	{
			"item_code": jobitem.item,
			"qty": jobitem.qty,
			"stock_qty": jobitem.qty,
			"rate": jobitem.rate,
		})
	si.set_missing_values()
	si.due_date = si.posting_date
	return si
