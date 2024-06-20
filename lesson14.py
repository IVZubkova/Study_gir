
def tuple_list_exemple():
    t = (1, 2, 3)
    l = [1, 2, 3]
    print(type(t))
    print(type(l))
    print(t == l)
    print(list(t) == l)
    print(tuple(l) == t)
    print('\nизменяемость list:')
    print(id(l))
    l.append(4)
    print(l)
    print(id(l))
    print('\nнеизменяемость tuple:')
    print(id(t))
    t = (*t, 4)
    print(id(t))
    print('\nсхожесть:')
    for i in l:
        print(i, end='')
    print('')
    for i in t:
        print(i, end='')
    print('')

def set_exemple():
    #set - множество элементов
    a = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
    s = set(a)
    print(s)
    print(sorted(set('hello world')))
    print(ord('a'), ord('A'))
    print(chr(97), chr(65))
    print([chr(i) for i in range(900, 1000)])
    print('\nhash')
    try:
       print({[1, 2, 3], [3, 2, 1], [1, 2]})
    except Exception as ex:
       print(ex)
    h = [(1, 2, 3), (3, 2, 1), (1, 2)]
    print(set(h))
    print([hash(e) for e in h])
    print([hash(e) for e in 'hello world'])






if __name__ == '__main__':
    set_exemple()

