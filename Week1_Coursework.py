#SR04 - Bubble Sort
"""
numbers1 = [2.049, 2.398, 2.009, 1.809, 2.894, 2.054, 2.927, 2.848, 2.246, 1.971]
length1 = len(numbers1)
for i in range(length1):
    for j in range(0,length1-i-1):
        if numbers1[j] > numbers1[j+1] :
            numbers1[j], numbers1[j+1] = numbers1[j+1], numbers1[j]
print(numbers1)
"""

#SR05 - Selection Sort
"""
numbers2 = [2.049, 2.398, 2.009, 1.809, 2.894, 2.054, 2.927, 2.848, 2.246, 1.971]
length2 = len(numbers2)
for a in range(length2):
    minimum = a
    for b in range(a+1, length2):
        if numbers2[minimum] > numbers2[b]:
            minimum = b
numbers2[a], numbers2[minimum] = numbers2[minimum], numbers2[a]

print(numbers2)
"""

#SR06
"""
import time
start_time = time.time()
for i in range(10):
    print(i)

end_time = time.time()
print(end_time - start_time)
"""

#SR09
"""
numbers3 = [73, 85, 43, 6, 29]
length3 = len(numbers3)
for c in range(length3) :
    for d in range(0, length3-c-1) :
        if numbers3[d] > numbers3[d+1] :
            numbers3[d], numbers3[d+1] = numbers3[d+1], numbers3[d]
print(numbers3)
"""

#SR10 - Sorted
numbers10 = [2.049, 2.398, 2.009, 1.809, 2.894, 2.054, 2.927, 2.848, 2.246, 1.971]
print(sorted(numbers10))