import math
import timeit
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import metpy.calc as mpcalc

def insertion_sort(data):
    for i in range(1, len(data)):
      if data[i] < data[i-1]:
        for j in range(i):
          last = i-j
          if not data[last-1] < data[last]:
              data[last-1], data[last] = data[last], data[last-1]

def merge_sort(data):
    mid = len(data) // 2 
    left = data[:mid]
    right = data[mid:]

    if len(data) > 1:

        merge_sort(left)
          
        merge_sort(right)

        leftPos = 0
        rightPos = 0
        mergePos = 0

        while (leftPos < len(left) and rightPos < len(right)):
            if left[leftPos] < right[rightPos]:
                data[mergePos] = left[leftPos]
                leftPos += 1
            else:
                data[mergePos] = right[rightPos]
                rightPos += 1
            mergePos += 1
            
        while (leftPos < len(left)):
            data[mergePos] = left[leftPos]
            leftPos += 1
            mergePos += 1
            
        while (rightPos < len(right)):
            data[mergePos] = right[rightPos]
            rightPos += 1
            mergePos += 1

def get_insertion_time():
    SETUP_CODE = '''from __main__ import insertion_sort,i;import random'''
    
    TEST_CODE = '''
randomlist = random.sample(range(0, 5000), i)
insertion_sort(randomlist)
'''

    time = timeit.timeit(setup=SETUP_CODE,
                          stmt=TEST_CODE,
                          number=3)
    
    return time

def get_merge_time():
    SETUP_CODE = '''from __main__ import merge_sort,i;import random'''
    
    TEST_CODE = '''
randomlist = random.sample(range(0, 5000), i)
merge_sort(randomlist)
'''

    time = timeit.timeit(setup=SETUP_CODE,
                          stmt=TEST_CODE,
                          number=3)
    
    return time

sum = 0
num = 1000
show_graph = True
nums = []

for i in range(10):
    data = {
        "num_of_inputs": [],
        "insertion_time": [],
        "merge_time": []
    }

    data['num_of_inputs'] = [x for x in range(num)]

    print('Testing Insertion Sort...')
    for i in range(num):
        time = get_insertion_time()
        data['insertion_time'].append(time)

    print('Testing Merge Sort...')
    for i in range(num):
        time = get_merge_time()
        data['merge_time'].append(time)


    xi = np.array(data['num_of_inputs'])
    y1 = np.array(data['insertion_time'])
    y2 = np.array(data['merge_time'])

    x, y = mpcalc.find_intersections(xi, y1, y2)

    x = [float(max(list(x.real)))]
    print(math.floor(x[0]))

    nums.append(math.floor(x[0]))
    sum += math.floor(x[0])

    if show_graph:
        df = pd.DataFrame(data)
        ax1=df.plot(kind='line', x='num_of_inputs', y='insertion_time', color='r', label='Insertion Sort')

        ax1=df.plot(kind='line', x='num_of_inputs', y='merge_time', color='b', label='Merge Sort', ax=ax1)

        ax1.set_title('Insertion Sort vs. Merge Sort (Time Complexity)')
        ax1.set_xlabel('Number of Inputs (n)')
        ax1.set_ylabel('Time (seconds)')

        plt.axvline(x, color='gold', label='Intersection')

        plt.legend()
        plt.show()


print('\n\n\nHere is the list of sums')
[print(f'{x}\n') for x in nums]
print(f'The Average Num of Inputs is {sum/10}')