try:
    file_a = open('RRR.txt', 'r')
except FileNotFoundError:
    print("Please check your file")
