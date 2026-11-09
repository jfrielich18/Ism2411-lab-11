# Reflection 1:
# I would use .get() when a dictionary key might not exist and I want
# the program to continue without an error. I would use bracket notation
# when I know the key exists and need its value. My rule of thumb is to
# use .get() for optional information and brackets for required information.

# Reflection 2:
# Exercise 8 is similar to using SUMIF in Excel because it adds values
# based on categories such as region. Python is useful for larger datasets
# because it can automatically process many records using loops without
# having to manually create or update formulas.

# Exercise 1
customer = {
    "name": "Alice",
    "email": "alice@example.com",
    "tier": "gold",
    "ytd_spend": 1250.50,
}
print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])
print(customer)
 
 
# Exercise 2
customer["phone"] = "555-123-4567"
print(customer)
customer["tier"] = "platinum"
print(customer)
del customer["email"]
print(customer)
 
 
# Exercise 3
print(customer.get("email", "no email on file"))
try:
    print(customer["email"])
except KeyError:
    print("KeyError: 'email' is not in the dictionary")
 
 
# Exercise 4
for key, value in customer.items():
    print(f"{key}: {value}")
 
# Looping without .items() only gives the keys, not the values. To get the
# value I would have to look it up with customer[key] myself, and unpacking
# "key, value" directly on the dict would fail.
for key in customer:
    print(key)
 
 
# Exercise 5
tier_discounts = {"bronze": 0, "silver": .05, "gold": .10, "platinum": .15}
purchase = 200
discount = tier_discounts.get(customer["tier"], 0)
final_price = purchase * (1 - discount)
print(f"Tier: {customer['tier']}")
print(f"Discount: {discount:.0%}")
print(f"Final price: ${final_price:.2f}")
 
 
# Exercise 6
customers = [
    {"name": "Alice", "tier": "platinum"},
    {"name": "Bob", "tier": "silver"},
    {"name": "Carla", "tier": "bronze"},
]
purchase = 300
for c in customers:
    rate = tier_discounts.get(c["tier"], 0)
    print(f"{c['name']} ({c['tier']}): discount ${purchase * rate:.2f} on ${purchase}")
 
 
#Exercise 7
catalog = {
    "Widget A": {"price": 9.99, "stock": 150},
    "Gadget C": {"price": 49.99, "stock": 8},
}
for product, info in catalog.items():
    if info["stock"] < 20:
        print(f"LOW STOCK: {product} has only {info['stock']} left")
 
 
# Exercise 8
transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200},
]
summary = {}
for t in transactions:
    summary[t["region"]] = summary.get(t["region"], 0) + t["amount"]
 
for region in sorted(summary):
    print(f"{region}: {summary[region]}")
 