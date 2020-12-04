for i in range(1,101):
    oszthato3 = ( i % 3 == 0 )
    oszthato5 = ( i % 5 == 0 )
    if   oszthato3 and not oszthato5:
        print('fizz')
    elif oszthato5 and not oszthato3:
        print('buzz')
    elif oszthato3 and oszthato5:
        print('fizzbuzz')
    else:
        print(i)
    




