// Copyright (c) 2017, Sathisha Poojary and contributors
// For license information, please see license.txt

frappe.ui.form.on('Auto Vehicle', {
	refresh: function(frm) {
		frm.add_custom_button(__('Add Dealer Services'), function() {
				frm.events.invoke_function(frm, "add_dealer_services")
		});
	},
	invoke_function(frm, method) {
		frappe.call({
			doc: frm.doc,
			method: method,
			callback: function(r) {
				if(!r.exe) {
					frm.refresh_fields()
				}
			}
		});
	},

});
