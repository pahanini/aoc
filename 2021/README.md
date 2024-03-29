# Решения [adventofcode.com 2021](https://adventofcode.com/2021/)

   **Помимо своих, привожу примеры наиболее интересных решений в reddit**

1. Простая задача на пробежаться по списку. Сделал простым суммированием, в лоб. 
   Во второй части есть более элегантное решение, когда не надо каждый раз вычислять
   сумму, достаточно сравнить новое число которое добавляется к окну с 
   тем что уходит из окна.
2. Задача на координаты, наверное есть миллионы способов решить в 1 строку, 
   просто складывал координаты.
3. Немного запутанная задача на получение данных из двухмерного массива. 
   Основная сложность это разобраться в условиях и не запутаться в расчетах.
4. Игра в бинго с кальмаром. Достаточно простой алгоритм, ждал что во второй части 
   перейдем к трехмерным доскам и поэтому в решении держал это в уме. Задача учит нас 
   тому, что преждевременная оптимизация это зло :-)
5. Очень простая задача. Нужно правильно рассчитать координаты, и заполнить словарь.
6. Супер-задача про анчоусов! Решение в лоб это поместить исходные данные в список, далее в цикле по количеству дней изменять 
   состояния и добавлять восьмерки в конец, но на большом количестве данных это работает медленно. Варианты прикрутить 
   кэширование или изменить подход к расчету. Второй вариант гораздо интереснее. Можно посчитать
   сколько анчоусов находиться на каком "сроке" и поместить эти данные в список из 9 элементов 
   (максимальное количество состояний). Потом ротировать список добавляя рыбок при необходимости.
   
   UPD: Найдено (не мной), похожее, но еще более простое решение 
   ```   
   for i in range(256):
       count[(i + 7) % 9] += count[i % 9]  
   ```
7. Задача чем то похожая на предыдущую. Также при простом переборе съест кучу времени. Немного нужно 
   подумать над формулой вычисления потребления топлива во второй части.
 
   UPD: Конечно же оказалось, что есть красивое математическое решение при помощи 
   медианы и среднего. 
   
   ```
   median = int(statistics.median(data))
   mean = int(statistics.mean(data))
   
   part1 = sum([crab_fuel(x, mean) for x in data])
   part1 = sum([crab_fuel(x, mean+1) for x in data])
   ```
   
8. Первая часть задания состоит в том, что нужно понять задание. Основная соль во 
   второй части. Вторая часть решается в уме или на бумажке. Хороший вариант для 
   задачки на собеседовании.
   
9. Простое сравнение координат с соседними в первой части и немного рекурсии во второй. 
   
   UPD: Если знать о существовании ```networkx.nx.grid_2d_graph``` и
   ```nx.connected_components``` то решение может быть куда проще)
   
10. Сначала она появилась на всех курсах по алгоритмам, 
    потом на всех собеседованиях и вот наконец она попала на adventofcode - 
    задача про скобочки!
    
11. Задачка чем то напомнившая игру "жизнь".
    
12. Как мне показалось, достаточно сложная задача на поиск всех возможных путей в графе. 
    Самая соль во второй части, я так и не нашел как решить ее при помощи какой-либо 
    стандартной библиотеки типа ```networkx```
    
13. Простенькая задачка про "оригами". Во второй части конечно можно вывести результат
    на экран и прочитать глазами. Но только ```tesseract```, только хардкор!
    
14. Опять задача на оптимизацию алгоритма, первая часть решается элементарно через 
    строки. Однако подход в лоб во второй части не работает, придется поискать более 
    оптимальный алгоритм, чем то напоминает задачу про анчоусов.

15. Вот и пошли сложные задачи, сделал через граф. Нужно поискать решение DP.

16. Суть задачи понять задание и разобраться в нем, самая пока неинтересная задача. 

17. Кидаем дрона в мишень. Ничего не придумал кроме брутфорса.

18. Решение в лоб использовать деревья, но есть сложность определения соседнего левого или 
    правого листа.  Для решения нужно как-то скрестить коня с ужом (дерево со списком).
    



