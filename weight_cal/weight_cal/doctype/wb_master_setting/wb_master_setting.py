# Copyright (c) 2023, Abhishek Chougule and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class WBMasterSetting(Document):
	@frappe.whitelist()
	def get_user(self):
		self.user_name=frappe.db.get_value("User", frappe.session.user, "full_name")
		self.operator_name=frappe.session.user