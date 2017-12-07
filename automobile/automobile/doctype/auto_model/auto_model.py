# -*- coding: utf-8 -*-
# Copyright (c) 2017, Sathisha Poojary and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class AutoModel(Document):
	def autoname(self):
		self.name = "{0}-{1}".format(self.model, self.year)
