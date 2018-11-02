def for1():
    print("Start for1")
    for i in range(1, 10):
        print(i)
    print('Finish for1')

def for2():
    print('Start for2')
    array=['A','B','C']
    for a in array:
        print (a)
    print('Finish for2')

def for3():
    print('Start for3')
    persones={'first_name':'Slava', 'lastname':'Starusev', 'age':50}
    for persone in persones.values():
        print(persone)
    print('Finish for3')

    def for4():
        print('Start for4')
        persones = {'first_name': 'Slava', 'lastname': 'Starusev', 'age': 50}
        for persone in persones.keys():
            print(persone)
        print('Finish for4')

for1()
for2()
for3()
for4()
