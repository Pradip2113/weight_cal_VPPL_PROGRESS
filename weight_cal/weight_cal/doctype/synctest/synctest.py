# Copyright (c) 2023, Abhishek Chougule and contributors
# For license information, please see license.txt

from frappe.model.document import Document
import string    
import random

class SyncTest(Document):
    def before_save(self):
        ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 10))  
        self.uin='N-'+ran