### Drug Design Genetic Algorithm 

This algorithm uses a bio-inspired selection process to optimize drug candidates. 

### Importing files and toolkits
```
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
```

### Creating an inital population using substances represented as Simplified Molecular Input Line Entry System (SMILES) Strings. SMILES Strings are a way to represent chemical substances using symbols computers can understand. Parameters are set using Lipinski's Rule of Five. Lipinski's Rule of Five consists of four rules to evaluate how druglike a sustance is. The parameters include the LogP value (permeability of the drug), weight, # of hydrogen Donors, # of hydrogen acceptors. 
```
inital_pop = [''.join(x) for x in data]

for x in inital_pop:
    m = Chem.MolFromSmiles(x)
    logp = Descriptors.MolLogP(m)
    weight = Descriptors.ExactMolWt(m)
    donors = Descriptors.NumHDonors(m)
    acceptors = Descriptors.NumHAcceptors(m)
```
### Each substance will be assigned a score to evaluate its fitness (how druglike it is). Violations of rule(s) in Lipinski's Rule of Five will lower a substances's score. Substances with 4 or more violations will be thrown out and not continue onto the next stage.
```
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
```
### If a substance's score is high enough, it will become a "parent" and generate a new "offspring." Each parent's SMILES String (which contains a list of characters) will have a selection point chosen at random. Two parent's SMILES String will crossover to create a new smiles string will corresponds with a new substance. This creates a new generation of substances that are more likely have be more fit than their parents.
```
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
```
### Creating random mutations to increase diversity. 
```
f = random.choice(parents)
def mutate(individual):
    hola = random.choice(f)
    return f.replace(hola, random.choice(string.ascii_letters), 1)
mutate(f)
```
### Adding any mutated SMILES Strings to the population and throwing out the orginal substance that was not mutated.
```
for idx, item in enumerate(parents):
    if f in item:
        parents[idx] = mutate(f)
```
### Validating whether each substance has a valid SMILES String and is chemically possible. If the string is invalid, it is thrown out. The process continues and more generations are made until the fittest substances make up the final generation. 
```
for item in parents:
    hey = Chem.MolFromSmiles(item)
    if hey is None:
        pass
    else:
        p1.append(item)
print(p1)
```



### Jekyll Themes
