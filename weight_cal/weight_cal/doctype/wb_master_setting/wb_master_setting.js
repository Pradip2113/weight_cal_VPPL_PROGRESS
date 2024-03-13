// Copyright (c) 2023, Abhishek Chougule and contributors
// For license information, please see license.txt

frappe.ui.form.on('WB Master Setting', {
	onload: function(frm) {
		frm.call({
			method:'get_user',
			doc: frm.doc,
		});
	}
});