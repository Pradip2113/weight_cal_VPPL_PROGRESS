// Copyright (c) 2023, Abhishek Chougule and contributors
// For license information, please see license.txt

frappe.ui.form.on("Cane Weight", {
    season: function(frm) {
            frm.set_query("trip_sheet_no", function() { 
                return {
                    filters: [
                        ["Trip Sheet", "season", '=', frm.doc.season],
                    ]
                };
            });
    	}
	}
);

frappe.ui.form.on('Cane Weight', {
    refresh: function(frm) {
        $('.layout-side-section').hide();
        $('.layout-main-section-wrapper').css('margin-left', '0');
		
    }
});

frappe.ui.form.on('Cane Weight', {
	actual_weight: function (frm) {
		frm.call({
			method:'net_weight',
			doc: frm.doc,
		});
	}
});

frappe.ui.form.on('Cane Weight', {
	empty_weight: function (frm) {
		frm.call({
			method:'tear_weight',
			doc: frm.doc,
		});
	}
});

// frappe.ui.form.on('Cane Weight', {
//     get_loaded_weight: function(frm) {
//             frappe.model.set_value("Cane Weight", frm.doc.name, 'gross_weight_timedate', frappe.datetime.get_datetime_as_string());
//     }
// });
// frappe.ui.form.on('Cane Weight', {
//     get_empty_weight: function(frm) {
//             frappe.model.set_value("Cane Weight", frm.doc.name, 'tear_weight_timedate', frappe.datetime.get_datetime_as_string());
//     }
// });


frappe.ui.form.on('Cane Weight', {
	onload: function (frm) {
		frm.fields_dict['trip_sheet_no'].$input.css('background-color', '#D2E9FB');
		frm.fields_dict['slip_no'].$input.css('background-color', '#D2E9FB');
		frm.fields_dict['vehicle_number'].$input.css('background-color', '#D2E9FB');
		frm.fields_dict['season'].$input.css('background-color', '#D2E9FB');
        frm.fields_dict['get_loaded_weight'].$input.css('background-color', '#D2E9FB');
		frm.fields_dict['get_empty_weight'].$input.css('background-color', '#D2E9FB');
		frm.call({
			method:'get_bridge_info',
			doc: frm.doc,
		});
		
	}
})

frappe.ui.form.on('Cane Weight', {
	refresh: function (frm) {
		frm.call({
			method:'get_bridge_info',
			doc: frm.doc,
		});
	}
})

frappe.ui.form.on('Cane Weight', {
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
  
  frappe.ui.form.on('Cane Weight', {
	manually_tear_weight: function (frm) {
	  var emtyWeight = frm.doc.manually_tear_weight;
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


frappe.ui.form.on('Cane Weight', {
	branch: function (frm) {
		frm.call({
			method:'get_shift',
			doc: frm.doc,
		});
	}
})
// frappe.ui.form.on('Cane Weight', {
// 	onload: function (frm) {
// 		frm.call({
// 			method:'get_empty_weight',
// 			doc: frm.doc,
// 		});
// 	}
// })

frappe.ui.form.on('Cane Weight', {
	get_loaded_weight: function (frm) {
		// frm.fields_dict.get_loaded_weight.$wrapper.hide();
		frm.call({
			method:'get_loaded_weight',
			doc: frm.doc,
		});
	}
})

// frappe.ui.form.on('Cane Weight', {
// 	get_loaded_weight: function (frm,cdt,cdn) {
// 		// frm.fields_dict.get_loaded_weight.$wrapper.hide();
// 		frm.call({
// 			method:'get_qty',
// 			doc: frm.doc,cdt,cdn
// 		});
// 	}
// })

// frappe.ui.form.on('Cane Weight', {
// 	loaded_weight: function (frm,cdt,cdn) {
// 		// frm.fields_dict.get_loaded_weight.$wrapper.hide();
// 		frm.call({
// 			method:'get_qty',
// 			doc: frm.doc,cdt,cdn
// 		});
// 	}
// })

// frappe.ui.form.on('Cane Weight', {
// 	empty_weight: function (frm,cdt,cdn) {
// 		// frm.fields_dict.get_loaded_weight.$wrapper.hide();
// 		frm.call({
// 			method:'get_qty',
// 			doc: frm.doc,cdt,cdn
// 		});
// 	}
// })


// frappe.ui.form.on('Cane Weight', {
// 	get_empty_weight: function (frm,cdt,cdn) {
// 		// frm.fields_dict.get_loaded_weight.$wrapper.hide();
// 		frm.call({
// 			method:'get_qty',
// 			doc: frm.doc,cdt,cdn
// 		});
// 	}
// })

frappe.ui.form.on('Cane Weight', {
	onload: function (frm) {
		frm.call({
			method:'get_actual_weight',
			doc: frm.doc,
		});
	}
})

frappe.ui.form.on('Cane Weight', {
	get_loaded_weight: function (frm) {
		frm.call({
			method:'get_actual_weight',
			doc: frm.doc,
		});
	}
})

frappe.ui.form.on('Cane Weight', {
	get_empty_weight: function (frm) {
		frm.call({
			method:'get_empty_weight',
			doc: frm.doc,
		});
	}
})

frappe.ui.form.on('Cane Weight', {
	get_empty_weight: function (frm) {
		frm.call({
			method:'get_actual_weight',
			doc: frm.doc,
		});
	}
})
// frappe.ui.form.on('Cane Weight Item', {
// 	item_code: function (frm) {
// 		frm.call({
// 			method:'get_qty',
// 			doc: frm.doc,
// 		});
// 	}
// })

frappe.ui.form.on('Cane Weight', {
	loaded_weight: function (frm) {
		frm.call({
			method:'get_actual_weight',
			doc: frm.doc,
		});
	}
})

frappe.ui.form.on('Cane Weight', {
	empty_weight: function (frm) {
		frm.call({
			method:'get_actual_weight',
			doc: frm.doc,
		});
	}
})
frappe.ui.form.on('Cane Weight', {
	empty_weight: function (frm) {
		frm.call({
			method:'get_actual_weight',
			doc: frm.doc,
		});
	}
})

frappe.ui.form.on('Cane Weight', {
	trip_sheet_no: function (frm) {
		frm.clear_table("penalty_charges")
		frm.refresh_field('penalty_charges')
		frm.call({
			method:'append_ht_tab',
			doc: frm.doc,
		});
	}
})