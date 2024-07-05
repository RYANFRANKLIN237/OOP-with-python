birthdays = {'alice': 'april 1' ,'bob':'dec 12', 'carol': 'march 4'}
while True:
    print('Enter a name:')
    name = input()
    if name in birthdays:
        print(birthdays[name] + '' ' is the birthday of ' + name)
    else:
        print('there is no birthday information for ' + name)
        print('what is their birthday?')
        birthday = input()
        birthdays[name] = birthday
        print('birthday information updated.')
    break