Построить фамильное древо по мужской линии

Создаем таблицу вида:

```select * from persons;```

```
 id | pid |        fullname        
----+-----+------------------------
  1 |   0 | Polikarp Yevstahievich
  2 |   1 | Veniamin Polikarpovich
  3 |   2 | Prokhor Veniaminovich
  4 |   3 | Prokop Prokhorovich
```
Делаем запрос вида:

```select concat('grandson ', p.fullname, ' => son ', p2.fullname, ' => father ', p3.fullname, ' => grandfather ', p4.fullname) from persons p inner join persons p2 on(p.pid = p2.id) inner join persons p3 on(p2.pid = p3.id) inner join persons p4 on(p3.pid = p4.id);```

```
concat                                                              
----------------------------------------------------------------------------------------------------------------------------------
 grandson Prokop Prokhorovich => son Prokhor Veniaminovich => father Veniamin Polikarpovich => grandfather Polikarp Yevstahievich
(1 row)
```
Объединить авторов с книгами посредством таблицы связей

```select * from authors_books;```
```
 author_id | book_id 
-----------+---------
         1 |       4
         2 |       1
         3 |       3
         4 |       2
```