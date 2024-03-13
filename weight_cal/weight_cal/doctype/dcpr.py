import frappe
# from frappe.model.document import Document


# class DcPr(Document):
    #-----------------------------------------------------------------------------------------------------------------
@frappe.whitelist()
def get_bridge_info(self):
    self.user_name=frappe.db.get_value("User", frappe.session.user, "full_name")
    doc = frappe.db.get_list("WB Master Setting", fields=["operator_name","weight_bridge_no"])
    for d in doc:
        if d.operator_name==frappe.session.user:
            self.wb=d.weight_bridge_no
            break
    wbstatus=frappe.get_doc("Weight Reading", "weight-reading")
    temp=wbstatus.wb1_status
    rolenm=frappe.db.get_value("User", frappe.session.user, "role_profile_name")
    if str(rolenm)=="WB User":
        if temp=="Connected.":
            if self.wb=="Weight Bridge 1":
                temp=wbstatus.wb1_status
                frappe.msgprint((self.wb+' : '+temp),indicator="green",title="Weight Bridge Status")
            if self.wb=="Weight Bridge 2":
                temp=wbstatus.wb2_status
                frappe.msgprint((self.wb+' : '+temp),indicator="green",title="Weight Bridge Status")
            if self.wb=="Weight Bridge 3":
                temp=wbstatus.wb3_status
                frappe.msgprint((self.wb+' : '+temp),indicator="green",title="Weight Bridge Status")
            if self.wb=="Weight Bridge 4":
                temp=wbstatus.wb4_status
                frappe.msgprint((self.wb+' : '+temp),indicator="green",title="Weight Bridge Status")
            if self.wb=="Weight Bridge 5":
                temp=wbstatus.wb5_status
                frappe.msgprint((self.wb+' : '+temp),indicator="green",title="Weight Bridge Status")
        else:   
            if self.wb=="Weight Bridge 1":
                temp=wbstatus.wb1_status
                frappe.msgprint((self.wb+' : '+temp),indicator="green",title="Weight Bridge Status")
            if self.wb=="Weight Bridge 2":
                temp=wbstatus.wb2_status
                frappe.msgprint((self.wb+' : '+temp),indicator="green",title="Weight Bridge Status")
            if self.wb=="Weight Bridge 3":
                temp=wbstatus.wb3_status
                frappe.msgprint((self.wb+' : '+temp),indicator="green",title="Weight Bridge Status")
            if self.wb=="Weight Bridge 4":
                temp=wbstatus.wb4_status
                frappe.msgprint((self.wb+' : '+temp),indicator="green",title="Weight Bridge Status")
            if self.wb=="Weight Bridge 5":
                temp=wbstatus.wb5_status
                frappe.msgprint((self.wb+' : '+temp),indicator="green",title="Weight Bridge Status")

@frappe.whitelist()
def get_qty(self):
    # cfactor=0
    for u in self.get('items'):
        if u.uom=="KG":
            u.qty=self.actual_weight
        if u.uom=="TON":
            u.qty=self.actual_weight*0.001

        #     batch=frappe.db.get_list("Item")
        #     for b in batch:
        #         eachbatch = frappe.get_doc("Item", b.name)
        #         for i in eachbatch.get('uoms'):
        #             for m in self.items:
        #                 if m.item_code==b.name:
        #                     if i.uom=="KG":
        #                         cfactor=i.conversion_factor
        #     u.qty=self.actual_weight*cfactor
        # else:
        #     u.qty=1.00







@frappe.whitelist()
def get_loaded_weight(self):
    doc=frappe.get_doc("Weight Reading")
    if self.wb=="Weight Bridge 1":
        self.loaded_weight=doc.wm1
    if self.wb=="Weight Bridge 2":
        self.loaded_weight=doc.wm2
    if self.wb=="Weight Bridge 3":
        self.loaded_weight=doc.wm3
    if self.wb=="Weight Bridge 4":
        self.loaded_weight=doc.wm4
    if self.wb=="Weight Bridge 5":
        self.loaded_weight=doc.wm5

@frappe.whitelist()
def get_empty_weight(self):
    # if is_internet_available:
    #     frappe.msgprint('Internet Available')
    doc=frappe.get_doc("Weight Reading")
    if self.wb=="Weight Bridge 1":
        self.empty_weight=doc.wm1
    if self.wb=="Weight Bridge 2":
        self.empty_weight=doc.wm2
    if self.wb=="Weight Bridge 3":
        self.empty_weight=doc.wm3
    if self.wb=="Weight Bridge 4":
        self.empty_weight=doc.wm4
    if self.wb=="Weight Bridge 5":
        self.empty_weight=doc.wm5


# @frappe.whitelist()
# def is_internet_available():
#   try:
#       requests.get('https://www.google.com')
#       return True
#   except requests.ConnectionError:
#       return False


@frappe.whitelist()
def get_actual_weight(self):
    self.actual_weight=self.loaded_weight-self.empty_weight

# @frappe.whitelist()
# def append_qty(self):
#   for i in self.items:
#       if str(i.item_group)=='Sugar':
#           i.qty=self.actual_weight

#-----------------------------------------------------------------------------------------------------------------