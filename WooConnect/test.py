from woocommerce import API

CONSUMER_KEY = ""
CONSUMER_SECRET = ""

wcapi = API(
    url="http://web.test/",
    consumer_key=CONSUMER_KEY,
    consumer_secret=CONSUMER_SECRET,
    version="wc/v3"
)

products = wcapi.get("products").json()
print(products)
