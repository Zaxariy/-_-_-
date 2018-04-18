# Oглавление
print("\n\t\t\tДобро пожаловать в игру Топоры и Тузы 1.0\n\t\t\tПравила игры Топоры и Тузы\nИгра загадывает четырех значное число,Игрок должен отгадать это число за как можно меньшое количество попыток\nЦифра вашего числа называется Топором ,если в загаданном машиной числе в том же месте стоит та же цифра\nЦифра вашего числа называется Тузом ,если в загаданном числе есть таже цифра,но она стоит в другом месте\nИзначально вам дается 10 спинкоинов,минимальная ставка 1,максимальная половина вашего счета\nПри угаданном числе меньше чем за 10 попыток вам будет начисле выйграш,в противном же случаи вы потеряете часть ваших спинкоинов\n\t\t\tПриятного время провождения")
spinkoins = 10


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
    spinkoins_p = spinkoins * 0.5
    if stavka == 1:
        print(" ")
    else:
        if 1 <= stavka <= spinkoins_p:
            print(" ")
        else:
            while stavka < 1 or stavka > spinkoins_p:
                print("Ошибка\nВаша Ставка\n")
                stavka = stavka_fuc('stavka')
                if stavka == 1:
                    break

    spinkoins = spinkoins - stavka

    # подключение функции рандома
    def proverka(num):
        size=len(num)
        if size != 4 or num[0] == num[1] or num[0] == num[2] or num[0] == num[3] or num[1] == num[2] or num[1] == num[3] or num[2] == num[3]:
            while size != 4 or num[0] == num[1] or num[0] == num[2] or num[0] == num[3] or num[1] == num[2] or num[1] == num[3] or num[2] == num[3]:
                num = str(number_fuc())
                size = len(num)

        return num

    import random

    # задаем рандомное число для отгадывания

    random_num = random.randint(1000, 9999)
    # переводим рандомное число в строку для проверки

    random_str = str(random_num)
    # начало проверки
    random_str=proverka(random_str)

    # конец

    #    print(random_str)

    # начало функции по вводу пользовательского числа

    # вводим пользовательское число

    def number_fuc():
        while True:
            try:
                num = int(input('Пожалуйста введите вашe число:'))
                return num
            except ValueError:
                print("Ошибка")

    def number(number_fuc):
        # вводим пользовательское число
        num = str(number_fuc)
        num=proverka(num)
        return num

    # конец функции

    # начало функции топоры и тузы

    def Ace_Axe(num, random_str):

        # система работы топоров

        # Число schet отвечает за коректную работу цикла
        schet = 0
        axe = 0
        # Конец

        for schet in range(4):
            if random_str[schet] == num[schet]:
                axe = axe + 1
            else:
                schet = schet + 1
        if axe>1 :
            print('Вы имеете' + ' ' + str(axe) + ' ' + 'Топора')
        elif axe==0 :
            print('Вы не имеете Топоров')
        else :
            print('Вы имеете' + ' ' + str(axe) + ' ' + 'Топор')
        # cистема работы топоров отлажена

        # система работы тузов
        # числа r и g отвечаю за корректную работу цикла ,а переменная d отвечает за топоры
        schet_two = 0
        schet_tree = 0
        ace = 0
        # конец
        for schet_two in range(4):
            for schet_tree in range(4):
                if random_str[schet_two] == num[schet_tree]:
                    ace = ace + 1
                else:
                    schet_tree = schet_tree + 1

        # что б тузы не суммировались с топорами пропишем строчку d=d-c

        ace = ace - axe
        if ace>1 :
            print('Вы имеете' + ' ' + str(ace) + ' ' + 'Туза')
        elif ace==0 :
            print('Вы не имеете Тузов')
        else :
            print('Вы имеете' + ' ' + str(ace) + ' ' + 'Туз')
        # cистема работы тузов отлажена

        return axe

    # конец функии

    # функция самой игры

    def open(number, random_str):
        num = number(number_fuc)
        axe = Ace_Axe(num, random_str)
        return axe

    # конец функции
    axe = open(number, random_str)
    poputka = 1
    # условие цикличности
    if axe == 4:
        print(" ")
    else:
        while axe != 4:
            axe = open(number, random_str)
            poputka = poputka + 1
            kol_poput = 10 - poputka
            if kol_poput!=-1 :
                print("У вас осталось" + ' ' + str(kol_poput) + " попыток")
                print(" ")
            else :
                print("Игра окончена\n")

            if poputka == 11:
                break
    if axe == 4:
        print("Поздравляем,вы угадали наше число")
    else:
        print("Простите,вы проиграли")

    if poputka <= 7:
        win = stavka * 2 + stavka
    elif poputka == 8:
        win = stavka * 1 + stavka
    elif poputka == 9:
        win = stavka * 0.6 + stavka
    elif poputka == 10:
        win = stavka * 0.2 + stavka
    else:
        win = 0
    win = float(win)
    spinkoins = int(spinkoins + win)
    print("Ваш текущий счет:" + " " + str(spinkoins))

    return spinkoins


# Конец функции

spinkoins = Game(spinkoins)  # Вызов и присваивание функции для обновления счета

# Условие запуска Игры


if spinkoins>0 :
    while spinkoins>0 :
        while True:
            print("Желаете сыграть еще?:введите yes или no")
            otvet = input("Ваш ответ:")
            otvet = otvet.lower()
            otvet = otvet.rstrip()
            if otvet == 'yes' or otvet == 'no':
                break
        if otvet == 'yes':
            spinkoins= Game(spinkoins)
        elif otvet=='no' :
            exit()
else :
    print("Извините,вы больше не можете играть")
