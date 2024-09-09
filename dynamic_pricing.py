# class Product:
#     def __init__(self,product_id,product_name,price,inventory_count):
#         self.product_name = product_name
#         self.product_id = product_id
#         self.price = price
#         self.inventory_count = inventory_count
#
#         def apply_discount(self,discount_percentage):
#             discount = self.price * discount_percentage/100
#             self.price -= discount
#         def cell(self,quantity):
#             self.inventory_count -= quantity
#
# class DynamicPricing:
#     def adjust_price(self,product,demand,price):
#         if demand=='high':
#             product.price += price
#             print(f"Product price has increased with an amount of {price}$ because of high demand ")
#         if demand=='low':
#             product.price -= price
#             print(f"Product price has decreased with an amount of {price}$ because of low demand ")
#
# dynamicpricing = DynamicPricing()
# product = Product(1,"koshik",2000,58)
# dynamicpricing.adjust_price(product,'low',1000)
# dynamicpricing.adjust_price(product,'high',1000)
#
# # 1. price-n u inventory count-n karox en aynqan nvazel minchev darnan bacasakan arjeq
# # ev naev tvic baci urish ban poxancelu depqum kstananq problem
#
# # 2 and 3 petqa cell(quantity) i mej stugumner katarenq qani vor qanakutyuny kara darna bacasakan
# # nuynnel  apply_discount(discount_percentage):
# # inventory increasing klini erb vor ogtagorcoxy bacasakan ta
# # mer minusi het kdarna drakan u kavelana
#
