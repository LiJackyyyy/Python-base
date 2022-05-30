import time


start_All = time.time()

start_a = time.time()
print("A")
time.sleep(1.5)
end_a = time.time()
print('A', end_a - start_a)

start_b = time.time()
print('B')
time.sleep(2)
end_b = time.time()
print("B", end_b - start_b)

end_All = time.time()
print(end_All - start_All)