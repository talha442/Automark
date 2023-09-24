from woocommerce import API
import json
import env
from pprint import pprint

HOSTNAME = env.HOSTNAME
CONSUMER_KEY = env.CONSUMER_KEY
CONSUMER_SECRET = env.CONSUMER_SECRET

# print(HOSTNAME)
# print(CONSUMER_KEY)
# print(CONSUMER_SECRET)

class WooAPI:
    def __init__(self):
        self.wcapi = API(
            url=HOSTNAME,
            consumer_key=CONSUMER_KEY,
            consumer_secret=CONSUMER_SECRET,
            version="wc/v3"
        )

    def get(self, endpoint):
        return self.wcapi.get(endpoint).json()

    def get_products(self):
        return self.get("products")

    def get_product(self, id):
        return self.get(f"products/{id}")

    def get_orders(self):
        return self.get("orders")

    def get_order(self, id):
        return self.get(f"orders/{id}")

    def get_customers(self):
        return self.get("customers")

    def get_customer(self, id):
        return self.get(f"customers/{id}")

    def get_coupons(self):
        return self.get("coupons")

    def get_coupon(self, id):
        return self.get(f"coupons/{id}")

    def get_reports(self):
        return self.get("reports")
    
    def get_system_status(self):
        return self.get("system_status")

    def get_store_info(self):
        return self.get("")

        
if __name__ == "__main__":
    woo = WooAPI()