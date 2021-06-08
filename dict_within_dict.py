wedding_item = {'Alice' : {'sufurias' : 3, 'plates' : 12, 'watches' : 1},'+\
                ''Brayo' : {'radio' : 1, 'watches' : 2, 'blenders' : 1},'+\
                ''Cyndie' : {'plates' : 24, 'juicers' : 2, 'blenders' : 1,'television_sets' : 1, 'sufurias' : 4 }}

def gift_totals(gift_list, item):
    for names in gift_list:
        count = 0
        present = names.get(names[item], 0)
        count += names[item]
    print(f'{names} brought {count} {item}s')
gift_totals(wedding_item,'sufurias')