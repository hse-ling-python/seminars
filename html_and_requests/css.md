
## CSS

+ CSS сокращение от Cascading Style Sheets
+ CSS описывают, как HTML элементы должны отображаться
+ стили можно сохранять в отдельные CSS файлы или прописывать внутри HTML файлов

Простой пример оформления страницы, где заданы цвет фона, цвет и положение заголовка, шрифт и размер текста параграфа:

```
<!DOCTYPE html>
<html>
<head>
<style>
body {
  background-color: lightblue;
}

h1 {
  color: yellow;
  text-align: center;
}

p {
  font-family: verdana;
  font-size: 15px;
}
</style>
</head>
<body>

<h1>Пример</h1>
<p>Пример оформления страницы</p>

</body>
</html>
```

#### Синтаксис

Синтаксис css правил: селектор (a selector -- элемент html, для которого прописывается форматирование) и блок деклараций (a declaration block -- описание форматирования выбранного элемента). 

Например, в примере выше, `h1` -- это селектор, `{color: yellow; text-align: center;}` -- a declaration block, который отвечает за то, чтобы заголовок был жёлтого цвета и был расположен в центре. Какие ещё селекторы вы можете найти в примере выше? Какое для них постулируется форматирование?

Каждое утверждение в блоке деклараций содержит название свойства, например, `color`, и значение этого свойства, например, `yellow`. Значение свойства отделяется от названия `:`. Каждое утверждение в блоке деклараций заканчивается `;`, а сам блок оформляется `{}`.

CSS комментарии начинаются с `/*` и заканчиваются `*/`:

```
p {
  color: red;
  /* This is a single-line comment */
  text-align: center;
}

/* This is
a multi-line
comment */
```

Селектором может быть не только элемент html разметки, но и элемент разметки с определённым id; тогда перед селектором-id ставится `#`: 

```
<!DOCTYPE html>
<html>
<head>
<style>
#para1 {
  text-align: center;
  color: red;
}
</style>
</head>
<body>

<p id="para1">ID Selector Example</p>
<p>This paragraph is not affected by the style.</p>

</body>
</html>
```

Селектор может специфицировать класс элемента, тогда перед названием класса ставится `.`:

```
<!DOCTYPE html>
<html>
<head>
<style>
.center {
  text-align: center;
  color: red;
}
</style>
</head>
<body>

<h1 class="center">Red and center-aligned heading</h1>
<p class="center">Red and center-aligned paragraph.</p> 

</body>
</html>
```

Можно применить стиль только к определённым элементам класса, в примере ниже только элементы `<p>` класса `center` будут затронуты форматированием:

```
p.center {
  text-align: center;
  color: red;
}
```

Чтобы применить форматирование ко всем элементам:

```
* {
  text-align: center;
  color: blue;
}
```

Чтобы применить форматирование к нескольким элементам:

```
h1, h2, p {
  text-align: center;
  color: red;
}
```

+ **Internal css** (тэг `<style>` внутри тэга `<head>`)

+ **Inline css** (атрибут `style` внутри соответствующего тэга, в приоритете)

```
<h1 style="color:blue;text-align:center;">This is a heading</h1>
<p style="color:red;">This is a paragraph.</p>
```
+ **External css** (отдельный `.css` файл, созданный в текстовом редакторе, ссылка на него в соответствующем `html` файле):

```
<!DOCTYPE html>
<html>
<head>
<link rel="stylesheet" type="text/css" href="mystyle.css">
</head>
<body>

<h1>This is a heading</h1>
<p>This is a paragraph.</p>

</body>
</html>
```
Например, так выглядит `mystyle.css`

```
body {
  background-color: lightblue;
}

h1 {
  color: navy;
  margin-left: 20px;
}
```

#### Цвета

+ Цвет фона: `<p style="background-color:Tomato;">`
+ Цвет текста: `<h1 style="color:Tomato;">Hello World</h1>`
+ Цвет рамки: `<h1 style="border:2px solid Tomato;">Hello World</h1>`
+ Цвета можно задавать в системах RGB, HEX, HSL, RGBA, HSLA:

```
<h1 style="background-color:rgb(255, 99, 71);">...</h1>
<h1 style="background-color:#ff6347;">...</h1>
<h1 style="background-color:hsl(9, 100%, 64%);">...</h1>

<h1 style="background-color:rgba(255, 99, 71, 0.5);">...</h1>
<h1 style="background-color:hsla(9, 100%, 64%, 0.5);">...</h1>
```

#### Фон

Мы уже видели, что можно задать цвет фона, но можно и сделать фоном картинку:

```
body {
  background: url("https://upload.wikimedia.org/wikipedia/commons/8/83/Socotra_dragon_tree.JPG");
}
```

#### Размер элемента

```
<!DOCTYPE html>
<html>
<head>
<style>
div {
  height: 200px;
  width: 50%;
  background-color: powderblue;
}
</style>
</head>
<body>

<h2>Set the height and width of an element</h2>

<p>This div element has a height of 200px and a width of 50%:</p>

<div></div>

</body>
</html>
```

#### Рамки

```
p.dotted {border-style: dotted;}
p.dashed {border-style: dashed;}
p.solid {border-style: solid;}
p.double {border-style: double;}
p.groove {border-style: groove;}
p.ridge {border-style: ridge;}
p.inset {border-style: inset;}
p.outset {border-style: outset;}
p.none {border-style: none;}
p.hidden {border-style: hidden;}
p.mix {border-style: dotted dashed solid double;}
```

#### Отступы

```
div {
  border: 1px solid black;
  margin-top: 100px;
  margin-bottom: 100px;
  margin-right: 150px;
  margin-left: 80px;
  background-color: lightblue;
}
```

#### Текст

+ цвет: `color: green;`
+ ориентирование: `text-align: center;`, `text-align: right;`, `text-align: left;`
+  `text-transform: uppercase;`
   `text-transform: lowercase;`
   `text-transform: capitalize;`
   
+ отступ: `text-indent: 50px;`
+ размер шрифта: `font-size: 30px;`
+ шрифт: `font-family: "Times New Roman", Times, serif;`
  `font-family: Arial, Helvetica, sans-serif;`
+ `font-weight: bold;`

#### Списки

Для списков можно задать, например, вид значка перечисления -- `list-style-type: circle;` -- каждый элемент списка будет отмечен кружком.

```
<!DOCTYPE html>
<html>
<head>
<style>
ul.a {
  list-style-type: circle;
}

ul.b {
  list-style-type: square;
}

ol.c {
  list-style-type: upper-roman;
}

ol.d {
  list-style-type: lower-alpha;
}
</style>
</head>
<body>

<p>Example of unordered lists:</p>
<ul class="a">
  <li>Coffee</li>
  <li>Tea</li>
  <li>Coca Cola</li>
</ul>

<ul class="b">
  <li>Coffee</li>
  <li>Tea</li>
  <li>Coca Cola</li>
</ul>

<p>Example of ordered lists:</p>
<ol class="c">
  <li>Coffee</li>
  <li>Tea</li>
  <li>Coca Cola</li>
</ol>

<ol class="d">
  <li>Coffee</li>
  <li>Tea</li>
  <li>Coca Cola</li>
</ol>

</body>
</html>
```

#### Таблицы

+ характер границ:

```
table, th, td {
  border: 1px solid black;
}
```

+ ориентация элементов таблицы:

```
th {
  text-align: left;
}
```

+ цвет строк:

```
th {
  background-color: #4CAF50;
  color: white;
}
```

Чтобы легче было размещать элементы на странице, можно создать **решётку элементов** (a grid):

```
<!DOCTYPE html>
<html>
<head>
<style>
.item1 { grid-area: header; }
.item2 { grid-area: menu; }
.item3 { grid-area: main; }
.item4 { grid-area: right; }
.item5 { grid-area: footer; }

.grid-container {
  display: grid;
  grid-template-areas:
    'header header header header header header'
    'menu main main main right right'
    'menu footer footer footer footer footer';
  grid-gap: 10px;
  background-color: #2196F3;
  padding: 10px;
}

.grid-container > div {
  background-color: rgba(255, 255, 255, 0.8);
  text-align: center;
  padding: 20px 0;
  font-size: 30px;
}
</style>
</head>
<body>

<h1>Grid Layout</h1>

<p>This grid layout contains six columns and three rows:</p>

<div class="grid-container">
  <div class="item1">Header</div>
  <div class="item2">Menu</div>
  <div class="item3">Main</div>  
  <div class="item4">Right</div>
  <div class="item5">Footer</div>
</div>

</body>
</html>
```

#### Задание

Создайте красивую страничку, где будут:

+ текстовые элементы (задайте шрифт, размер, цвет, фон для них)
+ картинка (задайте размер, позицию)
+ таблица (задайте характер границ, размер ячеек, ориентацию текста в ячейках)
+ список (задайте характер маркеров элементов списка, цвет фона для списка)

+ полезный ресурс про css: https://www.w3schools.com/css/css_intro.asp
+ полезный ресурс про html: https://www.w3schools.com/html/html_intro.asp

#### Bootstrap

+ Технология, которая позволяет использовать шаблоны стилей, что ускоряет работу.
+ В открытом доступе с 2011 года.
+ https://www.w3schools.com/bootstrap/bootstrap_get_started.asp


**Пример:**

```
<!DOCTYPE html>
<html lang="en">
<head>
  <title>Bootstrap Example</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/js/bootstrap.min.js"></script>
</head>
<body>

<div class="jumbotron text-center">
  <h1>Пример</h1>
  <p>Страница создана с использованием bootstrap</p> 
</div>
  
<div class="container">
  <div class="row">
    <div class="col-sm-4">
      <h3>Первый столбец</h3>
      <p>Важный текст</p>
      <p>Ещё более важный текст</p>
    </div>
    <div class="col-sm-4">
      <h3>Второй столбец2</h3>
      <p>Важный текст</p>
      <p>Ещё более важный текст</p>
    </div>
    <div class="col-sm-4">
      <h3>Третий столбец</h3>        
      <p>Важный текст</p>
      <p>Ещё более важный текст</p>
    </div>
  </div>
</div>

</body>
</html>
```
