people=[
    {"name": "coco", "age": 17},
    {"name": "kate", "age": 25},
    {"name": "john", "age": 15},
    {"name": "lisa", "age": 21},

]
filtered_people = list(filter(lambda p: p["age"] >= 18, people)) #to filter out the names under 18
remaining_people = list(map(lambda p: p['name'], filtered_people)) # map remaining people name
print(remaining_people) #print the names
