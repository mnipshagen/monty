# one city: (city name, population, federal state)
cities = [('Osnabrück',165000,'Lower Saxony'),('Münster',311000,'North Rhine-Westphalia'),('Bielefeld',333000,'North Rhine-Westphalia')]


total_population = 0

# get summed up population of all cities in list 'cities'
for city in cities:
    total_population += city[2]
