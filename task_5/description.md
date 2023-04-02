#  Cipher
Таблиця, яка використовується для шифрування і розшифрування
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
B C D E F G H I J K L M N O P Q R S T U V W X Y Z A
C D E F G H I J K L M N O P Q R S T U V W X Y Z A B
D E F G H I J K L M N O P Q R S T U V W X Y Z A B C
E F G H I J K L M N O P Q R S T U V W X Y Z A B C D
F G H I J K L M N O P Q R S T U V W X Y Z A B C D E
G H I J K L M N O P Q R S T U V W X Y Z A B C D E F
H I J K L M N O P Q R S T U V W X Y Z A B C D E F G
I J K L M N O P Q R S T U V W X Y Z A B C D E F G H
J K L M N O P Q R S T U V W X Y Z A B C D E F G H I
K L M N O P Q R S T U V W X Y Z A B C D E F G H I J
L M N O P Q R S T U V W X Y Z A B C D E F G H I J K
M N O P Q R S T U V W X Y Z A B C D E F G H I J K L
N O P Q R S T U V W X Y Z A B C D E F G H I J K L M
O P Q R S T U V W X Y Z A B C D E F G H I J K L M N
P Q R S T U V W X Y Z A B C D E F G H I J K L M N O
Q R S T U V W X Y Z A B C D E F G H I J K L M N O P
R S T U V W X Y Z A B C D E F G H I J K L M N O P Q
S T U V W X Y Z A B C D E F G H I J K L M N O P Q R
T U V W X Y Z A B C D E F G H I J K L M N O P Q R S
U V W X Y Z A B C D E F G H I J K L M N O P Q R S T
V W X Y Z A B C D E F G H I J K L M N O P Q R S T U
W X Y Z A B C D E F G H I J K L M N O P Q R S T U V
X Y Z A B C D E F G H I J K L M N O P Q R S T U V W
Y Z A B C D E F G H I J K L M N O P Q R S T U V W X
Z A B C D E F G H I J K L M N O P Q R S T U V W X Y

Використання шифру Віженера передбачає якесь задане ключове слово. Це слово або набір букв має складатися лише з великих літер англійського алфавіту.

### Шифрування

#### Приклад
Щоб наочно побачити як працює цей шифр пропонуємо розглянути данний приклаж: Нехай ми маємо ключове слово - CAT і стрічку, яку будемо кодувати - **ABC**.

Перша літера закодованого повідомлення буде **С**, так як рядок який починається з A перетинається зі стовпчиком який починається з C якраз в літері **C**. За аналогією далі отримаємо B і V

### Розшифрування
Розшифрування відбувається за схожою логікою, але тепер для повернення до закодованого повідомлення ми будемо розлядаємо перетин літери коду та літери ключового слова. Закодоване повідомлення CBV перетвориться на CAT
### Переваги
* Простота використання
* Швидкість
### Недоліки
* Неможливість кодування будь-яких інших символів (зокрема пробілів), окрім великих букв англійського алфавіту.
* Можна злегкістю дізнатися ключове слово, якщо спробувати закодувати слово з букв **А**.
* Використання переважно для навчання.
