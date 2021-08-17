from rdkit import Chem
from rdkit.Chem import Descriptors
import random
import csv
import random
import string
with open('file.csv' , newline ='') as f:
    reader = csv.reader(f)
    data = list(reader)
    f.close()


inital_pop = [''.join(x) for x in data]

for x in inital_pop:
    m = Chem.MolFromSmiles(x)
    logp = Descriptors.MolLogP(m)
    weight = Descriptors.ExactMolWt(m)
    donors = Descriptors.NumHDonors(m)
    acceptors = Descriptors.NumHAcceptors(m)
total = []
if logp <= 5:
    total.append(1)
if weight <= 500:
    total.append(1)
if donors <= 5:
    total.append(1)
if acceptors <= 10:
    total.append(1)
for x in inital_pop:
    if sum(total) ==4:
        break
    if sum(total) ==3:
        break
    if sum(total) ==2:
        break
    if sum(total) ==1:
        pass
    if sum(total) ==0:
        pass


first = []
second = []
parents = []
p1 = []
for i in range(50):
    x = random.choice(inital_pop)
    first.append(x[:len(x) // 2])
    second.append(x[len(x) // 2:])
    tot = second + first
    parents.append(random.choice(tot) + random.choice(tot))

f = random.choice(parents)
def mutate(individual):
    hola = random.choice(f)
    return f.replace(hola, random.choice(string.ascii_letters), 1)
mutate(f)

for idx, item in enumerate(parents):
    if f in item:
        parents[idx] = mutate(f)

for item in parents:
    hey = Chem.MolFromSmiles(item)
    if hey is None:
        pass
    else:
        p1.append(item)
print(p1)




