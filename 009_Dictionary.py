fish = {'name': "Nemo", 'hands': "fins", 'special': "gills"}
dog = {'name': "Clifford", 'hands': "paws", 'color': "red"}
birds = {'name': "Chizhik", 'hands': "wings", 'breeding': "eggs"}

dog.update(fish)
birds.update(dog)

print (birds)

