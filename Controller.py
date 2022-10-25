from random import randint
from Classes import Game

list_game = []


def step_game(step, player_id):
    for i in list_game:
        if player_id == i.player_id:
            current_game = i
    if current_game.status_game and current_game.count_candies == 150:
        return 'Для начала игры введите команду "игра"'
    if step <= 28 and step > 0 and step <= current_game.count_candies:
        current_game.count_candies -= step
        text = f'Вы взяли {step} конфет.\nНа столе осталось {current_game.count_candies} конфет\n'
        current_game.status_game = True
        if current_game.count_candies == 0:
            current_game.count_candies = 150
            text += '<b>Вы победили. Поздравляю!!! =)</b>'
            return text
        if current_game.count_candies < 29:
            step_computer = current_game.count_candies
            current_game.count_candies = 150
            text += f'Игрок Computer взял {step_computer} конфет.\nОсталось 0 конфет.\n<b>Вы проиграли =(</b>'
            return text
        if current_game.count_candies % 29 != 0:
            step_computer = current_game.count_candies % 29
            current_game.count_candies -= step_computer
            text += f'Игрок Computer взял {step_computer} конфет.\nОсталось {current_game.count_candies} конфет.\nВаш ход.\n\nДля сброса игры введит слово "сброс"'
            return text
        else:
            step_computer = randint(1, 28)
            current_game.count_candies -= step_computer
            text += f'Игрок Computer взял {step_computer} конфет.\nОсталось {current_game.count_candies} конфет.\nВаш ход.\n\nДля сброса игры введит слово "сброс"'
            return text

    else:
        return 'Для начала игры введите слово "игра".\nДля того чтобы сделать ход введите количество конфет.\nДля сброса игры введите слово "сброс"'

def clear_game(player_id):
    for i in list_game:
        if player_id == i.player_id:
            current_game = i
    current_game.count_candies = 150
    current_game.status_game = True


def game_control(player_name, player_id, text):
    for i in list_game:
        if player_id == i.player_id and i.count_candies != 150:
            return 'игра начата'
        elif player_id == i.player_id and i.count_candies == 150:
            if text == 'игра':
                i.status_game = False
            return 'новая игра'
    game = Game.Game(player_name, player_id)
    list_game.append(game)
    return 'первая игра'

