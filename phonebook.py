people =[
    {"name" : "Kelly", "number" : "+02-34-234324"},
    {"name" : "David", "number" : "+02-34-543543"}
]
name = input ("Name:")
for person in people :
    if person["name"]== name:
        number= person["number"]
        print(f"Found: {number}")
