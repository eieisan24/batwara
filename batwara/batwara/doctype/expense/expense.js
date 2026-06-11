// Copyright (c) 2026, Build with Ei Ei San and contributors
// For license information, please see license.txt

frappe.ui.form.on("Expense", {
	refresh(frm) {
        frm.set_query("paid_by", function(){
            return {
                filters: {
                    "ignore_user_type": 1
                }
            }
        });
	},
});
