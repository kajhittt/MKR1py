from sort_by_area import sort_by_area  
from sort_by_population import sort_by_population

def read_and_sort(file_path):
    with open(file_path, "r") as file:
        data = []
        for line in file:
            country, area, population = line.strip().split(", ")
            data.append([country, float(area), int(population)])

    sorted_by_area = sort_by_area(data)
    sorted_by_population = sort_by_population(data)

    return sorted_by_area, sorted_by_population