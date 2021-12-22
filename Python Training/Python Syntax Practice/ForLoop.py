keyLocation = "chair"
locations = ["bedroom", 'bathroom', "couch", "chair", "Hall", "Kitchen"]

for i in locations:                             ##Like for Each Loop in java
    if keyLocation == i:
        print("Key found in", i)
        break
    else:
        print("key Not found in", i)

for i in range(len(locations)):                 ##Using range Function
    if keyLocation == locations[i]:
        print("Keys Found in", locations[i])
        break
    else:
        print("Keys not Found in", locations[i])

for i in range(5):                              ## Printing on the same lines using for loop
    print(locations[i], end=" ")