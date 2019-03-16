import random
taken = 0
print('Давай сыграем в игру. \nЯ загадываю число от 1 до 100, а ты пытаешься его отгадать. \nЕсли твой ответ окажется неправильным, я постараюсь тебе помочь. \nВсего у тебя будет 8 попыток. \nПопробуем? \nЯ уже загадал.')
numb = random.randint(1,100)
while taken < 8:
    print('Итак, твоё число - это ')
    guess = input()
    guess = int(guess)

    taken = taken+1

    if guess < numb:
        print('Маловато')

    if guess > numb:
        print('Многовато')

    if guess == numb:
        break

if guess == numb:
    taken = str(taken)
    print('Поздравляю! Ты угадал число с '+taken+' попытки.')

if guess != numb:
    numb = str(numb)
    print('К сожалению, у тебя не осталось попыток. Я загадал число '+numb+'. Ты проиграл.')

input('Нажми ENTER для окончания игры')
