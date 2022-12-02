<<<<<<< HEAD
![sunrise image](./icon.png)

=======
# :sunrise_over_mountains:
>>>>>>> 920bf75493e5fa8a9444960e8e9e28af02505e53

# sunrise
search for similar days in different semesters

Приложение для поиска похожего дня, по определенным параметрам, из другого полугодия.

Первое полугодие с 23 декабря по 20 июня включительно, второе полугодие с 22 июня по 20 декабря.
21 июня, 21 и 22 декабря игнорируются.

----------------------------------------------------------------------------------------------------------
В качестве источника данных используется файл sunrise_data.csv содержащий в себе обязательные столбцы:
  1. day - число, от 1 - 31
  2. month - номер месяца, от 1 - 12
  3. sunrise - время восхода солнца, в формате HH:MM
  4. sunset - время захода солнца, в формате HH:MM
  5. dlh - продолжительность дня, в формате HH:MM:SS

Файл sunrise_data.csv должен распологаться в корне. Файл который представлен здесь слдержит данные для г.Сегежа(63.7 северной широты 34.3 восточной долготы) на 2022 год.

------------------
bash скрипт. Должен быть исполняемым файлом.

    #!/bin/bash
    path/to/python ./sunrise_kivy.py
***
desktop файл для запуска с рабочего стола.
Расположить в ~/.local/share/applications/ или непосредственно на рабочем столе, но в этом случае его не будет в меню запуска.

    [Desktop Entry]
    Comment[ru_RU]=
    Comment=
    Encoding=UTF-8
    Exec=./bash path/to/project/sunrise/sunrise.sh
    GenericName[ru_RU]=санрайс
    Icon=path/to/project/sunrise/src/images/icon.png
    Name[ru_RU]=SunRise
    Name=SunRise
    Path=path/to/project/sunrise/
    StartupNotify=true
    Terminal=false
    Type=Application
    Version=1.0
    X-KDE-RunOnDiscreteGpu=false
    X-KDE-SubstituteUID=false

