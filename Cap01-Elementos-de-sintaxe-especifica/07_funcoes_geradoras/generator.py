"""cria um generator"""


def main():
    for i in inclusive_range(0,25):
        print(i, end=" ")
    print()


def inclusive_range(*args):
    "Cria um range incluindo o ultimo numero."
    numargs = len(args)
    start=0
    step=1

    if numargs < 1:
        raise TypeError("Esperado ao menos 1 argumento, recebido {}".format(numargs))
    elif numargs == 1:
        stop = args[0]
    elif numargs == 2:
        start = args[0]
        stop = args[1]
        #(start, stop) = args
    elif numargs == 3:
        (start, stop, step) = args
    else:
        raise TypeError("Esperado 3 argumentos, recebido {}".format(numargs))

    #Generator
    i = start
    while i <= stop:
        yield i
        i += step


if __name__=="__main__":main()