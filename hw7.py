names = ("Ross","Rachel","Chandler","Monica","Joey","Phoebe")
friends_list = set()

for name in names:
    names_ = input(f'{name}, enter the names of the friends you invited: ')
    name_list = names_.split()
    for name in name_list:
        friends_list.add(name)

print('This is final list of people invited:')
for count, name in enumerate(friends_list, start=1):
    print(count, '.', name)