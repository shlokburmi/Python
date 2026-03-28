marks={
    "harry": 85,
    "rohan": 78,
    "skillf": 56,
    0:"Suresh"

}

print(marks["harry"])

print(marks.items())
print(marks.keys())

marks.update({"harry": 90})
print(marks["harry"])

print(marks.get("harry"))

print(marks.get("Harry"))  #prints none




