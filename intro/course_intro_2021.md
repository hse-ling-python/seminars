# Intro

## Устройство курса


### Количество пар

Первый модуль - 7 (пока 6, возможно, что седьмая пара переедет на второй модуль); второй модуль - 12; третий модуль - 14

Страница курса: https://hse-ling-python.github.io/

### Оценка

0.7 домашние задания + 0.3 проект

На сегодняшний день план такой:

**1 модуль**: три домашних задания - по морфологии, пандас и визуализации, по векторным моделям

В первом модуле поговорим о типах данных, морфологии, визуализации и поработаем с векторными семантическими моделями

**2 модуль**: три домашних задания - бд, краулер, сайт

Второй модуль посвящен вебу: базы данных, html + css, скачивание данных из интернета, создание своего веб-приложения

**3 модуль**: три домашних задания -- хакатон, машинное обучение, бот -- и итоговый проект на 3 балла от итоговой оценки

В третьем модуле поговорим о машинном обучении, тг ботах и о других интересных темах

## В чём писать код?

Основным инструментом для работы будет PyCharm и Jupyter notebooks 

**PyCharm**

PyCharm удобен для написания скриптов, работы с большими проектами, где сложная система файлов разных типов. Кроме этого, удобно работать с системами контроля версий, например с **git**, который используется на GitHub и GitLab.

Есть бесплатная версия (Community), а для студентов и преподавателей бесплатна и версия Professional, в которой есть определенные бонусы. Для этого по корпоративной почте можно получить лицензию, скачать версию Professional и активировать в специальной форме. 

1. [Зарегистрироваться на сайте и получить студенческую лицензию](https://www.jetbrains.com/shop/eform/students)
2. [Скачать версию для своей ОС](https://www.jetbrains.com/pycharm/download/)
3. Установить (есть инструкции на сайте)
4. Запустить и активировать лицензию (Help -> Register)

**тетрадки Jupyter**

Тетрадки Jupyter (например, вот этот конспект) позволяют работать с визуализацией (вставлять графики, картинки), а также выполнять код не один раз, как скрипт, а отдельными кусочками. Это часто используется в машинном обучении, когда не нужно писать огромные функций, а просто запустить обучение модели и вывести графики. Правила хорошего тона говорят, что писать огромные функции в тетрадках - это плохо, поэтому для них лучше использовать обычные .py файлы


Можно установить через pip
```shell
pip install jupyter
```

## Если что-то идет не так

Если в командной строке пишет, что нет pip, попробуйте посмотреть версию питона:

```shell
python --version
```

или

```shell
python3 --version
```

Если будет писать, что питон не найден или не является известной программой, то, скорее всего, у вас Windows и проще всего зайти на python.org и переустановить питон, не забыв отметить "add to PATH". Если и это не помогает, обратитесь к преподавателю или напишите в чат.

## Еще о правилах хорошего тона

Красивый код - это не только эстетическое удовольствие, но и жизненная необходимость, потому что такой код проще понимать, а так легче работать в команде, искать свои ошибки и вспоминать, что ты написал год назад.

Для Python есть отдельная конвенция о том, как надо писать код - **PEP-8**. В PyCharm есть встроенная функция проверки и справа от кода есть полоса, где можно найти советы и исправления. Плюс к этому есть подчеркивания, при наведении на которые вы тоже можете найти полезные советы. Соответствие PEP-8 будет одним из требований этого курса. Для jupyter есть расширения для проверки PEP


```python
# вот так можно запускать команды для консоли прямо внутри тетрадки
! pip3 install pycodestyle flake8 pycodestyle_magic
```

импортируем и активируем модуль проверки


```python
%load_ext pycodestyle_magic
%pycodestyle_on
```


```python
name = 'this is very very very very very very very very very very very very very very very very very long line'
```

    1:80: E501 line too long (111 > 79 characters)



```python
t=5+3
```

    1:2: E225 missing whitespace around operator



```python
t = 5 + 3
```

Просмотрите конвенции https://www.python.org/dev/peps/pep-0008/

Назовите несколько, которые Вы считаете наиболее полезными.

## Полезное про Jupyter

**Немного магии**

Magic commands -- функции, позволяющие решать некоторые стандартные проблемы


```python
%lsmagic
```




    Available line magics:
    %alias  %alias_magic  %autocall  %automagic  %autosave  %bookmark  %cd  %clear  %cls  %colors  %config  %connect_info  %copy  %ddir  %debug  %dhist  %dirs  %doctest_mode  %echo  %ed  %edit  %env  %gui  %hist  %history  %killbgscripts  %ldir  %less  %load  %load_ext  %loadpy  %logoff  %logon  %logstart  %logstate  %logstop  %ls  %lsmagic  %macro  %magic  %matplotlib  %mkdir  %more  %notebook  %page  %pastebin  %pdb  %pdef  %pdoc  %pfile  %pinfo  %pinfo2  %popd  %pprint  %precision  %profile  %prun  %psearch  %psource  %pushd  %pwd  %pycat  %pylab  %qtconsole  %quickref  %recall  %rehashx  %reload_ext  %ren  %rep  %rerun  %reset  %reset_selective  %rmdir  %run  %save  %sc  %set_env  %store  %sx  %system  %tb  %time  %timeit  %unalias  %unload_ext  %who  %who_ls  %whos  %xdel  %xmode
    
    Available cell magics:
    %%!  %%HTML  %%SVG  %%bash  %%capture  %%cmd  %%debug  %%file  %%html  %%javascript  %%js  %%latex  %%markdown  %%perl  %%prun  %%pypy  %%python  %%python2  %%python3  %%ruby  %%script  %%sh  %%svg  %%sx  %%system  %%time  %%timeit  %%writefile
    
    Automagic is ON, % prefix IS NOT needed for line magics.



line magics -- один ```%``` впереди и относятся к одной строке,

cell magics -- два ```%%``` впереди и относятся к ячейке.


```latex
%%latex
\begin{align}
a = \frac{1}{2} && b = \frac{6}{7}
\end{align}
```


\begin{align}
a = \frac{1}{2} && b = \frac{6}{7}
\end{align}


**Автоматическое комментирование** -- ```Ctrl/Cmd + /``` -- закомментирует выделенный участок кода; чтобы убрать комментарий, нажмите повторно. 

**Удалили код или ячейку с кодом случайно?**

+ Чтобы вернуть удалённый внутри ячейки код, нажмите ```CTRL/CMD+Z```

+ Чтобы вернуть удалённую ячейку, нажмите ```ESC+Z``` или ```EDIT > Undo Delete Cells```

## Markdown
 
Markdown -- это упрощенный язык разметки, который преобразует (почти) обычный текст в html-страницу. Создан в 2004 году Джоном Грубером и Аароном Шварцем, затем был дополнен и адаптирован для различных приложений. Markdown-файлы имеют расширение .md или .markdown. Markdown используется на github, telegram и, что особенно важно для нас сейчас, в jupyter тетрадках для форматирования текстовых окон.

Несколько примеров форматирования:

1.Заголовки в Markdown выделяются решетками #:

# заголовок 1 уровня
## заголовок 2 уровня
...
###### заголовок 6 уровня

2. Чтобы выделить текст курсивом, нужно поставить в начале и в конце фрагмента текста * или _ (не отделяя пробелом):

*звезды* или _нижние подчеркивания_

3. Чтобы сделать текст жирным, нужно поставить в начале и в конце фрагмента текста ** или __ (не отделяя пробелом):

**две звезды** или __два нижних подчеркивания__

4. Чтобы перечеркнуть текст, используйте ~~ в начале и в конце (не отделяя пробелом):

~~две тильды~~

5. список можно сделать просто написав 1. какой-то пункт (для нумерованного списка) или просто - какой-то пункт (для маркированного списка). После каждого пункта два переноса строки (два enter)

6. Дальнейшие опции посмотрим [тут](https://github.com/adam-p/markdown-here/wiki/Markdown-Here-Cheatsheet)

Для энтузиастов -- [вдохновляющий набор расширений и приложений, где используется Markdown](https://github.com/mundimark/awesome-markdown)

Поэкспериментируйте с языком в тетрадке или оформите с помощью него репозиторий на гитхабе.
    

**Выделение комментариев цветом**

```<div class="alert alert-block alert-info">
<b>Tip:</b> Use blue boxes (alert-info) for tips and notes. 
If it’s a note, you don’t have to include the word “Note”.
</div>```

```<div class="alert alert-block alert-warning">
<b>Example:</b> Yellow Boxes are generally used to include additional examples or mathematical formulas.
</div>```

```<div class="alert alert-block alert-success">
Use green box only when necessary like to display links to related content.
</div>```

```<div class="alert alert-block alert-danger">
It is good to avoid red boxes but can be used to alert users to not delete some important part of code etc. 
</div>```

<div class="alert alert-block alert-info">
<b>Tip:</b> Use blue boxes (alert-info) for tips and notes. 
If it’s a note, you don’t have to include the word “Note”.
</div>

<div class="alert alert-block alert-warning">
<b>Example:</b> Yellow Boxes are generally used to include additional examples or mathematical formulas.
</div>

<div class="alert alert-block alert-success">
Use green box only when necessary like to display links to related content.
</div>

<div class="alert alert-block alert-danger">
It is good to avoid red boxes but can be used to alert users to not delete some important part of code etc. 
</div>

## Система контроля версий

Системы контроля версий позволяют отслеживать изменения в файлах, откатываться к рабочей версии и многое другое. Мы используем **git** и платформу **GitHub** для версионирования и хранения файлов курса.

### git

**Используем командную строку**

Склонировать репозиторий по ссылке
```shell
git clone https://github.com/hse-ling-python/seminars.git
```
Создать репозиторий (локально)
```shell
git init
```
Скачать изменения из удаленного репозитория
```shell
git pull
```
Добавить указанные файлы в список отслеживаемых
```shell
git add ./somefolder/my_file.txt
```
Удалить файл (из git и физически)
```shell
git rm ./somefolder/my_file.txt
```
Удалить файл (из git, но не физически)
```shell
git rm --cache ./somefolder/my_file.txt
```
Посмотреть статус изменений
```shell
git status
```
Закоммитить изменения; после -m в кавычках пишется сообщение о том, что изменено
```shell
git commit -m "add new file"
```
Отправить изменения в удаленный репозиторий
```shell
git push
```

**Через PyCharm**

Слева, где располагается каталог файлов проекта, можно добавить файл в git, а в верхнем меню **VCS -> Commit** написать сообщение коммита и выбрать файлы, которые в него попадут. **VCS -> Git -> Push** запушит изменения, а **VCS -> Git -> Pull**, соответственно, скачает изменения из удаленного репозитория.

## Не работает код, не устанавливается пакет, всё очень плохо

Ошибки и проблемы возникают постоянно, есть много вариантов их решить, но основной и главный способ - погуглить и почитать **Stack Overflow**. Можно просто скопировать сообщение ошибки и первой ссылкой в поиске скорее всего будет именно Stack Overflow. К этому стоит привыкать, потому что не всегда рядом будет человек, который сможет сесть и разобраться в вашей проблеме вместе с вами.

Ну а так как у нас учебный курс, есть еще и альтернативные варианты:

1. Спросить у однокурсников
2. Спросить в чате
3. Написать преподавателю
4. Оставить issue в репозитории

## Система отправки работ

Используем GitHub Classroom. Там будут создаваться задания и репозитории для заданий (после того как вы примете задание), для которых установлен автоматический дедлайн, после которого загрузка закрывается. 

- домашнее задание может быть по нескольким темам
- в этом году заданий много, но большинство заданий не очень большие
- выгодно делать все задания, так как предшествующие задания помогают делать последующие задания

## Оформление

Большую часть домашних заданий можно делать вот в таких jupyter-тетрадках, для каких-то веб-приложений или других более крупных проектов нужен проект или папок и скриптов - это удобнее писать в PyCharm.


## Опрос

Пожалуйста, пройдите опрос: https://forms.gle/9fGrW5Kfu8F5oWLY6 