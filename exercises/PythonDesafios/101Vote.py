def vote(year):
    from _datetime import date
    current = date.today().year
    age = current - year
    if age < 16:
        return f'Who is {age} years old: DO NOT VOTE.'
    elif 16 <= age < 18 or age > 65:
        return f'Who is {age} years old: OPTIONAL VOTE.'
    else:
        return f'Who is {age} years old: MANDATORY VOTE.'


birth = int(input('What year did you born? '))
print(vote(birth))
