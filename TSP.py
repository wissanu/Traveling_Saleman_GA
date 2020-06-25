from random import randint, seed, sample

# create Cities and Route distance

cities = [1,2,3,4]
distance = [[0, 5, 40, 15],
            [10, 0, 40, 30],
            [5, 20, 0, 30],
            [30, 25, 20, 0]]

number_generation = 10
pop_num = 4
gene_num = len(cities)
best_chromosome = []
best_fitness = 999999
rand_inx = 1

# Find Random Chromosome

def random_chromosome1():
    Random_ind = 1
    chromosome2 = []
    for i in range(pop_num):
        seed(Random_ind)
        chromosome = sample(range(0, gene_num), gene_num)
        chromosome2.append(chromosome)
        Random_ind = Random_ind + 1
    return chromosome2


# Find the fitness

def find_fitness(chromosome2):
    route2 = []
    for x in chromosome2:
        sumroute2 = distance[x[0]][x[1]] + distance[x[1]][x[2]] + distance[x[2]][x[3]]
        route2.append(sumroute2)
    return route2


# Create single Crossover
def PMX_CROSSOVER(chromosome2):
    # find pairs of parent in range of the defined and do pmx crossover
    global rand_inx
    count = 0
    chromosome_child = []

    while (count<pop_num):
        seed(rand_inx)
        selected = sample(range(0, gene_num), 2)
        c, d = pmx_pair(chromosome2[selected[0]], chromosome2[selected[1]])
        if not chromosome_child or c not in chromosome_child :
            chromosome_child.append(c)
            count = count + 1
        rand_inx = rand_inx + 1

    return chromosome_child

# logical pmx crossover process
def pmx(a,b, start, stop):
    child = [None]*len(a)
    # Copy a slice from first parent:
    child[start:stop] = a[start:stop]

    # Map the same slice in parent b to child using indices from parent a:
    for ind,x in enumerate(b[start:stop]):
        ind += start
        if x not in child:
            while child[ind] != None:
                ind = b.index(a[ind])
            child[ind] = x

    # Copy over the rest from parent b
    for ind,x in enumerate(child):
        if x == None:
            child[ind] = b[ind]

    return child

# select pair to do pmx process with indicate start and stop point
def pmx_pair(a,b):
    half = len(a) // 2
    start = randint(0, len(a)-half)
    stop = start + half
    return pmx(a,b,start,stop) , pmx(b,a,start,stop)

def mutation(chromosome_child):

    global rand_inx
    # create swap with random two points.
    # the process will end with only 1 chromosome success in mutate.

    seed(rand_inx)
    point = sample(range(0, gene_num), 3)
    # do swap and check if not duplicate.
    temp = chromosome_child.pop(point[2])
    temp[point[0]], temp[point[1]] = temp[point[1]], temp[point[0]]

    if temp not in chromosome_child:
        chromosome_child.append(temp)
    elif temp in chromosome_child:
        temp[point[1]], temp[point[0]] = temp[point[0]], temp[point[1]]
        chromosome_child.append(temp)
    rand_inx = rand_inx + 1

    return chromosome_child


# generation loop main function

if __name__ == '__main__':

    for gen in range(1, number_generation + 1):
        print('generation', gen)
        if gen == 1:
            chromosome_2 = random_chromosome1()
        else:
            chromosome_2 = chromosome_child2

        # add elitism
        if gen != 1 and best_chromosome not in chromosome_2:
            chromosome_2[0] = best_chromosome

        print('chromosome', chromosome_2)

        chromosome_child2 = PMX_CROSSOVER(chromosome_2)
        print('child', chromosome_child2)

        chromosome_child2 = mutation(chromosome_child2)
        print('mutaion', chromosome_child2)

        route_2 = find_fitness(chromosome_child2)
        print('fitness', route_2)

        if min(route_2) < best_fitness:
            min_index = route_2.index(min(route_2))
            best_chromosome = chromosome_child2[min_index]
            best_fitness = min(route_2)

    # best solution
    print("================")
    print("best fitness:", best_fitness)
    print("best chromosome :",best_chromosome)
