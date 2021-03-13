Задача 1:

Создала таблицу вида:

```select * from users;```

```
id  | gender |  name  |     email     
----+--------+--------+---------------
  1 | m      | Vasya  | nnnn@mail.com
  2 | m      | Alex   | ttt@mail.com
  3 | m      | Alexey | mmm@gmail.com
  4 | f      | Helen  | uuu@mail.ru
  5 | f      | Jenny  | ooo@gmail.com
  6 | f      | Lora   | lll@mail.ru
(6 rows)
```

2.Получить результат вида:

```select concat('We have ',count(*), case when gender = 'm' then ' boys!' else ' girls!' end) from users group by gender;```

```
      concat      
------------------
 We have 3 boys!
 We have 3 girls!
(2 rows)
```

2.Получить результат вида:

```select concat('This is ', name, case when gender = 'm' then ', he ' else ', she ' end, 'has email ',email) from users;```

```
                  concat                   
-------------------------------------------
 This is Vasya he has email nnnn@mail.com
 This is Alex he has email ttt@mail.com
 This is Alexey he has email mmm@gmail.com
 This is Helen she has email uuu@mail.ru
 This is Jenny she has email ooo@gmail.com
 This is Lora she has email lll@mail.ru
(6 rows)
```

