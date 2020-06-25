from random import randint, seed, sample

# Find Random Chromosome
rand_inx = 1


def random_chromosome1(pop_num, gene_num):
    Random_ind = 1
    chromosome2 = []
    for i in range(pop_num):
        seed(Random_ind)
        chromosome = sample(range(0, gene_num), gene_num)
        chromosome2.append(chromosome)
        Random_ind += 1
    return chromosome2


# Find the fitness

def find_fitness(chromosome2, distance):
    route2 = []
    for x in chromosome2:
        route2.append(distance[x[0]][x[1]] + distance[x[1]][x[2]] + distance[x[2]][x[3]] + distance[x[3]][x[0]])
    return route2


# Create single Crossover
def PMX_CROSSOVER(chromosome2, pop_num, gene_num):
    # find pairs of parent in range of the defined and do pmx crossover
    global rand_inx
    count = 0
    chromosome_child = []

    while count < pop_num:
        seed(rand_inx)
        selected = sample(range(0, gene_num), 2)
        c = pmx_pair(chromosome2[selected[0]], chromosome2[selected[1]])
        if not chromosome_child or c not in chromosome_child:
            chromosome_child.append(c)
            count += 1
        rand_inx += 1

    return chromosome_child


# logical pmx crossover process
def pmx(a, b, start, stop):
    child = [None] * len(a)
    # Copy a slice from first parent:
    child[start:stop] = a[start:stop]

    # Map the same slice in parent b to child using indices from parent a:
    for ind, x in enumerate(b[start:stop]):
        ind += start
        if x not in child:
            while child[ind] is not None:
                ind = b.index(a[ind])
            child[ind] = x

    # Copy over the rest from parent b
    for ind, x in enumerate(child):
        if x is None:
            child[ind] = b[ind]

    return child


# select pair to do pmx process with indicate start and stop point
def pmx_pair(a, b):
    half = len(a) // 2
    start = randint(0, len(a) - half)
    stop = start + half
    return pmx(a, b, start, stop)


def mutation(chromosome_child, gene_num):
    global rand_inx
    # create swap with random two points.
    # the process will end with only 1 chromosome success in mutate.

    seed(rand_inx)
    point = sample(range(0, gene_num), 3)
    # do swap and check if not duplicate.
    temp = chromosome_child.pop(point[2])
    temp[point[0]], temp[point[1]] = temp[point[1]], temp[point[0]]

    if temp not in chromosome_child:
        chromosome_child.insert(point[2], temp)
    elif temp in chromosome_child:
        temp[point[1]], temp[point[0]] = temp[point[0]], temp[point[1]]
        chromosome_child.insert(point[2], temp)
    rand_inx += 1

    return chromosome_child
