import json
from collections import namedtuple
from json import JSONEncoder

class Asset:
    def __init__(self, id, name, asset_tag, serial, model, model_number, eol, status_label, category, manufacturer, supplier, notes, order_number, company, location, rtd_location, image, assigned_to, warranty_months, warranty_expires, created_at, updated_at, last_audit_date, next_audit_date, deleted_at, purchase_date, last_checkout, expected_checkin, purchase_cost, checkin_counter, checkout_counter, requests_counter, user_can_checkout, custom_fields, available_actions):
        self.id, self.name, self.asset_tag, self.serial, self.model, self.model_number, self.eol, self.status_label, self.category, self.manufacturer, self.supplier, self.notes, self.order_number, self.company, self.location, self.rtd_location, self.image, self.assigned_to, self.warranty_months, self.warranty_expires, self.created_at, self.updated_at, self.last_audit_date, self.next_audit_date, self.deleted_at, self.purchase_date, self.last_checkout, self.expected_checkin, self.purchase_cost, self.checkin_counter, self.checkout_counter, self.requests_counter, self.user_can_checkout, self.custom_fields, self.available_actions = id, name, asset_tag, serial, model, model_number, eol, status_label, category, manufacturer, supplier, notes, order_number, company, location, rtd_location, image, assigned_to, warranty_months, warranty_expires, created_at, updated_at, last_audit_date, next_audit_date, deleted_at, purchase_date, last_checkout, expected_checkin, purchase_cost, checkin_counter, checkout_counter, requests_counter, user_can_checkout, custom_fields, available_actions

class AssetEncoder(JSONEncoder):
    def default(self,o):
        return o.__dict__

def customAssetDecoder(assetDict):
    return namedtuple('X', assetDict.keys())(*assetDict.values())
