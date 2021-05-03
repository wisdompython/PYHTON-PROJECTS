student_marks = [['kola', 67, 43, 66],
                 ['ife', 90, 98, 87],
                 ['tobi', 88, 90, 96],
                 ['edima', 87,77, 90]
                ]
each_total_test = []
num_test = len(student_marks[0]) - 1
num_students = len(student_marks)
for test_index in range (num_test):
    each_total_test.append(0)
for student_index in range(num_students):
    for test_index in range(num_test):
        each_total_test[test_index] += student_marks[student_index][test_index + 1]
each_total_average = []
for test_index in range(num_test):
    each_total_average.append(each_total_test[test_index]/len(student_marks))
for test_index in range(num_test):
    print('the average test ' + str (test_index + 1) + ' is ' + \
          str(each_total_average[test_index]))