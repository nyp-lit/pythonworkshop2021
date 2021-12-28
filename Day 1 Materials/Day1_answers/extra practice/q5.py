
items = {"TV": 30, "laptop": 20,"refrigerator": 50, "table": 20, "air conditioner": 100}


def findIt(name, items):
    if name not in items:
        print(f"{name} is gone")
    else:
     print(f"{name} is here!")

findIt("laptop", items)
