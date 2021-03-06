# Эти задачи необходимо решить используя регулярные выражения!

# Задача - 1
# Запросите у пользователя имя, фамилию, email. Теперь необходимо совершить проверки, имя и фамилия
# должны иметь заглавные первые буквы.
# email - не должен иметь заглавных букв и должен быть в формате: текст в нижнем регистре,
# допускается нижнее подчеркивание и цифры, потом @, потом текст, допускаются цифры, точка, ru или org или com
# Например:
# Пупкин василий - неверно указано имя, te$T@test.net - неверно указан email
# (спецсимвол, заглавная буква, .net), te_4_st@test.com - верно указан.
import re

pattern_one = '[А-Яа-я]+'
name = input('Ваше имя: ')
print(re.match(pattern_one, name))

surname = input('Ваша фамилия: ')
print(re.match(pattern_one, surname))

# на самом деле каждый может по разному создать имя почты, получается шаблонов много
# я только 3 примера напишу
pattern_two = r'[A-z]+@+[a-z]+\.+[a-z]+'
pattern3 = r'[a-zA-Z]+[0-9]\.+[A-Za-z]+@+[a-z]+\.[a-z]+'
email = input('Введите E-mail: ')
print(re.match(pattern_two, email))  # с этими шаблонами можно получить None, а на самом деле пользователь ввел email
print(re.match(pattern3, email))  # с этими шаблонами можно получить None, а на самом деле пользователь ввел email

pattern_uni = r'.+@+[a-z]+\.(ru|com|net)'
print(re.match(pattern_uni, email))  # тут шаблон получает универсальным, если только вместо(ru|com|net) поставить [a-z]
pattern_univ = r'.+@+[a-z]+\.[a-z]'
print(re.match(pattern_univ, email))

# Задача - 2:
# Вам дан текст:

some_str = '''
Мороз и солнце; день чудесный!
Еще ты дремлешь, друг прелестный —
Пора, красавица, проснись:
Открой сомкнуты негой взоры
Навстречу северной Авроры,
Звездою севера явись!
Вечор, ты помнишь, вьюга злилась,
На мутном небе мгла носилась;
Луна, как бледное пятно,
Сквозь тучи мрачные желтела,
И ты печальная сидела —
А нынче... погляди в окно:
Под голубыми небесами
Великолепными коврами,
Блестя на солнце, снег лежит;
Прозрачный лес один чернеет,
И ель сквозь иней зеленеет,
И речка подо льдом блестит.
Вся комната янтарным блеском
Озарена. Веселым треском
Трещит затопленная печь.
Приятно думать у лежанки.
Но знаешь: не велеть ли в санки
Кобылку бурую запречь?
Скользя по утреннему снегу,
Друг милый, предадимся бегу
Нетерпеливого коня
И навестим поля пустые,
Леса, недавно столь густые,
И берег, милый для меня.'''

# Необходимо с помощью регулярных выражений определить есть ли в тексте подряд
# более одной точки, при любом исходе сообщите результат пользователю!
pattern_str = r'\.{2,}'
print(re.findall(pattern_str, some_str))

