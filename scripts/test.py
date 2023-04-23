from collections import OrderedDict

def Test():

    D = OrderedDict({(0, 1): -192.5, (1, 3): -195.0, (1, 2, 3, 4): -195.0, (0, 1, 2): 192.5, (2,): 487.5, (2, 4): -195.0})

    # with open("out.txt", "w") as f:
    #     for key, value in D.items():
    #         key_str = str(key).replace(" ", "")  # convert tuple key to a string without spaces
    #         f.write(key_str+":"+str(value)+", ")


    with open("output.txt", "w") as f:
        print(D, file=f)
Test()