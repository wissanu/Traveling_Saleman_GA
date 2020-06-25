from TSP import FN_TSP as ga

# create Cities and Route distance

cities = [1,2,3,4]
distance = [[0, 5, 40, 15],
            [10, 0, 40, 30],
            [5, 20, 0, 30],
            [30, 25, 20, 0]]

number_generation = 20
pop_num = 4
gene_num = len(cities)
best_chromosome = []
best_fitness = 99999


# generation loop main function

if __name__ == '__main__':

    for gen in range(1, number_generation + 1):
        print('generation', gen)
        if gen == 1:
            chromosome_2 = ga.random_chromosome1(pop_num,gene_num)
        else:
            chromosome_2 = chromosome_child2

        # add elitism
        if gen != 1 and best_chromosome not in chromosome_2:
            chromosome_2[0] = best_chromosome

        print('chromosome', chromosome_2)

        chromosome_child2 = ga.PMX_CROSSOVER(chromosome_2,pop_num,gene_num)
        print('child', chromosome_child2)

        chromosome_child2 = ga.mutation(chromosome_child2,gene_num)
        print('mutaion', chromosome_child2)

        route_2 = ga.find_fitness(chromosome_child2,distance)
        print('fitness', route_2)

        if min(route_2) < best_fitness:
            min_index = route_2.index(min(route_2))
            best_chromosome = chromosome_child2[min_index]
            best_fitness = min(route_2)

    # best solution
    print("================")
    print("best fitness:", best_fitness)
    print("best chromosome :",best_chromosome)
    print("route : ",best_chromosome[0],"->",best_chromosome[1],"->",best_chromosome[2],"->",best_chromosome[3],"->",best_chromosome[0])
