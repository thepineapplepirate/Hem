
import argparse
from collections import OrderedDict
import json
import pickle


def Hamiltonian(in_file, OutFile):

    f = open(in_file) 
    lines = f.readlines()

    hem_1_ord = {}
    hem_higher_ord = {}

    for line in lines:
        h = []
        for i ,x, in enumerate(line.split('*')[1].strip('\n')[::-1]):           
            if x.upper() == 'Z':
                h.append(i)
 
        if len(h)  == 1:
            #hem_1_ord[h[0]] = float(''.join(line.split('*')[0].split(' ')))
            hem_1_ord[h[0]] = float(line.split('*')[0])
        elif len(h) > 1:
            #hem_higher_ord[tuple(h)] = float(''.join(line.split('*')[0].split(' ')))
            hem_higher_ord[tuple(h)] = float(line.split('*')[0])

    with open(OutFile, "w") as f:
        f.write("[")
        up = []
        for n in hem_1_ord, hem_higher_ord:
            l = []
            for key, value in n.items():
                key_str = str(key).replace(" ", "")  # convert tuple key to a string without spaces
                l.append(key_str+": "+str(value))
            up.append("{"+', '.join(l)+"}")

        f.write(', '.join(up))
        f.write(", 0]")

    print([hem_1_ord, hem_higher_ord, 0])

    with open('Hem_out.pickle', 'wb') as f:
        pickle.dump([hem_1_ord, hem_higher_ord, 0], f)



if __name__=="__main__":

    parser = argparse.ArgumentParser(description='Process input file')
    parser.add_argument('input_file', type=str, help='input file path')
    parser.add_argument('output_file', type=str, help='output file path')

    args = parser.parse_args()

    Hamiltonian(args.input_file, args.output_file)
