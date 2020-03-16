#function receives two grades per student and prints the highest scoring subjects with the student's name
def compare_subjects_within_student(subj1_all_students,subj2_all_students):
    history={
        'Rick': [100, 99], 'Morty': [78, 61], 'Beth':[90, 80], 'Summer':[69, 71], 'Jerry':[31, 78]
            }
    math={
        'Rick': [98, 97], 'Morty': [81, 71], 'Beth':[94, 89], 'Summer':[75, 49], 'Jerry':[50, 51], 'Birdperson':[92,87]
        }

    list1=list(set(subj1_all_students) & set(subj2_all_students))

    for value in list1:
        if max(history[value])>max(math[value]):
            max_grade='History'
        else:
            max_grade='Math'
        print (value, max_grade)
 
subj1_all_students=('Rick', 'Morty','Beth','Jerry','Summer')
subj2_all_students=('Rick', 'Morty','Beth','Jerry','Summer','Birdperson')
 
compare_subjects_within_student(subj1_all_students,subj2_all_students)

