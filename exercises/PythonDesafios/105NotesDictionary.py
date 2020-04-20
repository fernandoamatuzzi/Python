def grades(*n, sit=False):
    '''
    -> Function to analyze grades and situation of students.
    :param n: one or more grades from students.
    :param sit: optional value, to show or not the situation of the student.
    :return: dictionary with info regarding the situation of the class.
    '''
    notes = dict()
    notes['total'] = len(n)
    notes['highest'] = max(n)
    notes['lowest'] = min(n)
    notes['average'] = sum(n)/len(n)
    if sit:
        if notes['average'] == 10:
            notes['situation'] = 'PERFECT!'
        elif notes['average'] >= 8.5:
            notes['situation'] = 'EXCELENT'
        elif notes['average'] >= 7:
            notes['situation'] = 'GOOD'
        elif notes['average'] >= 6:
            notes['situation'] = 'ACCEPTABLE'
        else:
            notes['situation'] = 'BAD'
    return notes

r = grades(0, 9, 8.5, sit=True)
print(r)
# help(grades)
