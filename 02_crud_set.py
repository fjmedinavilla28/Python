set_countries = {'col', 'mex', 'bol'}
size = len(set_countries)
print(size)

print('col' in set_countries)
print('pe' in set_countries)

#add

set_countries.add('pe')
print(set_countries)

#update

set_countries.update({'ar','ecua','pe'})
print(set_countries)

#remove
set_countries.remove('ar')
print(set_countries)

#no genera error porque no existe arg, solo dice que no está.

set_countries.discard('arg')
print(set_countries)

set_countries.add('arg')
print(set_countries)

#borra absolutamente todo, no deja nada, un borrado de bajo nivel

set_countries.clear()
print(set_countries)
print(len(set_countries))
