dirs = '.'
output = ''
readme = ''



def fiter(entry):
    return True


def to_dict():
    p = {}
    g = globals()
    for i in g:
        if not i.startswith('_'):
            p[i] = g[i]
            
    return p

