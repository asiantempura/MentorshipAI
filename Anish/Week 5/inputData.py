def func(in1: list[int], in2: int):
    out1 = []

    for i in in1:
        if i <= in2:
            out1.append(i)
        else:
            print(f'{i} > {in2}')

    return out1
    
