import random
import numpy as np
from ajustez import ajustare

class GATE:
    def __init__(self, dataset, epochs, mutation_rate, pop_size):
        self.x = [np.asarray(x[0]) for x in dataset]
        self.y = [x[1] for x in dataset]
        self.dataset = dataset
        self.population_size = pop_size
        self.length = len(dataset)
        self.alpha_pop = [[random.random() for y in range(0,self.length)] for x in range(0, self.population_size)]
        self.b = random.random()
        self.mutation_rate = mutation_rate
        self.epochs = epochs
        self.early_stop = 3
        self.error = 0.001

    def fitness(self, alpha):
        alpha_sum = np.sum(alpha)
        sum = 0
        for i in range(0, self.length):
            for j in range(0, self.length):
                product = np.dot(self.x[i], self.x[j])
                product = product * alpha[i] * alpha[j] * self.y[i] * self.y[j]
                sum += product
        return -1 * alpha_sum + 0.5 * sum

    def elitism(self, pop):
        best_pop = None
        best_pop_fitness = 0
        for alpha in pop:
            curr_fitness = self.fitness(alpha)
            if curr_fitness > best_pop_fitness:
                best_pop_fitness = curr_fitness
                best_pop = alpha
        return best_pop

    def tournir_selection(self, pop):
        tournir = [alpha for alpha in pop]
        participation = [False for alpha in tournir]
        fitness_score = [self.fitness(alpha) for alpha in tournir]

        # turnir
        winners = []
        while len(winners) < len(participation) / 2:
            p1 = random.randrange(0, len(participation))
            while participation[p1] != False:
                p1 = random.randrange(0, len(participation))
                
            p2 = random.randrange(0, len(participation))
            while participation[p2] != False:
                p2 = random.randrange(0, len(participation))

            participation[p1] = True
            participation[p2] = True

            if fitness_score[p1] > fitness_score[p2]:
                winners.append(tournir[p1])
            else:
                winners.append(tournir[p2])

        return winners

    def crossover(self, pop):
        new_pop = [alpha for alpha in pop]
        old_pop = [alpha for alpha in pop]
        
        while len(old_pop) > 0:
            i = random.randint(0, len(old_pop) - 1)
            p1 = old_pop.pop(i)

            if len(old_pop) == 0:
                break

            i = random.randint(0, len(old_pop) - 1)
            p2 = old_pop.pop(i)

            c1 = []
            c2 = []
            for i in range(len(p1)):
                gamma = random.random() # for each or only once?
                c1.append(gamma * p1[i] + (1 - gamma) * p2[i])
                c2.append(gamma * p2[i] + (1 - gamma) * p1[i])
            new_pop.append(c1)
            new_pop.append(c2)

        return new_pop
                

    def mutation(self, pop):
        new_pop = []
        for alpha in pop:
            if random.random() < self.mutation_rate:
                mutated_pop = []
                g1 = random.randint(0, len(alpha) - 1)
                g2 = random.randint(0, len(alpha) - 1)
                for i in range(0, len(alpha)):
                    mutated_pop.append(alpha[i])
                #print(mutated_pop)
                aux = mutated_pop[g1]
                mutated_pop[g1] = mutated_pop[g2]
                mutated_pop[g2] = aux
                #print(mutated_pop) todo: vezi daca face bine
                new_pop.append(mutated_pop)
            else:
                new_pop.append(alpha)
        return new_pop

    def adjustment(self, alpha_pop):
        new_pop = []
        for alpha in alpha_pop:
            new_alpha = ajustare(alpha, self.dataset)
            new_pop.append(new_alpha)
        return new_pop

    def run_algorithm(self):
        curr_fitness = 0
        no_change = 0
        #adjustment here
        new_pop = self.adjustment(self.alpha_pop)
        for ep in range(0, self.epochs):
            best_pop = self.elitism(new_pop)
            best_pop_fitness = self.fitness(best_pop)
            if np.abs(curr_fitness - self.error) <= best_pop_fitness <= np.abs(curr_fitness + self.error):
                no_change += 1
                if no_change > self.early_stop:
                    break
            new_pop = self.tournir_selection(new_pop)
            new_pop = self.crossover(new_pop)
            new_pop.append(best_pop)
            new_pop = self.mutation(new_pop)
            #adjustment here
            new_pop = self.adjustment(new_pop)
            self.alpha_pop = new_pop
        lagrange_mul = self.elitism(self.alpha_pop)
        return lagrange_mul, self.bias_computation(lagrange_mul)


    def bias_computation(self, alpha):
        outer_sum = 0
        for i in range(0,self.length):
            inner_sum = 0
            for j in range(0,self.length):
                product = np.dot(self.x[i], self.x[j])
                inner_sum += self.y[j] * alpha[j] * product
            outer_sum += self.y[i] - inner_sum
        return (1 / self.length) * outer_sum