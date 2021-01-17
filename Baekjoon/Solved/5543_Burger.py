Burger = []
Drink = []
Set = []

for I in range(3):
    Burger.append(int(input()))
for I in range(2):
    Drink.append(int(input()))

for I in range(3):
    for J in range(2):
        Set.append(Burger[I] + Drink[J])
        
print(min(Set) - 50)
