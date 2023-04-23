import pandas as pd

# Load the pickle file
with open('hs1._converted_problem.pickle', 'rb') as f:
    data = pd.read_pickle(f)

# with open('hs1._converted_problem.csv', 'w') as f:

for i in data:
    if type(i) == dict: 
        for n in i.keys():
            if type(n) != tuple:
                a = str(n)+","+str(n)+","+str(i[n])
                #f.write(a)
                #f.write('\n')
                print(a)                  
            else:
                # print(str(n[0])+","+str(n[1])+","+str(i[n])+",\n")
                b = str(n[0])+","+str(n[1])+","+str(i[n])
               # f.write(b)
               # f.write('\n')
                print(b)
