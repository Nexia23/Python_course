solution_student = []  # Das ist eine Liste in der eure Antworten gespeichert werden :)

# Assignment 00:
# x = 1
# y = 1
# x == y ?? True or False ?

solution_student.append(True)  # Hier wird die erste Antwort an die Liste gehangen.

# Assignment 01:
# x = [1,2]
# y = [1,2]
# x == y ?? True or False ?

solution_student.append()

# Assignment 02:
# x = [1,2]
# y = [1,2]
# x is y ?? True or False ?

solution_student.append()

# Assignment 03:
# x = [1,2]
# y = x
# x == y ?? True or False ?

solution_student.append()

# Assignment 04:
# x = [1,2]
# y = x
# x is y ?? True or False ?

solution_student.append()

# Assignment 05:
# x = 5
# y = 5
# x is y ?? True or False ?

solution_student.append()

# Assignment 06:
# x = 5
# y = x
# x = 6
# x == y ?? True or False ?

solution_student.append()

# Assignment 06:
# x = 2
# y = x
# x = x + 1
# x == y ?? True or False ?

solution_student.append()

# Assignment 06:
# x = [1,2]
# y = x
# x.append(3)
# x is y ?? True or False ?

solution_student.append()

if __name__ == '__main__':
    import _pickle
    with open('./solution/solution_1.pkl', 'rb') as solution_file:
        solution_tutors = _pickle.load(solution_file)
    if solution_tutors == solution_student:
        print('Solved!')
    else:
        print('Try Again!')
