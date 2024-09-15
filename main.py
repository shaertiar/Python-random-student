import os
import json
import random

def main():
    def draw_logo():
        os.system('CLS')
        print('██████╗ ██╗   ██╗    ██╗  ██╗██╗███╗   ███╗')
        print('██╔══██╗╚██╗ ██╔╝    ██║ ██╔╝██║████╗ ████║')
        print('██████╔╝ ╚████╔╝     █████╔╝ ██║██╔████╔██║')
        print('██╔══██╗  ╚██╔╝      ██╔═██╗ ██║██║╚██╔╝██║')
        print('██████╔╝   ██║       ██║  ██╗██║██║ ╚═╝ ██║')
        print('╚═════╝    ╚═╝       ╚═╝  ╚═╝╚═╝╚═╝     ╚═╝')
        print('                                           ')
        print(' █████╗ ██████╗ ████████╗██╗   ██╗██████╗  ')
        print('██╔══██╗██╔══██╗╚══██╔══╝██║   ██║██╔══██╗ ')
        print('███████║██████╔╝   ██║   ██║   ██║██████╔╝ ')
        print('██╔══██║██╔══██╗   ██║   ██║   ██║██╔══██╗ ')
        print('██║  ██║██║  ██║   ██║   ╚██████╔╝██║  ██║ ')
        print('╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝ ') 
        print()

    # Функция создания файла
    def create_file(filename):
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump({}, file)

    # Цикл
    while True:
        draw_logo()
        print('[0] - Выход')
        print('[1] - Изменить цветовую схему')
        print('[2] - Выбрать класс')
        
        answer = input('[?]: ')
        
        if answer == '0': break
        
        elif answer == '1':
            print('  [1] - \033[91mТакой текст.\033[0m   [2] - \033[92mТакой текст.\033[0m')
            print('  [3] - \033[93mТакой текст.\033[0m   [4] - \033[94mТакой текст.\033[0m')
            print('  [5] - \033[95mТакой текст.\033[0m   [6] - \033[96mТакой текст.\033[0m')
            print('  [7] - \033[0mТакой текст.\033[0m')
            
            answer = input('  [?]: ')
            if answer == '1': print('\033[91m')
            elif answer == '2': print('\033[92m')
            elif answer == '3': print('\033[93m')
            elif answer == '4': print('\033[94m')
            elif answer == '5': print('\033[95m')
            elif answer == '6': print('\033[96m')
            
        elif answer == '2':
            selected_class = input("  Введите класс (например 9О; 0 - вывести все классы): ").lower()

            if selected_class == '0':
                try:
                    # Вывод всех классов
                    classes = os.listdir('classes')
                    for filename in classes:
                        if filename.endswith('.json'):
                            print(f'    {filename[:-5].upper()}')
                    if not classes:
                        print('    Пока-что классов нет.')
                except FileNotFoundError:
                    print(f'    Кажеться папка с классами пропала... Но мы ее уже пересоздали!')
                    print('    Пока-что классов нет.')
                    os.mkdir('classes')
                    
                input('    Enter для продолжения...')

            # Создание класса, если его нет
            elif not os.path.exists(f'classes/{selected_class}.json'):
                # Создавать файл при разрешении
                if input(f'    Класс "{selected_class.upper()}" не найден. Создать? (д/н): ').lower() == 'д':
                    
                    try:
                        create_file(f'classes/{selected_class}.json') # Создание файла
                        print(f'      Класс "{selected_class.upper()}" создан.')
                    except FileNotFoundError:
                        print(f'      Кажеться папка с классами пропала... Но мы ее уже пересоздали!')
                        os.mkdir('classes')
                        
                        create_file(f'classes/{selected_class}.json') # Создание файла
                        print(f'      Класс "{selected_class.upper()}" создан.')
                    
                    students = json.load(open(f'classes/{selected_class}.json', 'r', encoding='utf-8')) # Получение файла
                    max_index = len(students)+1 # Получение индекса
                    
                    # Добавление учеников по очереди
                    while (name := input(f"      По номеру введите имена учеников (0 - прекратить ввод) №{max_index}: ")) != '0':
                        students[str(max_index)] = name
                        max_index += 1
                        
                    # Выгрузка файла
                    json.dump(students, open(f'classes/{selected_class}.json', 'w', encoding='utf-8'))

            else:
                # Получение списка учеников
                students = json.load(open(f'classes/{selected_class}.json', 'r', encoding='utf-8'))
                
                # Цикл
                while True:
                    draw_logo()
                    print(f'Класс: {selected_class.upper()}')
                    print(f'[0] - Назад')
                    print(f'[1] - Добавить/переименовать ученика')
                    print(f'[2] - Выбрать случайного ученика ученика')
                    print(f'[3] - Вывод список учеников')
                    
                    answer = input('[?]: ')
                    
                    if answer == '0': break
                    
                    elif answer == '1':
                        # Получение всех данных
                        if (index := input('    Введите номер ученика(0 - назад): ')) == 0:
                            name = input('    Введите имя ученика: ')
                            
                            students[index] = name
                                
                            # Выгрузка файла
                            json.dump(students, open(f'classes/{selected_class}.json', 'w', encoding='utf-8'))
                        
                    elif answer == '2':
                        if students:
                            # Выбор случайного ученика
                            index = random.randint(1, len(students))
                            
                            print(f'  Выбран ученик: №{index} - {students[str(index)]}!\n')
                            
                            input('  Enter для продолжения...')
                        else:
                            print('    Список учеников пуст.')
                            
                            input('    Enter для продолжения...')
                        
                    elif answer == '3':
                        for student in students:
                            print(f'  №{student} - {students[student]}')
                            
                        input('  Enter для продолжения...')
                        
if __name__ == '__main__':
    try:
        main()
    except:
        print("Ошибочка...")

        input('  Enter для выхода...')

print('\033[0m')
