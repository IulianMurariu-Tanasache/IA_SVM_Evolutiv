import random
import numpy as np

class GATE:
    def __init__(self, dataset, epochs, mutation_rate):
        self.x = [np.asarray(dataset[0]) for x in dataset]
        self.y = [dataset[1] for x in dataset]
        self.alpha = [random.random() for x in dataset]
        self.length = len(dataset)
        self.b = random.random()
        self.mutation_rate = mutation_rate
        self.epochs = epochs
        self.early_stop = 3
        self.error = 0.001

    def fitness(self):
        alpha_sum = np.cumsum(self.x)
        sum = 0
        for i in range(0, self.length):
            for j in range(0, self.length):
                product = np.cumsum(np.dot(self.x[i], self.x[j]))
                product = product * self.alpha[i] * self.alpha[j] * self.y[i] * self.y[j]
                sum += product
        return -1 * alpha_sum + 0.5 * sum

    def elitism(self, pop):
        best_pop = None
        best_pop_fitness = 0
        for x in pop:
            curr_fitness = self.fitness(x)
            if curr_fitness > best_pop_fitness:
                best_pop_fitness = curr_fitness
                best_pop = x
        return best_pop

    def tournir_selection(self, pop):
        tournir = [x for x in pop]
        participation = [False for x in tournir]
        fitness_score = [self.fitness(x) for x in tournir]

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
        new_pop = [x for x in pop]
        old_pop = [x for x in pop]
        gamma = random.random()

        while len(old_pop) > 0:
            i = random.randrange(0, len(old_pop))
            p1 = old_pop.pop(i)

            if len(old_pop) == 0:
                break

            i = random.randrange(0, len(old_pop))
            p2 = old_pop.pop(i)

            for i in range(len(p1)):
                c1 = gamma * p1[i] + (1 - gamma) * p2[i]
                c2 = gamma * p2[i] + (1 - gamma) * p1[i]
                new_pop.append(c1)
                new_pop.append(c2)

        return new_pop
                

    def mutation(self, pop):
        new_pop = []
        for x in pop:
            if random.random() < self.mutation_rate:
                mutated_pop = []
                g1 = int(random.random() * (len(x)))
                g2 = int(random.random() * (len(x)))
                for i in range(0, len(x)):
                    mutated_pop.append(x[i])
                print(mutated_pop)
                aux = mutated_pop[g1]
                mutated_pop[g1] = mutated_pop[g2]
                mutated_pop[g2] = aux
                print(mutated_pop)
                new_pop.append(mutated_pop)
            else:
                new_pop.append(x)

    def run_algorithm(self):
        curr_fitness = 0
        no_change = 0
        for ep in range(0, self.epochs):
            best_pop = self.elitism(self.alpha)
            best_pop_fitness = self.fitness(best_pop)
            #adjustment here
            if np.abs(curr_fitness - self.error) <= best_pop_fitness <= np.abs(curr_fitness + self.error):
                no_change += 1
                if no_change > self.early_stop:
                    break
            new_pop = self.tournir_selection(self.alpha)
            new_pop = self.crossover(new_pop)
            new_pop = self.mutation(new_pop)
            #adjustment here
            self.alpha = new_pop
        return self.alpha, self.bias_computation()


    def bias_computation(self):
        outer_sum = 0
        for i in range(0,self.length):
            inner_sum = 0
            for j in range(0,self.length):
                product = np.cumsum(np.dot(self.x[i], self.x[j]))
                inner_sum += self.y[j] * self.alpha[j] * product
            outer_sum += self.y[i] - inner_sum
        return (1 / self.length) * outer_sum




