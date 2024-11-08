sets = {
    '': 0,
    'a': 0,
    'b': 0,
    'c': 0,
    'ab': 0,
    'ac': 0,
    'bc': 0,
}
for c in input():
    match c.lower():
        case 'a':
            if sets['bc']:
                sets['bc'] -= 1
                sets[''] += 1
            elif sets['b']:
                sets['b'] -= 1
                sets['ab'] += 1
            elif sets['c']:
                sets['c'] -= 1
                sets['ac'] += 1
            else:
                sets['a'] += 1
                if sets['']:
                    sets[''] -= 1
        case 'b':
            if sets['ac']:
                sets['ac'] -= 1
                sets[''] += 1
            elif sets['a']:
                sets['a'] -= 1
                sets['ab'] += 1
            elif sets['c']:
                sets['c'] -= 1
                sets['bc'] += 1
            else:
                sets['b'] += 1
                if sets['']:
                    sets[''] -= 1
        case 'c':
            if sets['ab']:
                sets['ab'] -= 1
                sets[''] += 1
            elif sets['a']:
                sets['a'] -= 1
                sets['ac'] += 1
            elif sets['b']:
                sets['b'] -= 1
                sets['bc'] += 1
            else:
                sets['c'] += 1
                if sets['']:
                    sets[''] -= 1

print(sets[''])
