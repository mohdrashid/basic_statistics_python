import random
height = {"min": 90, "max": 200}
weight = {"min": 40, "max": 90}

population = []
firstName = ["Mohammed","Ahmed","Ram","Agash","John","Yahya","Jamal","Reem","Clara","Christina"]
lastName = ["Mohammed","Ahmed","Ram","Agash","John","Yahya","Jamal"]

size = 10000

for i in range(0,size):
    name=firstName[random.randint(0,len(firstName)-1)]+" "+lastName[random.randint(0,len(lastName)-1)]
    population.append({
        "name": name,
        "id": i+1,
        "height": random.randint(height["min"],height["max"]),
        "weight": random.randint(weight["min"],weight["max"])
    })

observations = {
    "height": {
        "mean": 0,
        "min": height["max"],
        "max": height["min"],
        "median": {
            "Q1": 0,
            "Q2": 0,
            "Q3": 0
        }
    },
    "weight": {
        "mean": 0,
        "min": weight["max"],
        "max": weight["min"],
        "median": {
            "Q1": 0,
            "Q2": 0,
            "Q3": 0
        }
    }
}

i = 0
for i in range(0,size):
    for observation in observations:
        observations[observation]["mean"] += population[i][observation]
        if population[i][observation] < observations[observation]["min"]:
           observations[observation]["min"] = population[i][observation]
        if population[i][observation] > observations[observation]["max"]:
            observations[observation]["max"] = population[i][observation]

for observation in observations:
    observations[observation]["mean"] /= i*1.0
    sortedList = sorted(population, key=lambda k: k[observation])
    if size % 2 == 0:
        Q2 = (sortedList[size/2-1][observation]+sortedList[size/2][observation])/2
    else:
        Q2 = sortedList[size/2-1][observation]
    Q1 = sortedList[(size / 2 - 1) / 2][observation]
    Q3 = sortedList[((size / 2) + (size-1)) / 2][observation]
    observations[observation]["median"]["Q2"] = Q2
    observations[observation]["median"]["Q1"] = Q1
    observations[observation]["median"]["Q3"] = Q3

print observations
