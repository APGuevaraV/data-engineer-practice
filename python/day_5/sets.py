set_first = set(range(1, 6))
print(type(set_first))

set_first.add(10)
set_first.remove(4)
print(set_first)

repetidos = [3, 4, 8, 1, 2, 6, 0, 7, 5, 3, 1, 3, 6, 8, 6, 3, 2, 4, 6, 7]
sin_rep = set(repetidos)
print(sin_rep)
super_set = set_first.union(sin_rep)
print(super_set)

super_set = set_first.intersection(sin_rep)
print(super_set)

super_set = set_first.issubset(sin_rep)
print(super_set)

lista = list(sin_rep)
lista.sort(reverse=True)
print(lista)

lista = sorted(list(sin_rep), reverse=True)
print(lista)
