# Copyright (c) 2023, Abhishek Chougule and contributors
# For license information, please see license.txt
import platform
import uuid
import frappe
from frappe.model.document import Document
import socket

local_ip = socket.gethostbyname(socket.gethostname())


class WeightBridge(Document):
    global weight
    global weight_name
    
#-----------------------------------------------------------------------------------------------------------------
    @frappe.whitelist()
    def get_bridge_info(self):

        # frappe.msgprint(f'Your IP Address is {local_ip}')
        # weight_reading=frappe.get_doc("Weight Reading", "weight-reading")
        # if(weight_reading.wm1_ip==local_ip):
        #     frappe.set_value('Weight Bridge 1')
        #     frappe.msgprint(('Weight Bridge 1'+' : '+weight_reading.wb1_status),title="Weight Bridge Status")
        # elif(weight_reading.wm2_ip==local_ip):
        #     self.wb='Weight Bridge 2'
        #     frappe.msgprint(('Weight Bridge 2'+' : '+weight_reading.wb2_status),title="Weight Bridge Status")
        # elif(weight_reading.wm3_ip==local_ip):
        #     self.wb='Weight Bridge 3'
        #     frappe.msgprint(('Weight Bridge 3'+' : '+weight_reading.wb3_status),title="Weight Bridge Status")
        # elif(weight_reading.wm4_ip==local_ip):
        #     self.wb='Weight Bridge 4'
        #     frappe.msgprint(('Weight Bridge 4'+' : '+weight_reading.wb4_status),title="Weight Bridge Status")
        # elif(weight_reading.wm5_ip==local_ip):
        #     self.wb='Weight Bridge 5'
        #     frappe.msgprint(('Weight Bridge 5'+' : '+weight_reading.wb5_status),title="Weight Bridge Status")
        # else:
        #     frappe.msgprint(("Local IP Dosen't Match with any IP of weight bridge"),indicator="red",title="Weight Bridge Status")
        
            
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
        # weight_reading=frappe.get_doc("Weight Reading", "weight-reading")
        # if (weight_reading.wm1_ip == local_ip and weight_reading.wb1_status == 'Connected'):
        #     self.loaded_weight=weight_reading.wm1
            
        # elif(weight_reading.wm2_ip==local_ip and weight_reading.wb2_status == 'Connected'):
        #     self.loaded_weight=weight_reading.wm2
     
        # elif(weight_reading.wm3_ip==local_ip and weight_reading.wb3_status == 'Connected'):
        #     self.loaded_weight=weight_reading.wm3
           
        # elif(weight_reading.wm4_ip==local_ip and weight_reading.wb4_status == 'Connected'):
        #     self.loaded_weight=weight_reading.wm4
       
        # elif(weight_reading.wm5_ip==local_ip and weight_reading.wb5_status == 'Connected'):
        #     self.loaded_weight=weight_reading.wm5
        
      
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
        # weight_reading=frappe.get_doc("Weight Reading", "weight-reading")
        # if (weight_reading.wm1_ip == local_ip and weight_reading.wb1_status == 'Connected'):
        #     self.empty_weight=weight_reading.wm1
            
        # elif(weight_reading.wm2_ip==local_ip and weight_reading.wb2_status == 'Connected'):
        #     self.empty_weight=weight_reading.wm2
     
        # elif(weight_reading.wm3_ip==local_ip and weight_reading.wb3_status == 'Connected'):
        #     self.empty_weight=weight_reading.wm3
           
        # elif(weight_reading.wm4_ip==local_ip and weight_reading.wb4_status == 'Connected'):
        #     self.empty_weight=weight_reading.wm4
       
        # elif(weight_reading.wm5_ip==local_ip and weight_reading.wb5_status == 'Connected'):
        #     self.empty_weight=weight_reading.wm5
        
        self.empty_weight=weight
        self.wb=weight_name
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

    @frappe.whitelist()
    def item_wgt_set(self):
      for i in self.items:
        #   if str(i.item_group)=='Sugar':
            i.qty=self.actual_weight
    
#-----------------------------------------------------------------------------------------------------------------
    @frappe.whitelist()
    def setamt(self):
        for i in self.get('items'):
            i.amount=i.qty*i.rate
            
    def before_submit(self):
        if self.loaded_weight == 0 :
            frappe.throw(" Gross Weight  0  Is Not Allow ......")
        if self.empty_weight == 0:
            frappe.throw(" Tear Weight 0  Is Not Allow ......")
            
            