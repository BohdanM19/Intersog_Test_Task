import pickle

with open("numbers.dat", "rb") as file:
    a = pickle.load(file)
    b = pickle.load(file)
    c = pickle.load(file)
    d = pickle.load(file)
    file.close()
Test_array = a + b + c + d
print("Amount of numbers are: {}".format(len(Test_array)))
zero = 0
one = 0

two_numbers = [0, 0, 0, 0]
three_numbers = [0, 0, 0, 0, 0, 0, 0, 0]

for i in range(0, len(Test_array)):
    if Test_array[i] == 0:  # start 1 task
        zero += 1
    else:
        one += 1  # end 1 task

    if i != len(Test_array) - 2 and i != len(Test_array) - 1:  # start 2 and 3 task
        three = str(Test_array[i]) + str(Test_array[i + 1]) + str(Test_array[i + 2])
        three = int(three, 2)
        three_numbers[three] += 1

    if i != len(Test_array) - 1:
        two = str(Test_array[i]) + str(Test_array[i + 1])
        two = int(two, 2)
        two_numbers[two] += 1  # end 2 and 3 task

# Task 4
print("All array consists of:")
print("0 - {}%".format(round((zero * 100) / len(Test_array), 2)))
print("1 - {}%".format(round((one * 100) / len(Test_array), 2)))

print("2 symbols combination")
two_numbers_headers = ("00", "01", "10", "11")
for i, h in zip(two_numbers, two_numbers_headers):
    print("{} meets {} times and is {}%".format(h, i, round(((i * 100) / (len(Test_array) - 1)), 2)))

print("3 symbols combination")
three_numbers_headers = ("000", "001", "010", "011", "100", "101", "110", "111")
for i, h in zip(three_numbers, three_numbers_headers):
    print("{} meets {} times and is {}%".format(h, i, round(((i * 100) / (len(Test_array) - 2)), 2)))
