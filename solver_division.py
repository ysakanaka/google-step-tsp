 #!/usr/bin/env python3

import sys
import math

from common import print_solution, read_input


def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)


def solve(cities):
    N = len(cities)

    dist = [[0] * N for i in range(N)]
    for i in range(N):
        for j in range(N):
            dist[i][j] = dist[j][i] = distance(cities[i], cities[j])

    current_city = 0
    unvisited_cities = set(range(1, N))
    solution = [current_city]

    def distance_from_current_city(to):
        return dist[current_city][to]

    mostfar_city = max(unvisited_cities, key=distance_from_current_city)
    max_distance = distance_from_current_city(mostfar_city)

    maxX_city = max(cities, key = (lambda city: city[0]))
    maxY_city = max(cities, key = (lambda city: city[1]))

    maxX = maxX_city[0]
    maxY = maxY_city[1]

    cities_ul = []
    cities_ll = []
    cities_ur = []
    cities_lr = []

    for i in range(1, N):
        if (cities[i][0] <= maxX/2.0) and (cities[i][1] >= maxY/2.0):
            cities_ul.append(i)
        elif (cities[i][0] <= maxX/2.0) and (cities[i][1] < maxY/2.0):
            cities_ll.append(i)
        elif (cities[i][0] > maxX/2.0) and (cities[i][1] >= maxY/2.0):
            cities_ur.append(i)
        else: cities_lr.append(i)

    while cities_ll:
        next_city = min(cities_ll, key=distance_from_current_city)
        cities_ll.remove(next_city)
        solution.append(next_city)
        current_city = next_city

    while cities_ul:
        next_city = min(cities_ul, key=distance_from_current_city)
        cities_ul.remove(next_city)
        solution.append(next_city)
        current_city = next_city

    while cities_ur:
        next_city = min(cities_ur, key=distance_from_current_city)
        cities_ur.remove(next_city)
        solution.append(next_city)
        current_city = next_city

    while cities_lr:
        next_city = min(cities_lr, key=distance_from_current_city)
        cities_lr.remove(next_city)
        solution.append(next_city)
        current_city = next_city

    return solution

    #while unvisited_cities:
    #    unvisited_cities.remove(next_city)
    #    solution.append(next_city)
    #    current_city = next_city
    #return solution


if __name__ == '__main__':
    assert len(sys.argv) > 1
    solution = solve(read_input(sys.argv[1]))
    print_solution(solution)
