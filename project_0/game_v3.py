import numpy as np

def game_core_v3(number: int = 1) -> int:
    """Усовершенствованный вариант алгоритма построен на том, что по обратной связи > или < число будет не изменяться на 1,
    а будет браться середина из оставшегося диапазона угадывания. Это позволяет сократить попытки в среднем до 5

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """

    count = 0
    left_stop, right_stop = 1, 100 #Зададим вспомогательные переменные, которые будут на каждом шаге
    #ограничивать слева и справа рассматриваемый диапазон угадывания.
    #Их начальные значения соответствуют всему диапазону от 0 до 100, поэтому можно их использовать на первом шаге
    #при генерации случайного числа
    predict = np.random.randint(left_stop, right_stop+1)
    
    #На каждом шаге в зависимости от того, справа или слева от загаданного числа оказывается текущее число,
    #оно становится новым ограничением диапазона угадывания. Из этого формируется список lft_lst,
    #который по мере угадывания сокращается до искомого числа. При этом оставшийся диапазон проверяется на длину,
    #чтобы более корректно находить середину диапазона для получения значения элемента списка
    while number != predict:
        count += 1
        if number > predict:
            left_stop = predict
            lft_lst = list(range(predict, right_stop+1))
            if (right_stop-predict)%2:
                pred_index = (right_stop-predict)//2 + 1
                predict = lft_lst[pred_index]
            else:
                pred_index = (right_stop-predict)//2
                predict = lft_lst[pred_index]
        elif number < predict:
            right_stop = predict
            lft_lst = list(range(left_stop, predict))
            if (predict-left_stop)%2:
                pred_index = (predict-left_stop)//2
                predict = lft_lst[pred_index]
            else:
                pred_index = (predict-left_stop)//2 - 1
                predict = lft_lst[pred_index]

    return count

def score_game(game_core_v3) -> int:
    """За какое количество попыток в среднем за 10000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(game_core_v3(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попытки")
    
    
#Run benchmarking to score effectiveness of all algorithms
print('Run benchmarking for game_core_v2: ', end='')
score_game(game_core_v3)