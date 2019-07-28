def order(args):
    return args


@order
def reversed_arguments(argum):
    arggs = []
    for arg in argum:
        arggs.append(arg)
    return arggs[::-1]


print(reversed_arguments('567'))