number_times = int(input('Number of iterations: '))
previous_number_1=0
previous_number_2=1
for i in range(number_times):
    temp_number = previous_number_1
    previous_number_1 += previous_number_2
    previous_number_2 = temp_number
    print(str(previous_number_1))