# SQL VS SQLAlchemy Шпаргалка

(Нуждается в проверке, но большая часть работает)

## Основные операции

### SELECT запросы

| SQL | SQLAlchemy ORM | Комментарий |
|-----|----------------|-------------|
| **Базовый SELECT** |
| `SELECT * FROM users` | `session.query(User).all()` | Получить все записи |
| `SELECT name, email FROM users` | `session.query(User.name, User.email).all()` | Выбор конкретных колонок |
| `SELECT DISTINCT department FROM employees` | `session.query(Employee.department).distinct().all()` | Уникальные значения |
| `SELECT * FROM users LIMIT 10` | `session.query(User).limit(10).all()` | Ограничение количества |
| `SELECT * FROM users LIMIT 10 OFFSET 20` | `session.query(User).limit(10).offset(20).all()` | Пагинация |

### WHERE / FILTER условия

| SQL | SQLAlchemy ORM | Комментарий |
|-----|----------------|-------------|
| **Простые условия** |
| `SELECT * FROM users WHERE age > 18` | `session.query(User).filter(User.age > 18).all()` | Больше чем |
| `SELECT * FROM users WHERE age >= 18` | `session.query(User).filter(User.age >= 18).all()` | Больше или равно |
| `SELECT * FROM users WHERE age = 25` | `session.query(User).filter(User.age == 25).all()` | Равно (два знака =) |
| `SELECT * FROM users WHERE age != 25` | `session.query(User).filter(User.age != 25).all()` | Не равно |
| `SELECT * FROM users WHERE name = 'John'` | `session.query(User).filter(User.name == 'John').all()` | Строковое равенство |
| **Сложные условия** |
| `SELECT * FROM users WHERE age > 18 AND status = 'active'` | `session.query(User).filter(User.age > 18, User.status == 'active').all()` | Несколько filter() |
| | `session.query(User).filter(and_(User.age > 18, User.status == 'active')).all()` | Явный and_() |
| `SELECT * FROM users WHERE age > 18 OR status = 'active'` | `session.query(User).filter(or_(User.age > 18, User.status == 'active')).all()` | Или условие |
| `SELECT * FROM users WHERE NOT (age > 18)` | `session.query(User).filter(not_(User.age > 18)).all()` | Отрицание |
| **Специальные операторы** |
| `SELECT * FROM users WHERE name LIKE 'J%'` | `session.query(User).filter(User.name.like('J%')).all()` | LIKE с % |
| `SELECT * FROM users WHERE name LIKE '%ohn%'` | `session.query(User).filter(User.name.like('%ohn%')).all()` | LIKE с % вокруг |
| `SELECT * FROM users WHERE name NOT LIKE 'J%'` | `session.query(User).filter(User.name.notlike('J%')).all()` | NOT LIKE |
| `SELECT * FROM users WHERE email LIKE '%@gmail.com'` | `session.query(User).filter(User.email.like('%@gmail.com')).all()` | LIKE в конце |
| `SELECT * FROM users WHERE name IN ('John', 'Jane', 'Bob')` | `session.query(User).filter(User.name.in_(['John', 'Jane', 'Bob'])).all()` | IN список |
| `SELECT * FROM users WHERE age BETWEEN 20 AND 30` | `session.query(User).filter(User.age.between(20, 30)).all()` | BETWEEN |
| `SELECT * FROM users WHERE age NOT BETWEEN 20 AND 30` | `session.query(User).filter(User.age.notbetween(20, 30)).all()` | NOT BETWEEN |
| **NULL проверки** |
| `SELECT * FROM users WHERE email IS NULL` | `session.query(User).filter(User.email.is_(None)).all()` | IS NULL |
| `SELECT * FROM users WHERE email IS NOT NULL` | `session.query(User).filter(User.email.isnot(None)).all()` | IS NOT NULL |
| **Подзапросы в WHERE** |
| `SELECT * FROM users WHERE id IN (SELECT user_id FROM orders)` | `subq = session.query(Order.user_id)`<br>`session.query(User).filter(User.id.in_(subq)).all()` | IN с подзапросом |

### JOIN операции

| SQL | SQLAlchemy ORM | Комментарий |
|-----|----------------|-------------|
| **INNER JOIN** |
| `SELECT * FROM users JOIN orders ON users.id = orders.user_id` | `session.query(User, Order).join(Order).all()` | Автоматический JOIN по FK |
| | `session.query(User, Order).join(Order, User.id == Order.user_id).all()` | Явное условие JOIN |
| `SELECT users.name, orders.total FROM users JOIN orders ON users.id = orders.user_id` | `session.query(User.name, Order.total).join(Order).all()` | Выбор колонок после JOIN |
| **LEFT/RIGHT JOIN** |
| `SELECT * FROM users LEFT JOIN orders ON users.id = orders.user_id` | `session.query(User, Order).outerjoin(Order).all()` | LEFT OUTER JOIN |
| `SELECT * FROM orders RIGHT JOIN users ON users.id = orders.user_id` | `session.query(Order, User).outerjoin(User).all()` | RIGHT OUTER JOIN |
| **Множественные JOIN** |
| `SELECT * FROM users JOIN orders ON users.id = orders.user_id JOIN products ON orders.product_id = products.id` | `session.query(User, Order, Product)`<br>`.join(Order)`<br>`.join(Product)`<br>`.all()` | Цепочка JOIN |
| **SELF JOIN** |
| `SELECT e1.name, e2.name as manager FROM employees e1 LEFT JOIN employees e2 ON e1.manager_id = e2.id` | `session.query(Employee.name, Employee.manager_name)`<br>`.join(Employee, Employee.manager_id == Employee.id, isouter=True)`<br>`.all()` | Self join с алиасами |

### GROUP BY и агрегатные функции

| SQL | SQLAlchemy ORM | Комментарий |
|-----|----------------|-------------|
| **Агрегатные функции** |
| `SELECT COUNT(*) FROM users` | `session.query(func.count()).select_from(User).scalar()` | Общее количество |
| `SELECT COUNT(id) FROM users` | `session.query(func.count(User.id)).scalar()` | COUNT по колонке |
| `SELECT AVG(age) FROM users` | `session.query(func.avg(User.age)).scalar()` | Среднее значение |
| `SELECT SUM(salary) FROM employees` | `session.query(func.sum(Employee.salary)).scalar()` | Сумма |
| `SELECT MIN(age), MAX(age) FROM users` | `session.query(func.min(User.age), func.max(User.age)).first()` | MIN и MAX вместе |
| **GROUP BY** |
| `SELECT department, COUNT(*) FROM employees GROUP BY department` | `session.query(Employee.department, func.count())`<br>`.group_by(Employee.department)`<br>`.all()` | Группировка с COUNT |
| `SELECT department, AVG(salary) FROM employees GROUP BY department` | `session.query(Employee.department, func.avg(Employee.salary))`<br>`.group_by(Employee.department)`<br>`.all()` | Группировка с AVG |
| `SELECT status, COUNT(*), AVG(age) FROM users GROUP BY status` | `session.query(User.status, func.count(), func.avg(User.age))`<br>`.group_by(User.status)`<br>`.all()` | Несколько агрегатов |
| **HAVING** |
| `SELECT department, COUNT(*) FROM employees GROUP BY department HAVING COUNT(*) > 5` | `session.query(Employee.department, func.count())`<br>`.group_by(Employee.department)`<br>`.having(func.count() > 5)`<br>`.all()` | HAVING условие |
| `SELECT department, AVG(salary) FROM employees GROUP BY department HAVING AVG(salary) > 50000` | `session.query(Employee.department, func.avg(Employee.salary))`<br>`.group_by(Employee.department)`<br>`.having(func.avg(Employee.salary) > 50000)`<br>`.all()` | HAVING с AVG |

### ORDER BY и сортировка

| SQL | SQLAlchemy ORM | Комментарий |
|-----|----------------|-------------|
| **Простая сортировка** |
| `SELECT * FROM users ORDER BY name` | `session.query(User).order_by(User.name).all()` | Сортировка ASC |
| `SELECT * FROM users ORDER BY name ASC` | `session.query(User).order_by(User.name.asc()).all()` | Явный ASC |
| `SELECT * FROM users ORDER BY name DESC` | `session.query(User).order_by(User.name.desc()).all()` | Сортировка DESC |
| `SELECT * FROM users ORDER BY age DESC, name ASC` | `session.query(User).order_by(User.age.desc(), User.name.asc()).all()` | Множественная сортировка |
| **Сортировка с вычислениями** |
| `SELECT * FROM users ORDER BY LENGTH(name) DESC` | `session.query(User).order_by(func.length(User.name).desc()).all()` | Сортировка по функции |
| `SELECT *, (score * 10) as weighted FROM users ORDER BY weighted DESC` | `session.query(User, (User.score * 10).label('weighted'))`<br>`.order_by('weighted DESC')`<br>`.all()` | Сортировка по вычислению |

## Модификация данных

### INSERT операции

| SQL | SQLAlchemy ORM | Комментарий |
|-----|----------------|-------------|
| **Простой INSERT** |
| `INSERT INTO users (name, email) VALUES ('John', 'john@example.com')` | `user = User(name='John', email='john@example.com')`<br>`session.add(user)`<br>`session.commit()` | Добавить один объект |
| **Множественный INSERT** |
| `INSERT INTO users (name, email) VALUES ('John', 'john@ex.com'), ('Jane', 'jane@ex.com')` | `session.add_all([`<br>`User(name='John', email='john@ex.com'),`<br>`User(name='Jane', email='jane@ex.com')`<br>`])`<br>`session.commit()` | Добавить несколько объектов |
| **INSERT с возвратом ID** |
| `INSERT INTO users (name) VALUES ('John') RETURNING id` | `user = User(name='John')`<br>`session.add(user)`<br>`session.flush()`<br>`print(user.id)` | Получить сгенерированный ID |

### UPDATE операции

| SQL | SQLAlchemy ORM | Комментарий |
|-----|----------------|-------------|
| **UPDATE по условию** |
| `UPDATE users SET status = 'inactive' WHERE last_login < '2023-01-01'` | `session.query(User)`<br>`.filter(User.last_login < '2023-01-01')`<br>`.update({'status': 'inactive'})`<br>`session.commit()` | Массовый UPDATE |
| `UPDATE users SET login_count = login_count + 1 WHERE id = 1` | `session.query(User)`<br>`.filter(User.id == 1)`<br>`.update({User.login_count: User.login_count + 1})`<br>`session.commit()` | UPDATE с вычислением |
| **UPDATE через объект** |
| `UPDATE users SET email = 'new@ex.com' WHERE id = 1` | `user = session.query(User).get(1)`<br>`user.email = 'new@ex.com'`<br>`session.commit()` | Изменить и закоммитить |

### DELETE операции

| SQL | SQLAlchemy ORM | Комментарий |
|-----|----------------|-------------|
| **DELETE по условию** |
| `DELETE FROM users WHERE status = 'inactive'` | `session.query(User)`<br>`.filter(User.status == 'inactive')`<br>`.delete()`<br>`session.commit()` | Массовый DELETE |
| `DELETE FROM users WHERE id = 1` | `session.query(User).filter(User.id == 1).delete()`<br>`session.commit()` | Удалить по ID |
| **DELETE через объект** |
| `DELETE FROM users WHERE id = 1` | `user = session.query(User).get(1)`<br>`session.delete(user)`<br>`session.commit()` | Удалить объект |

## Продвинутые операции

### Подзапросы

| SQL | SQLAlchemy ORM | Комментарий |
|-----|----------------|-------------|
| **Подзапрос в SELECT** |
| `SELECT u.name, (SELECT COUNT(*) FROM orders o WHERE o.user_id = u.id) as order_count FROM users u` | `subq = session.query(func.count(Order.id))`<br>`.filter(Order.user_id == User.id)`<br>`.label('order_count')`<br>`session.query(User.name, subq).all()` | Скалярный подзапрос |
| **Подзапрос в FROM** |
| `SELECT * FROM (SELECT department, AVG(salary) as avg_sal FROM employees GROUP BY department) WHERE avg_sal > 50000` | `subq = session.query(Employee.department, func.avg(Employee.salary).label('avg_sal'))`<br>`.group_by(Employee.department)`<br>`.subquery()`<br>`session.query(subq.c.department, subq.c.avg_sal)`<br>`.filter(subq.c.avg_sal > 50000)`<br>`.all()` | Подзапрос как таблица |
| **EXISTS** |
| `SELECT * FROM users u WHERE EXISTS (SELECT 1 FROM orders o WHERE o.user_id = u.id)` | `subq = session.query(Order).filter(Order.user_id == User.id).exists()`<br>`session.query(User).filter(subq).all()` | EXISTS условие |
| **NOT EXISTS** |
| `SELECT * FROM users u WHERE NOT EXISTS (SELECT 1 FROM orders o WHERE o.user_id = u.id)` | `subq = session.query(Order).filter(Order.user_id == User.id).exists()`<br>`session.query(User).filter(not_(subq)).all()` | NOT EXISTS |

### UNION и UNION ALL

| SQL | SQLAlchemy ORM | Комментарий |
|-----|----------------|-------------|
| **UNION** |
| `SELECT name FROM users UNION SELECT name FROM customers` | `q1 = session.query(User.name)`<br>`q2 = session.query(Customer.name)`<br>`session.query(q1.union(q2)).all()` | UNION (уникальные) |
| **UNION ALL** |
| `SELECT name FROM users UNION ALL SELECT name FROM customers` | `q1 = session.query(User.name)`<br>`q2 = session.query(Customer.name)`<br>`session.query(q1.union_all(q2)).all()` | UNION ALL (все строки) |

### CASE выражения

| SQL | SQLAlchemy ORM | Комментарий |
|-----|----------------|-------------|
| **Простой CASE** |
| `SELECT name, CASE WHEN age < 18 THEN 'minor' ELSE 'adult' END as age_group FROM users` | `age_group = case(`<br>`(User.age < 18, 'minor'),`<br>`else_='adult'`<br>`)`<br>`session.query(User.name, age_group.label('age_group')).all()` | CASE WHEN |
| **CASE с несколькими условиями** |
| `SELECT name, CASE WHEN score >= 90 THEN 'A' WHEN score >= 80 THEN 'B' ELSE 'C' END as grade FROM students` | `grade = case(`<br>`(Student.score >= 90, 'A'),`<br>`(Student.score >= 80, 'B'),`<br>`else_='C'`<br>`)`<br>`session.query(Student.name, grade.label('grade')).all()` | Множественные условия |

### Функции даты и времени

| SQL | SQLAlchemy ORM | Комментарий |
|-----|----------------|-------------|
| **Текущая дата/время** |
| `SELECT NOW()` | `session.query(func.now()).scalar()` | Текущее время сервера |
| `SELECT CURRENT_DATE` | `session.query(func.current_date()).scalar()` | Текущая дата |
| **Экстракция частей даты** |
| `SELECT EXTRACT(YEAR FROM created_at) FROM users` | `session.query(func.extract('year', User.created_at)).all()` | Год из даты |
| `SELECT EXTRACT(MONTH FROM created_at) FROM users` | `session.query(func.extract('month', User.created_at)).all()` | Месяц из даты |
| **Разница дат** |
| `SELECT DATE_PART('day', NOW() - created_at) FROM users` | `session.query(func.date_part('day', func.now() - User.created_at)).all()` | Разница в днях |

## Частые ошибки и решения

### Ошибка: "Ambiguous join"

**Проблема:**
```python
# ОШИБКА: SQLAlchemy не знает, как джойнить
session.query(Film).join(Rating).filter(...)
```

**Решение:**
```python
# Указать условие JOIN явно
session.query(Film).join(Rating, Film.title_id == Rating.title_id).filter(...)

# Или использовать relationship (надо прописать в модели базы)
session.query(Film).join(Film.rating).filter(...)
```

### Ошибка: "Textual SQL should be explicitly declared"

**Проблема:**
```python
# ОШИБКА в SQLAlchemy 2.0+
session.execute("SELECT * FROM users")
```

**Решение:**
```python
from sqlalchemy import text
session.execute(text("SELECT * FROM users"))
```

### Ошибка: "Comparison with None"

**Проблема:**
```python
# ОШИБКА: Не работает с NULL
session.query(User).filter(User.email == None)
```

**Решение:**
```python
# Использовать .is_() для NULL
session.query(User).filter(User.email.is_(None))
```

## Примеры

```python
# Базовый SELECT с фильтрацией
users = session.query(User)\
    .filter(User.age > 18)\
    .filter(User.status == 'active')\
    .order_by(User.name)\
    .limit(10)\
    .all()

# JOIN с агрегацией
result = session.query(
    User.name,
    func.count(Order.id).label('order_count'),
    func.sum(Order.total).label('total_spent')
).join(Order)\
 .filter(Order.created_at >= '2023-01-01')\
 .group_by(User.id)\
 .having(func.count(Order.id) > 5)\
 .order_by(func.sum(Order.total).desc())\
 .all()

# Подзапрос
subq = session.query(
    Order.user_id,
    func.count(Order.id).label('order_count')
).group_by(Order.user_id).subquery()

result = session.query(
    User,
    subq.c.order_count
).outerjoin(subq, User.id == subq.c.user_id)\
 .filter(subq.c.order_count > 10)\
 .all()
```
