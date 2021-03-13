Работаю с таблицами ```актер - фильм - режисер```:

Создаем связь ```movies - director_id```:

```alter table movies add column director_id int;```

Добавляем связи таким образом:

```update movies set director_id = 5 where id in (2,9);```
```update movies set director_id = 1 where id = 11;```

```
 id |             title             | director_id 
----+-------------------------------+-------------
  5 | Cruella                       |            
  7 | The Notebook                  |            
  2 | Snatch                        |           5
  9 | Sherlock Holmes               |           5
 11 | The Departed                  |           1
  1 | Once Upon a Time in Hollywood |           2
  3 | Pulp Fiction                  |           2
  4 | Django Unchained              |           2
  6 | La La Land                    |           3
  8 | Blade Runner 2049             |           4
 10 | Star Wars                     |           7
(11 rows)
```

Создаем параметр gender для актеров:

```alter table actors add column gender varchar(1);```

Заполняем колонку:

```update actors set gender = 'm'  where id in (1,2,4,6,8);```
```update actors set gender = 'f'  where id in (3,5,7,9);```

```
       name        | id | gender 
-------------------+----+--------
 Brad Pitt         |  1 | m
 Leonardo DiCaprio |  2 | m
 Mark Wahlberg     |  4 | m
 Ryan Gosling      |  6 | m
 Jude Law          |  8 | m
 Emma Stone        |  3 | f
 Jennifer Aniston  |  5 | f
 Rachel McAdams    |  7 | f
 Natalie Portman   |  9 | f
```
Смотрим сколько актеров m/f находятся в нашей таблице:

```select gender, count(*) from actors group by gender;```

```
 gender | count 
--------+-------
 m      |     5
 f      |     4
(2 rows)
```
Смотрим у скольких режиссеров снимаются актеры мужского пола и сколько их:

```select director.name, count(*) from actors inner join actors_movies on (actor_id = actors.id) inner join movies on (movie_id = movies.id) inner join director on (director.id = director_id) where gender = 'm' group by director.name;```
```
       name        | count 
-------------------+-------
 Damien Chazelle   |     1
 Guy Ritchie       |     2
 Quentin Tarantino |     3
 Martin Scorsese   |     2
 Denis Villeneuve  |     1
(5 rows)
```

Теперь с женским полом:

```select director.name, count(*) from actors inner join actors_movies on (actor_id = actors.id) inner join movies on (movie_id = movies.id) inner join director on (director.id = director_id) where gender = 'm' group by director.name;```
```
      name       | count 
-----------------+-------
 Damien Chazelle |     1
 Guy Ritchie     |     1
 George Lucas    |     1
(3 rows)
```
Создаем соединительную таблицу актер - фильм:

```create table actors_movies (id serial, actor_id int, movie_id int);```

Заполняем:

```insert into actors_movies (actor_id, movie_id) values (1, 2), (1, 1), (2, 11), (2, 1), (2, 4), (3, 5), (3, 6), (6, 6), (6, 8), (6, 7), (7, 7), (8, 9), (4, 11), (9, 10), (7, 9);```
```
 id | actor_id | movie_id 
----+----------+----------
  1 |        1 |        2
  2 |        1 |        1
  3 |        2 |       11
  4 |        2 |        1
  5 |        2 |        4
  6 |        3 |        5
  7 |        3 |        6
  8 |        6 |        6
  9 |        6 |        8
 10 |        6 |        7
 11 |        7 |        7
 12 |        8 |        9
 13 |        4 |       11
 14 |        9 |       10
 15 |        7 |        9
(15 rows)
```

Соединяем актер - фильм

```select name, title from actors inner join actors_movies on (actors.id = actor_id) inner join movies on (movies.id = movie_id);```
```
       name        |             title             
-------------------+-------------------------------
 Brad Pitt         | Snatch
 Brad Pitt         | Once Upon a Time in Hollywood
 Leonardo DiCaprio | Django Unchained
 Leonardo DiCaprio | The Departed
 Leonardo DiCaprio | Once Upon a Time in Hollywood
 Emma Stone        | La La Land
 Emma Stone        | Cruella
 Mark Wahlberg     | The Departed
 Ryan Gosling      | La La Land
 Ryan Gosling      | The Notebook
 Ryan Gosling      | Blade Runner 2049
 Rachel McAdams    | Sherlock Holmes
 Rachel McAdams    | The Notebook
 Jude Law          | Sherlock Holmes
 Natalie Portman   | Star Wars
(15 rows)
```
Выбираем фильмы с участием Бреда Питта:

```select name, title from actors inner join actors_movies on (actors.id = actor_id) inner join movies on (movies.id = movie_id) where name = 'Brad Pitt';```
```
   name    |             title             
-----------+-------------------------------
 Brad Pitt | Snatch
 Brad Pitt | Once Upon a Time in Hollywood
```

Посмотрим в скольких фильмах снимался каждый актер:

```select name, count(*) from actors inner join actors_movies on (actors.id = actor_id) inner join movies on (movies.id = movie_id) group by name;```
```
       name        | count 
-------------------+-------
 Rachel McAdams    |     2
 Emma Stone        |     2
 Ryan Gosling      |     3
 Natalie Portman   |     1
 Jude Law          |     1
 Mark Wahlberg     |     1
 Leonardo DiCaprio |     3
 Brad Pitt         |     2
(8 rows)
```
Выводим отдельно Питта:

```select name, count(*) from actors inner join actors_movies on (actors.id = actor_id) inner join movies on (movies.id = movie_id) where name = 'Brad Pitt' group by name;```
```
   name    | count 
-----------+-------
 Brad Pitt |     2
```
Выводим только тех актеров, которые снимались больше, чем в одном фильме:

```select name, count(*) from actors inner join actors_movies on (actors.id = actor_id) inner join movies on (movies.id = movie_id) group by name having count(*) > 1;```
```
       name        | count 
-------------------+-------
 Rachel McAdams    |     2
 Emma Stone        |     2
 Ryan Gosling      |     3
 Leonardo DiCaprio |     3
 Brad Pitt         |     2
(5 rows)
```
Смотрим у каких режиссеров снимался Питт:

```select actors.name as actor, director.name as director from actors inner join actors_movies on (actors.id = actor_id) inner join movies on (movies.id = movie_id) inner join director on (director_id = director.id) where actors.name = 'Brad Pitt';```
```
   actor   |     director      
-----------+-------------------
 Brad Pitt | Quentin Tarantino
 Brad Pitt | Guy Ritchie
```
Делаем красивый запрос для просмотра всех таблиц:

```select actors.name as actors, title, director.name as director from actors full join actors_movies on (actors.id = actors_movies.actor_id) full join movies on (movies.id =  actors_movies.movie_id) full join director on (director.id = director_id);```
```
      actors       |             title             |     director      
-------------------+-------------------------------+-------------------
 Leonardo DiCaprio | The Departed                  | Martin Scorsese
 Mark Wahlberg     | The Departed                  | Martin Scorsese
                   | Pulp Fiction                  | Quentin Tarantino
 Leonardo DiCaprio | Once Upon a Time in Hollywood | Quentin Tarantino
 Leonardo DiCaprio | Django Unchained              | Quentin Tarantino
 Brad Pitt         | Once Upon a Time in Hollywood | Quentin Tarantino
 Ryan Gosling      | La La Land                    | Damien Chazelle
 Emma Stone        | La La Land                    | Damien Chazelle
 Ryan Gosling      | Blade Runner 2049             | Denis Villeneuve
 Rachel McAdams    | Sherlock Holmes               | Guy Ritchie
 Brad Pitt         | Snatch                        | Guy Ritchie
 Jude Law          | Sherlock Holmes               | Guy Ritchie
                   |                               | Steven Spielberg
 Natalie Portman   | Star Wars                     | George Lucas
 Jennifer Aniston  |                               | 
 Emma Stone        | Cruella                       | 
 Ryan Gosling      | The Notebook                  | 
 Rachel McAdams    | The Notebook                  | 
(18 rows)
```
Показываем фильмы без актеров:

```select actors.name, title from actors inner join actors_movies on (actor_id = actors.id) right join movies on (movie_id = movies.id);```
```
       name        |             title             
-------------------+-------------------------------
 Brad Pitt         | Once Upon a Time in Hollywood
 Leonardo DiCaprio | Once Upon a Time in Hollywood
 Brad Pitt         | Snatch
                   | Pulp Fiction
 Leonardo DiCaprio | Django Unchained
 Emma Stone        | Cruella
 Ryan Gosling      | La La Land
 Emma Stone        | La La Land
 Rachel McAdams    | The Notebook
 Ryan Gosling      | The Notebook
 Ryan Gosling      | Blade Runner 2049
 Rachel McAdams    | Sherlock Holmes
 Jude Law          | Sherlock Holmes
 Natalie Portman   | Star Wars
 Mark Wahlberg     | The Departed
 Leonardo DiCaprio | The Departed
(16 rows)
```
Показываем фильмы и режиссеров:

```select title, director.name from movies left join director on (director_id = director.id);```
```
            title              |       name        
-------------------------------+-------------------
 The Departed                  | Martin Scorsese
 Django Unchained              | Quentin Tarantino
 Once Upon a Time in Hollywood | Quentin Tarantino
 Pulp Fiction                  | Quentin Tarantino
 La La Land                    | Damien Chazelle
 Blade Runner 2049             | Denis Villeneuve
 Snatch                        | Guy Ritchie
 Sherlock Holmes               | Guy Ritchie
 Star Wars                     | George Lucas
 The Notebook                  | 
 Cruella                       | 
(11 rows)
```