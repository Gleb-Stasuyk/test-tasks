from typing import Any, List


def first_non_repeating_letter(a: str) -> str:
    # Пройдем циклом по массиву и соберем все одинарные символы
    indices_of_non_repeating_letters = [i for i in range(len(a)) if a.lower().count(a.lower()[i]) == 1]
    # Возьмем первый, если есть, иначе пустая строка
    answer = a[indices_of_non_repeating_letters[0]] if len(indices_of_non_repeating_letters) > 0 else ''
    return answer


def make_looper(a: str) -> Any:
    string_list = list(a)

    def looper() -> Any:
        # Берем первый символ из списка возвращаем его и ставим в конец
        while True:
            letter = string_list[0]
            string_list.append(string_list.pop(0))
            return letter

    return looper


def is_merge(s: str, part1: str, part2: str) -> bool:
    # Делаем проверку на нужное количество символов
    if len(s) != len(part1 + part2):
        return False

    part1 = list(part1)
    part2 = list(part2)

    for i in range(len(s)):
        # Поочередно сверяем сиволы искомой строки с символами в партах 1 и 2 попутно удаляя подошедшие
        if len(part1) != 0 and s[i] == part1[0]:
            part1.pop(0)
        elif len(part2) != 0 and s[i] == part2[0]:
            part2.pop(0)
        else:
            # Если искомого символа в строках нет - возвращаем False
            return False

    return True


def count_change(money: int, coins: List[int]) -> int:
    """
    Создадим массив элементов от 0 до 'money' включительно, в котором индекс каждого элемента будет 
    обозначать денежную еденицу. Далее в цикле пройдемся каждой монетой по массиву и будем увеличивать текущее значенние
    элемента + значение элемента в индексе который [index] - номинал монеты. Поэтому 0 индекс должен быть изначально
    равен 1, для того, что бы первому элементу индекса номинала монеты присвоить 
    значение +=1 в проходе цикла каждой монетой.
    На примере [3, [1,2]] при первом проходе получим список [1,1,1,1], при втором проходе присвоим 2 индексу += list[0]
    затем третьему индексу += list[1] в итоге индес суммы сдачи (3) получится 2.
    """
    result = (money + 1) * [0]
    result[0] = 1

    for coin in coins:
        for i in range(len(result)):
            if i >= coin:
                temp = i - coin
                result[i] += result[temp]

    return result[money]


if __name__ == '__main__':
    print(first_non_repeating_letter('a'))  # a
    print(first_non_repeating_letter('stress'))  # t
    print(first_non_repeating_letter('moonmen'))  # e
    print(first_non_repeating_letter(''))  # (пустая строка)
    print(first_non_repeating_letter('abba'))  # (пустая строка)
    print(first_non_repeating_letter('hello world, eh?'))  # w
    print(first_non_repeating_letter('sTreSS'))  # T
    print(first_non_repeating_letter('Go hang a salami, I\'m a lasagna hog!'))  # ,
    abc = make_looper('abc')
    print(abc())  # 'a'
    print(abc())  # 'b'
    print(abc())  # 'c'
    print(abc())  # 'a'
    print(is_merge('helloworld', 'hello', 'world'))  # True
    print(is_merge('helloworld', 'how', 'ellorld'))  # True
    print(is_merge('helloworld', 'hell', 'world'))  # False
    print(is_merge('helloworld', 'ehll', 'world'))  # False
    print(is_merge('helloworld', 'worldd', 'hello'))  # False
    print(count_change(4, [1, 2]))  # 3 (1+1+1+1, 1+1+2, 2+2)
    print(count_change(10, [5, 2, 3]))  # 4 (5+5, 2+3+2+3, 5+2+3, 2+2+2+2+2)
    print(count_change(11, [5, 7]))  # 0
