# Порівняння алгоритмів сортування

У цьому дослідженні ми порівняли три алгоритми сортування: сортування вставками, сортування злиттям та Timsort.

## Сортування вставками (Insertion Sort)

- Часова складність: O(n^2)
- Стабільність: гарантована
- Опис: перебирає елементи масиву один за одним і вставляє їх на відповідні позиції в відсортовану частину масиву
- Ефективний для невеликих масивів або вже відсортованих даних

## Сортування злиттям (Merge Sort)

- Часова складність: O(n log n)
- Стабільність: гарантована
- Опис: базується на розділенні масиву на менші частини, сортуванні їх окремо, а потім об'єднанні відсортованих підмасивів
- Ефективний для великих масивів

## Timsort

- Часова складність: O(n log n).
- Стабільність: гарантована.
- Гібридний алгоритм, поєднує сортування злиттям і сортування вставками.
- Використовується в Python (вбудовані функція sorted() та метод sort()), оскільки добре справляється з різними типами даних та різними розмірами масивів.

# Результати порівняльного аналізу алгоритмів за часом виконання шляхом їх тестування на різних наборах даних:

### Mасив випадкових цілих чисел розміром n = 10**3:

- Insertion Sort time: 0.011932 seconds
- Merge Sort time: 0.001046 seconds
- Timsort time: 0.000067 seconds

### Збільшений масив більше ніж на порядок n = 10**4:

- Insertion Sort time: 1.286191 seconds
- Merge Sort time: 0.014168 seconds
- Timsort time: 0.000894 seconds

### Великий масив випадкових цілих чисел розміром n = 10**5

- Insertion Sort time: 154.194906 seconds
- Merge Sort time: 0.179078 seconds
- Timsort time: 0.012862 seconds

## Висновки:

Згідно з результатами досліджень, коли ми маємо великий масив даних, Timsort є найефективнішим варіантом. Він поєднує переваги обох підходів (сортування злиттям та сортування вставками) і добре працює на різних наборах даних.
Сортування злиттям також є ефективним, але, хоча Timsort та злиття мають однакову часову складність, Timsort все одно на порядок ефективніше.
Сортування вставками виявилось найповільнішим.

Якщо подивитись на 3 експерименти, то для Timsort та злиттям витрачений час при більшені масиву на порядок зростає теж приблизно на порядок (трохи більше ніж на порядок, що нагадує логарифмічний зсув), а от для вставки при збільшенні масиву кожного разу порядки, час збільшується на 2 порядки. Такі результати повністю підтверджують зазначені часові складності для кожного методу
