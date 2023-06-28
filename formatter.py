    
data = [{'damage': 14163, 'exp': 404, 'kills': 2, 'reward': 29042},
 {'damage': 2931, 'exp': 149, 'kills': 0, 'reward': 15387},
 {'damage': 11908, 'exp': 1819, 'kills': 5, 'reward': 22256},
 {'damage': 7054, 'exp': 376, 'kills': 0, 'reward': 21463},
 {'damage': 1029, 'exp': 2837, 'kills': 2, 'reward': 23403},
 {'damage': 11182, 'exp': 148, 'kills': 4, 'reward': 22866},
 {'damage': 14447, 'exp': 877, 'kills': 9, 'reward': 26930},
 {'damage': 3214, 'exp': 1396, 'kills': 3, 'reward': 24564},
 {'damage': 9187, 'exp': 2389, 'kills': 1, 'reward': 18652},
 {'damage': 12000, 'exp': 1094, 'kills': 12, 'reward': 24617},
 {'damage': 10277, 'exp': 1244, 'kills': 10, 'reward': 27386},
 {'damage': 4369, 'exp': 1853, 'kills': 7, 'reward': 19043},
 {'damage': 14952, 'exp': 2332, 'kills': 8, 'reward': 18921},
 {'damage': 8177, 'exp': 298, 'kills': 4, 'reward': 29392},
 {'damage': 4980, 'exp': 799, 'kills': 6, 'reward': 22675},
 {'damage': 14518, 'exp': 2278, 'kills': 3, 'reward': 25722},
 {'damage': 6200, 'exp': 811, 'kills': 4, 'reward': 12377},
 {'damage': 2959, 'exp': 1569, 'kills': 5, 'reward': 10762},
 {'damage': 2993, 'exp': 2971, 'kills': 9, 'reward': 12676},
 {'damage': 8580, 'exp': 102, 'kills': 6, 'reward': 29736}]


def format_number(num):
    num = str(num)
    parts = []
    for i in range(len(num), 0, -3):
        parts.insert(0, num[max(i-3, 0):i])
    
    return ' '.join(parts)


def show_average(dataset, key):
    vals = [i[key] for i in dataset]
    print (key, format_number(sum(vals)//len(vals)))


def show_total(dataset, key):
    vals = [i[key] for i in dataset]
    print (key, format_number(sum(vals)))

show_average(data, 'exp')
show_average(data, 'reward')
print ('total')
show_total(data, 'exp')
show_total(data, 'reward')


