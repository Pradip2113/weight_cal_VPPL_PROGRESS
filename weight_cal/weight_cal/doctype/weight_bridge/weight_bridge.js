// Copyright (c) 2023, Abhishek Chougule and contributors
// For license information, please see license.txt

frappe.ui.form.on('Weight Bridge', {
	manually_weight: function (frm) {
	  var manuallyWeight = frm.doc.manually_weight;
	  var loadedWeightField = frm.get_field('loaded_weight');
	  if (manuallyWeight) {
		loadedWeightField.df.read_only = 0;
	  } else {
		loadedWeightField.df.read_only = 1;
		frm.set_value("loaded_weight", 0.0);
	  }
	  loadedWeightField.refresh();
	}
  });
  frappe.ui.form.on('Weight Bridge', {
	manually_weight: function (frm) {
	  var emtyWeight = frm.doc.manually_weight;
	  var emtyWeightField = frm.get_field('empty_weight');
	  if (emtyWeight) {
		emtyWeightField.df.read_only = 0;
	  } else {
		emtyWeightField.df.read_only = 1;
		frm.set_value("empty_weight", 0.0);
	  }
	  emtyWeightField.refresh();
	}
  });



  
frappe.ui.form.on('Weight Bridge', {
	onload: function (frm) {
		frm.call({
			method:'get_bridge_info',
			doc: frm.doc,
		});  
	}
})

frappe.ui.form.on('Weight Bridge', {
	set_weight_qty: function (frm) {
		frm.call({
			method:'item_wgt_set',
			doc: frm.doc,
		});  
	}
})

frappe.ui.form.on('Weight Bridge', {
	get_empty_weight(frm) {
		frm.call({
			method:'get_empty_weight',
			doc: frm.doc,
		});
	    
	}
})

frappe.ui.form.on('Weight Bridge', {
	get_loaded_weight(frm) {
		frm.call({
			method:'get_loaded_weight',
			doc: frm.doc,
		}); 
	}
})
frappe.ui.form.on('Weight Bridge', {
	get_empty_weight(frm) {
		frm.call({
			method:'get_actual_weight',
			doc: frm.doc,
		}); 
	}
})
frappe.ui.form.on('Weight Bridge', {
	get_empty_weight(frm) {
		frm.call({
			method:'get_qty',
			doc: frm.doc,
		}); 
	}
})

frappe.ui.form.on('Weight Bridge', {
	get_loaded_weight(frm) {
		frm.call({
			method:'get_actual_weight',
			doc: frm.doc,
		});  
	}
})
frappe.ui.form.on('Weight Bridge', {
	get_loaded_weight(frm) {
		frm.call({
			method:'get_qty',
			doc: frm.doc,
		});  
	}
})


frappe.ui.form.on('Delivery Note Item', {
	item_code: function (frm,cdt,cdn) {
		frm.call({
			method:'get_qty',
			doc: frm.doc,
		});
	}
})

frappe.ui.form.on('Delivery Note Item', {
	rate: function (frm) {
		frm.call({
			method:'setamt',
			doc: frm.doc,
		});
	}
})
// frappe.ui.form.on('Weight Bridge', {
// 	onload: function (frm) {
// 		frm.call({
// 			method:'get_bridge_info',
// 			doc: frm.doc,
// 		});
// 	}
// })

// frappe.ui.form.on('Delivery Note Item', {
// 	rate: function (frm) {
// 		frm.call({
// 			method:'setamt',
// 			doc: frm.doc,
// 		});
// 	}
// })


// frappe.ui.form.on('Weight Bridge', {
// 	onload: function (frm) {
// 		frm.call({
// 			method:'get_empty_weight',
// 			doc: frm.doc,
// 		});
// 	}
// })

// frappe.ui.form.on('Weight Bridge', {
// 	get_loaded_weight: function (frm) {
// 		// frm.fields_dict.get_loaded_weight.$wrapper.hide();
// 		frm.call({
// 			method:'get_loaded_weight',
// 			doc: frm.doc,
// 		});
// 	}
// })

// frappe.ui.form.on('Weight Bridge', {
// 	get_loaded_weight: function (frm,cdt,cdn) {
// 		// frm.fields_dict.get_loaded_weight.$wrapper.hide();
// 		frm.call({
// 			method:'get_qty',
// 			doc: frm.doc,cdt,cdn
// 		});
// 	}
// })

// frappe.ui.form.on('Weight Bridge', {
// 	loaded_weight: function (frm,cdt,cdn) {
// 		// frm.fields_dict.get_loaded_weight.$wrapper.hide();
// 		frm.call({
// 			method:'get_qty',
// 			doc: frm.doc,cdt,cdn
// 		});
// 	}
// })

// frappe.ui.form.on('Weight Bridge', {
// 	empty_weight: function (frm,cdt,cdn) {
// 		// frm.fields_dict.get_loaded_weight.$wrapper.hide();
// 		frm.call({
// 			method:'get_qty',
// 			doc: frm.doc,cdt,cdn
// 		});
// 	}
// })


// frappe.ui.form.on('Weight Bridge', {
// 	get_empty_weight: function (frm,cdt,cdn) {
// 		// frm.fields_dict.get_loaded_weight.$wrapper.hide();
// 		frm.call({
// 			method:'get_qty',
// 			doc: frm.doc,cdt,cdn
// 		});
// 	}
// })


// frappe.ui.form.on('Weight Bridge', {
// 	get_loaded_weight: function (frm) {
// 		frm.call({
// 			method:'get_actual_weight',
// 			doc: frm.doc,
// 		});
// 	}
// })

// frappe.ui.form.on('Weight Bridge', {
// 	get_empty_weight: function (frm) {
// 		frm.call({
// 			method:'get_empty_weight',
// 			doc: frm.doc,
// 		});
// 	}
// })

// frappe.ui.form.on('Weight Bridge', {
// 	get_empty_weight: function (frm) {
// 		frm.call({
// 			method:'get_actual_weight',
// 			doc: frm.doc,
// 		});
// 	}
// })
// frappe.ui.form.on('Delivery Note Item', {
// 	item_code: function (frm) {
// 		frm.call({
// 			method:'get_qty',
// 			doc: frm.doc,
// 		});
// 	}
// })

// frappe.ui.form.on('Weight Bridge', {
// 	loaded_weight: function (frm,cdt,cdn) {
// 		// frm.fields_dict.get_loaded_weight.$wrapper.hide();
// 		frm.call({
// 			method:'get_actual_weight',
// 			doc: frm.doc,cdt,cdn
// 		});
// 	}
// })
// frappe.ui.form.on('Weight Bridge', {
// 	empty_weight: function (frm,cdt,cdn) {
// 		// frm.fields_dict.get_loaded_weight.$wrapper.hide();
// 		frm.call({
// 			method:'get_actual_weight',
// 			doc: frm.doc,cdt,cdn
// 		});
// 	}
// })


// frappe.ui.form.on("Weight Bridge", {
// 	setup: function(frm) {
// 		frm.set_indicator_formatter('item_code',
// 			function(doc) {
// 				return (doc.docstatus==1 || doc.qty<=doc.actual_qty) ? "green" : "orange"
// 			})
// 		}
// 	});

// // frappe.ui.form.on('Weight Bridge', {
// // 	onload: function (frm) {
// // 		frm.call({
// // 			method:'get_bridge_info',
// // 			doc: frm.doc,
// // 		});
// // 	}
// // });

// // frappe.ui.form.on('Weight Bridge', {
// // 	get_loaded_weight: function (frm) {
// // 		frm.call({
// // 			method:'get_loaded_weight',
// // 			doc: frm.doc,
// // 		});
// // 	}
// // });

// // frappe.ui.form.on('Weight Bridge', {
// // 	get_empty_weight: function (frm) {
// // 		frm.call({
// // 			method:'get_empty_weight',
// // 			doc: frm.doc,
// // 		});
// // 	}
// // });

// // frappe.ui.form.on('Weight Bridge', {
// // 	get_actual_weight: function (frm) {
// // 		frm.call({
// // 			method:'get_actual_weight',
// // 			doc: frm.doc,
// // 		});
// // 	}
// // });

