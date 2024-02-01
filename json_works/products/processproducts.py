from json import load

f=open("C:\\Users\\Admin\\Desktop\\mypython\\json_works\\products\\data.json","r",encoding="UTF-8")
data=load(f)

# q1--> print total no.of products
# print(len(data))

#q2-->print all product name
product_names=[p.get("title") for p in data]
# print(product_names)

# q3-->print all categories
all_categories=[p.get("category") for p in data]
# print(set(all_categories))

# q4-->print all product name available under rs 50

price_filter=[p.get("title") for p in data if p.get("price")<=50]
# print(price_filter)

# q5-->print all jwellery products name
category_filter=[p.get("title") for p in data if p.get("category")=="jewelery"]
# print(category_filter)

# q6-->costly_product
def get_price(dictionary):
    return dictionary.get("price")
costly_product=max(data,key=get_price)
# print(costly_product.get("title"),costly_product.get("price"))
# print(costly_product.get("price"))

# q7-->cheapest product
cheapest_product=min(data,key=get_price)
# print(cheapest_product.get("title"),cheapest_product.get("price"))

# q8-->product title,rating count
review_count=[(p.get("title"),p.get("rating").get("count")) for p in data]
#print(review_count)

# q9-->print title of top rating count
def get_rating_count(dictionary):
    return (dictionary.get("rating").get("count"))
top_review_count=max(data,key=get_rating_count)
print(top_review_count.get("title"),top_review_count.get("rating").get("count"))

