
from random import choice
from uuid import uuid4

names = [
    "Алина",
    "Алиса",
    "Анастасия",
    "Анна",
    "Арина",
    "Валерия",
    "Варвара",
    "Вероника",
    "Виктория",
    "Дарья",
    "Диана",
    "Екатерина",
    "Елена",
    "Елизавета",
    "Ирина",
    "Кристина",
    "Ксения",
    "Маргарита",
    "Марина",
    "Мария",
    "Милана",
    "Наталья",
    "Ольга",
    "Полина",
    "Светлана",
    "Татьяна",
    "Юлия",
    "Александр",
    "Алексей",
    "Андрей",
    "Артем",
    "Арсений",
    "Владислав",
    "Денис",
    "Дмитрий",
    "Евгений",
    "Егор",
    "Иван",
    "Игорь",
    "Илья",
    "Кирилл",
    "Максим",
    "Матвей",
    "Михаил",
    "Никита",
    "Роман",
    "Руслан",
    "Сергей",
    "Тимофей",
    "Тимур",
    "Ярослав",
]

letters = [chr(i)+'.' for i in range(ord("А"), ord("Я")+1)]

def generate_pupils(number):
    """ создание виртуальных учеников"""
    return [{"pupil_name": choice(names) + ' ' + choice(letters)} for _ in range(number)]

def generate_codes(number):
    """ гененирование уникальных кодов"""
    return [str(uuid4()) for i in range(number)]