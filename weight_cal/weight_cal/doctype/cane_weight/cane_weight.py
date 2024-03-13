# Copyright (c) 2023, Abhishek Chougule and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import datetime
from datetime import date
from frappe.utils.data import get_datetime


class CaneWeight(Document):
	#-----------------------------------------------------------------------------------------------------------------
	@frappe.whitelist()
	def get_bridge_info(self):
		self.user_name=frappe.db.get_value("User", frappe.session.user, "full_name")
		# weight_reading=frappe.get_doc("Weight Reading", "weight-reading")
		# if(weight_reading.wm1_ip==local_ip):
		# 	self.wb='Weight Bridge 1'
		# 	frappe.msgprint(('Weight Bridge 1'+' : '+weight_reading.wb1_status),title="Weight Bridge Status")
		# elif(weight_reading.wm2_ip==local_ip):
		# 	self.wb='Weight Bridge 2'
		# 	frappe.msgprint(('Weight Bridge 2'+' : '+weight_reading.wb2_status),title="Weight Bridge Status")
		# elif(weight_reading.wm3_ip==local_ip):
		# 	self.wb='Weight Bridge 3'
		# 	frappe.msgprint(('Weight Bridge 3'+' : '+weight_reading.wb3_status),title="Weight Bridge Status")
		# elif(weight_reading.wm4_ip==local_ip):
		# 	self.wb='Weight Bridge 4'
		# 	frappe.msgprint(('Weight Bridge 4'+' : '+weight_reading.wb4_status),title="Weight Bridge Status")
		# elif(weight_reading.wm5_ip==local_ip):
		# 	self.wb='Weight Bridge 5'
		# 	frappe.msgprint(('Weight Bridge 5'+' : '+weight_reading.wb5_status),title="Weight Bridge Status")
		# else:
		# 	frappe.msgprint(("Local IP Dosen't Match with any IP of weight bridge"),indicator="red",title="Weight Bridge Status")
   
   
		doc = frappe.db.get_list("WB Master Setting",filters={"operator_name": frappe.session.user } ,fields=["name","operator_name","weight_bridge_no"])
		if doc:
			self.operator_name= doc[0].name
			self.wb= doc[0].weight_bridge_no
		else:
			frappe.msgprint("User do not have any permission to access any weight bridge")
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

	# @frappe.whitelist()
	# def get_qty(self):
	# 	# cfactor=0
	# 	for u in self.get('items'):
	# 		if u.uom=="KG":
	# 			u.qty=self.actual_weight
	# 		if u.uom=="TON":
	# 			u.qty=self.actual_weight*0.001

	# 		    batch=frappe.db.get_list("Item")
	# 		    for b in batch:
	# 		        eachbatch = frappe.get_doc("Item", b.name)
	# 		        for i in eachbatch.get('uoms'):
	# 		            for m in self.items:
	# 		                if m.item_code==b.name:
	# 		                    if i.uom=="KG":
	# 		                        cfactor=i.conversion_factor
	# 		    u.qty=self.actual_weight*cfactor
	# 		else:
	# 		    u.qty=1.00







	@frappe.whitelist()
	def get_loaded_weight(self):
		# weight_reading=frappe.get_doc("Weight Reading", "weight-reading")
		# if (weight_reading.wm1_ip == local_ip and weight_reading.wb1_status == 'Connected'):
		# 	self.loaded_weight=weight_reading.wm1
			
		# elif(weight_reading.wm2_ip==local_ip and weight_reading.wb2_status == 'Connected'):
		# 	self.loaded_weight=weight_reading.wm2

		# elif(weight_reading.wm3_ip==local_ip and weight_reading.wb3_status == 'Connected'):
		# 	self.loaded_weight=weight_reading.wm3
			
		# elif(weight_reading.wm4_ip==local_ip and weight_reading.wb4_status == 'Connected'):
		# 	self.loaded_weight=weight_reading.wm4

		# elif(weight_reading.wm5_ip==local_ip and weight_reading.wb5_status == 'Connected'):
		# 	self.loaded_weight=weight_reading.wm5
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
		self.gross_weight_timedate=datetime.datetime.now()

	@frappe.whitelist()
	def get_empty_weight(self):
		# weight_reading=frappe.get_doc("Weight Reading", "weight-reading")
		# if (weight_reading.wm1_ip == local_ip and weight_reading.wb1_status == 'Connected'):
		# 	self.empty_weight=weight_reading.wm1
			
		# elif(weight_reading.wm2_ip==local_ip and weight_reading.wb2_status == 'Connected'):
		# 	self.empty_weight=weight_reading.wm2

		# elif(weight_reading.wm3_ip==local_ip and weight_reading.wb3_status == 'Connected'):
		# 	self.empty_weight=weight_reading.wm3
			
		# elif(weight_reading.wm4_ip==local_ip and weight_reading.wb4_status == 'Connected'):
		# 	self.empty_weight=weight_reading.wm4

		# elif(weight_reading.wm5_ip==local_ip and weight_reading.wb5_status == 'Connected'):
		# 	self.empty_weight=weight_reading.wm5
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
		self.tear_weight_timedate= datetime.datetime.now()
		self.tear_weight()


	@frappe.whitelist()
	def net_weight(self):
		if(self.actual_weight <=0):
			frappe.throw("Net Weight Can't Negative or 0")
   
	@frappe.whitelist()
	def tear_weight(self):
		tolerance = 1e-9 
		loaded_weight=float(self.loaded_weight)
		empty_weight=float(self.empty_weight)# Adjust the tolerance based on your specific requirements
		if loaded_weight < empty_weight - tolerance:
			frappe.throw("Error: Gross weight cannot be less than Tear weight.")
		elif abs(loaded_weight - empty_weight) < tolerance:
			frappe.throw("Error: Gross weight and Tear weight cannot be the same.")


	@frappe.whitelist()
	def get_actual_weight(self):
		self.actual_weight=self.loaded_weight-self.empty_weight
		self.set_binding_weight()
		self.actual_weight= (self.loaded_weight-self.empty_weight)-((self.binding_weight)/1000)
		self.set_weight_id_water_supplier()
  
	@frappe.whitelist()
	def before_save(self):
		self.validate_net_weight()
		self.time_validation()
		self.weight_flag=1
  
	@frappe.whitelist()
	def before_submit(self):
		self.set_value_at_cane_weight_no()
		self.update_counter_at_branch()
		self.create_deduction()
		self.set_value_in_h_and_t_contract()
		self.assignDiseal()
		self.weight_flag=2
		self.add_diesel_sale()
		frappe.db.set_value("Farmer List",self.farmer_code,"read_only_count",1)
  
	@frappe.whitelist()
	def before_cancel(self):
		self.on_cancel_update_counter_at_branch()
		self.cancel_deduction()
		self.update_diesel_sale()
  
	@frappe.whitelist()
	def validate_net_weight(self):
		if self.actual_weight <=0:
			frappe.throw('Weight can not be negative')
   
	@frappe.whitelist()
	def set_value_at_cane_weight_no(self):
		current_value= frappe.get_value("Branch",self.branch,"cane_weight_no")
		if not self.cane_weight_no:
			self.cane_weight_no = current_value+1
			# frappe.throw(str(self.cane_weight_no))

   
	@frappe.whitelist()
	def update_counter_at_branch(self):
		if self.cane_weight_no:
			frappe.set_value("Branch",self.branch,"cane_weight_no",self.cane_weight_no)

	@frappe.whitelist()
	def on_cancel_update_counter_at_branch(self):
		current_value= frappe.get_value("Branch",self.branch,"cane_weight_no")
     
		if self.cane_weight_no==current_value:
			frappe.set_value("Branch",self.branch,"cane_weight_no",(self.cane_weight_no-1))
 
	@frappe.whitelist()
	def set_binding_weight(self):
		value_per_weight = frappe.get_value("Branch",self.branch,"binding_weight_per_ton")
		if value_per_weight:
			self.binding_weight = self.actual_weight*value_per_weight
   
		else:
			frappe.throw(f'Set Binding Weight Quentity per Ton In Branch "{self.branch}"')
   
	@frappe.whitelist()
	def set_weight_id_water_supplier(self):
		if self.water_supplier_code:
			a_w=float(self.actual_weight)
			w_p=float(self.water_share)
			water_supplier_weight = ((a_w * w_p)/100)
			change_actual_weight = (a_w- water_supplier_weight)
			self.actual_weight=change_actual_weight
			self.water_supplier_weight = water_supplier_weight
	
    #To get the shift type
	@frappe.whitelist()
	def get_shift(self):
		current_time = datetime.datetime.now().time()
		child_table = frappe.get_all("Child Shift Setting", filters={
			"parent": self.branch,
		}, fields=["shift", "start_time", "end_time"])
		for shift_setting in child_table:
			start_time = shift_setting.start_time.total_seconds()
			end_time = shift_setting.end_time.total_seconds()
			current_seconds = current_time.hour * 3600 + current_time.minute * 60 + current_time.second
			if start_time <= current_seconds <= end_time:
				self.shft = shift_setting.shift
				break
		
	# @frappe.whitelist()
	# def append_qty(self):
	#   for i in self.items:
	#       if str(i.item_group)=='Sugar':
	#           i.qty=self.actual_weight
	
	#code for keeping logs
	def after_insert(self):
		with open("/home/erpadmin/logs/"+str(date.today())+"_"+self.wb+".txt",'a+') as f:
			f.write(str(self.name)+" "+str(self.wb)+" "+str(self.gross_weight_timedate)+" Gross Weight:"+str(self.loaded_weight)+" Tear Weight:"+str(self.empty_weight)+" Net Weight:"+str(self.actual_weight)+"\n")
			f.close()
	#To append harvester info and transporter into into table
	@frappe.whitelist()
	def append_ht_tab(self):
		self.append(
			"penalty_charges",
			{
				"vendor_id":self.transporter_code,
				"vendor_name":self.transporter_name,
				"type":"Transporter",
				"deduction_type":"Penalty"
			}	
		)
		self.append(
			"penalty_charges",
			{
				"vendor_id":self.harvester_code,
				"vendor_name":self.harvester_name,
				"type":"Harvester",
				"deduction_type":"Penalty"
			}	
		)		
	def create_deduction(self):
		for i in self.get("penalty_charges"):
			if(i.deduction_amount>0):
				doc = frappe.new_doc('Deduction Form')
				doc.farmer_code =self.transporter_code if(i.type=="Transporter") else self.harvester_code 
				doc.deduction_amount=float(i.deduction_amount)
				doc.deduction_name=i.deduction_type
				doc.season=self.season
				doc.branch=self.branch
				doc.date=self.date
				doc.vender_type="H and T"
				doc.h_and_t_contract_id=self.contract_id if(i.type=="Transporter") else self.harvester_contract 
				doc.deduction_status=0
				doc.insert()
				i.doc_name=str(doc.name)
				doc.submit()
	def cancel_deduction(self):
		for i in self.get("penalty_charges"):
			if(i.doc_name):
				doc = frappe.get_doc("Deduction Form",(str(i.doc_name)))
				doc.cancel()
    
    
    
	def set_value_in_h_and_t_contract(self):
		frappe.set_value('H and T Contract',self.contract_id,'last_cane_weight_entry',self.creation)
  
	def time_validation(self):
		# frappe.throw("hiiii.....?")
		datetime_value = get_datetime(self.creation)
		value = frappe.get_value('H and T Contract',self.contract_id,'last_cane_slip_entry')
		if value:
			branch_setting_time = get_datetime(frappe.get_value('Branch',self.branch,'cane_weight_time'))
			# frappe.throw(str(( datetime_value-value)<=(branch_setting_time)))
			if( datetime_value-value)<=(branch_setting_time):
				frappe.throw(f'Your are not allow to create "Cane weight" because {self.contract_id} have not complited {branch_setting_time}  time set by agricultural Department come after {branch_setting_time-(datetime_value-value)} time')


	def assignDiseal(self):
		if self.gang_type == "HARVESTING MACHINE":
			weightlist= frappe.get_all("Cane Weight",filters={"season":self.season,
			"gang_type": "HARVESTING MACHINE","transporter_name":self.transporter_name,"harvester_name":self.harvester_name,"docstatus":1}, fields=["actual_weight"])
			total_weight=0
			for i in weightlist:
				total_weight= total_weight + i.actual_weight
			total_weight= total_weight + self.actual_weight
			frappe.msgprint(str(total_weight))
	
	
		
  	
	def add_diesel_sale(self):
		ton_value_on_diesel_allocate, diesel_allocation_value_har, diesel_allocation_per_km = frappe.get_value("Branch",{"name":self.branch},["total_ton_value_from_which_diesel_will_allocate", "diesel_allocation_amount_per_ton", "diesel_allocation_amount_per_km"])
		if(not ton_value_on_diesel_allocate):
			frappe.throw("Please Enter Total TON Value From Which Diesel Will Allocate in Branch")
		if(not diesel_allocation_value_har):
			frappe.throw("Please Enter How Much Diesel Will Allocate (in Liter) in Branch")
		if(not diesel_allocation_per_km):
			frappe.throw("Please Enter Diesel Allocation Per KM (in Liter) in Branch")
		if(self.vehicle_type!="BULLOCK CART"):
			if(self.contract_id):
				doc=frappe.get_doc("H and T Contract",self.contract_id)
				child_table=doc.get("diesel_calculation")
				count=0
				for i in child_table:
					if(len(child_table)>0 and i.customer_type=='Transporter'):
						count=1
						i.total_distance=i.total_distance+self.distance
						i.total_allocation=i.total_allocation+(self.distance*diesel_allocation_per_km)
						i.total_lapse=i.total_lapse+i.remaining
						i.remaining=self.distance*diesel_allocation_per_km
				if(count==0):
					doc.append("diesel_calculation",{
						"customer_type":"Transporter",
						"total_distance":self.distance,
						"total_allocation":self.distance*diesel_allocation_per_km,
						"total_sold":0,
						"total_lapse":0,
						"remaining":self.distance*diesel_allocation_per_km,
					})
				doc.save()
    
		if(self.gang_type=="HARVESTING MACHINE"):
			if(self.harvester_contract):
				doc1=frappe.get_doc("H and T Contract",self.harvester_contract)
				child_table=doc1.get("diesel_calculation")
				count=0
				for i in child_table:
					if(len(child_table)>0 and i.customer_type=='Harvester'):
						count=1
						liter_value_per_ton=diesel_allocation_value_har/ton_value_on_diesel_allocate
						i.total_weight=i.total_weight+self.actual_weight
						i.total_allocation=i.total_allocation+(self.actual_weight*liter_value_per_ton)
						i.remaining=i.remaining+(self.actual_weight*liter_value_per_ton)
				if(count==0):
					liter_value_per_ton=diesel_allocation_value_har/ton_value_on_diesel_allocate
					doc1.append("diesel_calculation",{
						"customer_type":"Harvester",
						"total_weight":self.actual_weight,
						"remaining":self.actual_weight*liter_value_per_ton,
						"total_allocation":self.actual_weight*liter_value_per_ton,
						"total_lapse":0,
						"total_sold":0,
					})
				doc1.save()
				
    
	def update_diesel_sale(self):
		ton_value_on_diesel_allocate, diesel_allocation_value_har, diesel_allocation_per_km = frappe.get_value("Branch",{"name":self.branch},["total_ton_value_from_which_diesel_will_allocate", "diesel_allocation_amount_per_ton", "diesel_allocation_amount_per_km"])
		if(not ton_value_on_diesel_allocate):
			frappe.throw("Please Enter Total TON Value From Which Diesel Will Allocate in Branch")
		if(not diesel_allocation_value_har):
			frappe.throw("Please Enter How Much Diesel Will Allocate (in Liter) in Branch")
		if(not diesel_allocation_per_km):
			frappe.throw("Please Enter Diesel Allocation Per KM (in Liter) in Branch")
		if(self.vehicle_type!="BULLOCK CART"):
			if(self.contract_id):
				doc=frappe.get_doc("H and T Contract",self.contract_id)
				child_table=doc.get("diesel_calculation")
				for i in child_table:
					if(len(child_table)>0 and i.customer_type=='Transporter'):
						i.remaining=(i.total_allocation-((self.distance*diesel_allocation_per_km)+i.total_sold))
						i.total_lapse=i.total_lapse-(i.total_allocation-(i.total_sold+i.remaining))
						i.total_distance=i.total_distance-self.distance
						i.total_allocation=i.total_allocation-(self.distance*diesel_allocation_per_km)
				doc.save()
		if(self.gang_type=="HARVESTING MACHINE"):
			if(self.harvester_contract):
				doc1=frappe.get_doc("H and T Contract",self.harvester_contract)
				child_table=doc1.get("diesel_calculation")
				for i in child_table:
					if(len(child_table)>0 and i.customer_type=='Harvester'):
						liter_value_per_ton=diesel_allocation_value_har/ton_value_on_diesel_allocate
						i.total_weight=i.total_weight-self.actual_weight
						i.total_allocation=i.total_allocation-(self.actual_weight*liter_value_per_ton)
						i.remaining=i.remaining-(self.actual_weight*liter_value_per_ton)
				doc1.save()

							
   
				
   
   
   
   
   
   
   
   
  #-----------------------------------------------------------------------------------------------------------------
