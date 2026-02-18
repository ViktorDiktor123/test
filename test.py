import sys

data = []

x = int(input('x: '))
if x == 0: # Divide by 0 protection
    sys.exit('Error: null')

lens = int(input('len: '))

for a in range(lens): # add data
    data.append(int(input(f'{a+1} num: ')))

for a in range(len(data)): # looking for a multiple
    if max(data) // x < max(data) / x:
        data.remove(max(data))
    else:
        sys.exit(f'num: {max(data)}')
