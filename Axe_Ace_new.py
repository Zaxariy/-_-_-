#Oглавление 
print("\n\t\t\tДобро пожаловать в игру Топоры и Тузы 1.0\n\t\t\tПравила игры Топоры и Тузы\nИгра загадывает четырех значное число,Игрок должен отгадать это число за как можно меньшое количество попыток\nЦифра вашего числа называется Топором ,если в загаданном машиной числе в том же месте стоит та же цифра\nЦифра вашего числа называется Тузом ,если в загаданном числе есть таже цифра,но она стоит в другом месте\nИзначально вам дается 10 спинкоинов,минимальная ставка 1,максимальная половина вашего счета\nПри угаданном числе меньше чем за 10 попыток вам будет начисле выйграш,в противном же случаи вы потеряете часть ваших спинкоинов\n\t\t\tПриятного время провождения")
#README: в коде присуствуют такие строки как print(" ") они равносильны "\n"
spinkoins=10

def Game(spinkoins):

    print("Ваша Ставка\n")
    def stavka_fuc(stavka):
        while True:
            try:
                stavka = int(input('Пожалуйста введите вашу ставку:'))
                return stavka
            except ValueError:
                print("Ошибка")
 
    stavka = int(stavka_fuc('stavka'))
    spinkoins_p=spinkoins*0.5
    if stavka==1 :
        print(" ")
    else :	
        if 1<=stavka<=spinkoins_p :
            print (" ")
        else :
            while stavka<1 or stavka>spinkoins_p  :
                print("Ошибка\nВаша Ставка\n")
                stavka=stavka_fuc('stavka')
                if stavka==1 :
                    break

    spinkoins=spinkoins-stavka



#подключение функции рандома

    import random

#задаем рандомное число для отгадывания

    random_num=random.randint(1000,9999)
#переводим рандомное число в строку для проверки

    random_str=str(random_num)
#начало проверки

    l=len(random_str)

    if l==4 and random_str[0]!=random_str[1] and random_str[0]!=random_str[2] and random_str[0]!=random_str[3] and random_str[1]!=random_str[2] and random_str[1]!=random_str[3] and random_str[2]!=random_str[3]:
        1
    else :
        while l!=4 or random_str[0]==random_str[1] or random_str[0]==random_str[2] or random_str[0]==random_str[3] or random_str[1]==random_str[2] or random_str[1]==random_str[3] or random_str[2]==random_str[3]:
            random_str=str(random.randint(1000,9999))

                       


#конец 

#    print(random_str)

#начало функции по вводу пользовательского числа

#вводим пользовательское число

    def number_fuc():
        while True:
            try:
                num = int(input('Пожалуйста введите вашe число:'))
                return num
            except ValueError:
                print("Ошибка")

    def number(number_fuc):
#вводим пользовательское число
        num=str(number_fuc)
#ограничение для числа
#строка и переменная l=len(num) отвечает за длину пользовательского числа 
        l=len(num)
        if l==4 and num[0]!=num[1] and num[0]!=num[2] and num[0]!=num[3] and num[1]!=num[2] and num[1]!=num[3] and num[2]!=num[3] :
            print(" ")
        else :
            while l!=4 or num[0]==num[1] or num[0]==num[2] or num[0]==num[3] or num[1]==num[2] or num[1]==num[3] or num[2]==num[3]:
                #print("ошибка")
                num=str(number_fuc())
                l=len(num)

        return num                


#конец функции 


#начало функции топоры и тузы

    def Ace_Axe(num,random_str):

#система работы топоров

#Число i отвечает за коректную работу цикла,а число с отвечает за количество топоров
        i=0
        c=0
#Конец

        for i in range(4):
            if random_str[i]==num[i]:
                c=c+1
            else :
                i=i+1
	
        print ('Вы имеете'+' '+str(c)+' '+'Топора')
#cистема работы топоров отлажена
	
#система работы тузов
#числа r и g отвечаю за корректную работу цикла ,а переменная d отвечает за топоры 	
        r=0
        g=0
        d=0
#конец
        for r in range(4):
            for g in range(4):
                if random_str[r]==num[g]:
                    d=d+1
                else :
                    g=g+1

#что б тузы не суммировались с топорами пропишем строчку d=d-c

        d=d-c
        print ('Вы имеете'+' '+str(d)+' '+'Туза')
	#cистема работы тузов отлажена

        return c

#конец функии 

#функция самой игры 

    def open(number,random_str):
        num=number(number_fuc)
        c=Ace_Axe(num,random_str)
        return c
#конец функции
    c=open(number,random_str)
    poputka=1
#условие цикличности
    if c==4:
        print(" ")
    else :
        while c!=4 :
            c=open(number,random_str)
            poputka=poputka+1
            z=10-poputka
            print("У вас осталось"+' '+str(z)+" попыток")
            print(" ")
            if poputka==11 :
                break
    if c==4 :
        print("Поздравляем вы угадали наше число")
    else :
        print("Простите вы проиграли")

    if poputka<=7 :
        win=stavka*2+stavka
    elif poputka==8 :
        win=stavka*1+stavka
    elif poputka==9 :
        win=stavka*0.6+stavka
    elif poputka==10 :
        win=stavka*0.2+stavka
    else :
        win=0
    win=float(win)
    spinkoins=int(spinkoins+win) 
    print("Ваш текущий счет:"+" "+str(spinkoins))

    return spinkoins  

#Конец функции 

spinkoins=Game(spinkoins)#Вызов и присваивание функции для обновления счета

#Условие запуска Игры

if spinkoins==0 :
    print("Извините вы не можете продолжать игру")
elif spinkoins>0  :
    print("Желаете сыграть еще?:введите yes или no")
    otvet=str(input())
    if otvet!="yes" :
        print(" ")
    elif otvet=="yes":
        while otvet=="yes" :
            if spinkoins==0 :
                print("Извините вы не можете продолжать игру")
                break
            elif spinkoins>0:
                spinkoins=Game(spinkoins)
 
