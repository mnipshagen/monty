# 2 was the wrong index, the populations are at index 1
def get_total_pop(cities, idx=1):
    '''
    Returns the total population of cities given in tuples in a list

    Args:
        cities: list of city tuples
        idx: the index of the population number in the city tuples, defaults to 1

    Return:
        The sum of all population numbers in the list
    '''

    total_population = 0

    # get summed up population of all cities in list 'cities'
    for city in cities:
        total_population += city[idx]

    return total_population


# one city: (city name, population, federal state)
cities = [('Osnabrück',165000,'Lower Saxony'),('Münster',311000,'North Rhine-Westphalia'),('Bielefeld',333000,'North Rhine-Westphalia')]
get_total_pop(cities)
