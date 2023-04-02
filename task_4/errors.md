# Document, Cursor, Character.
В даній програмі є 3 класи Document, Cursor, Character
### **Document**
  * __init__ - ініціалізація класу
  * string - стрінгова репрезентація (property)
  * insert - метод для вставлення нового символу
  * delete - видаляє символ під курсором
  * save - зберігає файл
### **Cursor**
  * __init__ - ініціалізаці курсору
  * forward - рухатися вперед
  * back - рухатися назад
  * home - рухатися до початку рядка
  * end - рухатися до закінчення рядка
### **Character**
  * __init__ - ініціалізація символу
  * __str__ - стрічкова репрезентація
  * __eq__ - метод порівняння
 
### Обробляються наступні помилки:
* FileNameTypeError - Коли імя документу неправильного типу (не str).
* CharacterTypeError - Коли символ неправльного типу (не str)
* BackMovementExeption - Коли більше не можна рухатися назад.
* ForwardMovementExeption - Коли більше не можна рухатися вперед.
* CharacterCompareError - Коли порівнюються символи з не підходящими типами (підходить тільки Character і str)
Щоб протестити:
```
coverage run classes_test.py
```
