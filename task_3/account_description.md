## Notebook

auth - Логіка авторизації.
notebook - реалізація записника.
auth_account - інтерфейс користувача

Ідея програми: створити записник з авторизацією та ролями.
1) В програмі можна робити наступні дії будучи не зареєстрованим:
  * create account - cтворити акаунт
  * login - залогінитись
  * logout - вийти з акаунту
  * exit - завершити виконання пронрами.
В програмі передбачено дві ролі Користувач та Адмін.
2) Користувач може:
  * create note - створювати свої записи
  * notes - переглядати свої записи
3) Адмін може:
  * create note - створювати свої записи
  * notes - переглядати свої записи
  * all notes - переглядати записи всіх користувачів
  * give permission - надавати права адмінства іншим користувачам
З самого початку програми створюється користувач з адмінськими правами
login - joe,
password - joepassword,
![image](https://user-images.githubusercontent.com/69431189/229369052-6b9f1361-3270-42dc-9f49-27f94654f252.png)

Під час виконання програми оброблюю такі помилки UsernameAlreadyExists, PasswordTooShort, InvalidUsername, InvalidPassword, PermissionError, NotPermittedError.
На екран виводиться, відповідне до кожної помилки, повідомлення.
Наприклад: ![image](https://user-images.githubusercontent.com/69431189/229369116-df973167-5c0f-485a-b987-0be7f667f106.png)
