technic_groups = {'Смартфоны': ['нокиа', 'айфон', 'самсунг'], 'Телевизоры': ['самсунг', 'сяоми', 'lg'], 'Клавиатуры': ['Logitech', 'Hyperx']}


search_group = input('Выбери подходящую группу(Смартфоны, Телевизоры, Клавиатуры): ')

if search_group == 'Смартфоны' or search_group == 'Телевизоры' or search_group == 'Клавиатуры':
    print(technic_groups[search_group])
