file = open("text.txt", "r", encoding="utf-8") #Открываем файл text.txt
lines = file.readlines()  # Читаем все строки из файла
file.close()
file2 = open("output.txt", "w", encoding="utf-8")  #Открываем файл output.txt
for line in lines: #Используем цикл for
    line2 = line.replace('о', 'a')  # Заменяем 'о' на 'a'
    file2.write(line2)  # Записываем измененную строку в файл output.txt
file2.close()