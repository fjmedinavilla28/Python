#operaciones de conjuntos
#unión de dos conjuntos

set_a = {'col','mex','bol'}
set_b = {'bol','pe'}
set_c = set_a.union(set_b)
print(set_c)

#con operadores matemáticos
print(set_a|set_b)

#intersección de conjuntos
set_c = set_a.intersection(set_b)
print(set_c)

#con operadores matemáticos
print(set_a & set_b)

#diferencia de condjuntos
set_c = set_a.difference(set_b)
print(set_c)

#con operadores matemáticos
print(set_a - set_b)

#diferencia simétrica simétrica
set_c = set_a.symmetric_difference(set_b)
print(set_c)

#con operadores matemáticos
print(set_a ^ set_b)
