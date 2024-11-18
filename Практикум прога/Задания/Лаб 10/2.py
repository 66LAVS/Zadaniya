def read_students_from_file(file_path): 
    """Читает данные студентов из файла и возвращает список списков.""" 
    students = [] 
    try: 
        with open(file_path, 'r', encoding='utf-8') as file: 
            for line in file: 
                parts = line.strip().split(';') 
                if len(parts) == 4: 
                    students.append(parts) 
        return students 
    except FileNotFoundError: 
        print(f"Ошибка: файл {file_path} не найден.") 
        return None 

def sort_students_by_age(students): 
    """Сортирует список студентов по возрасту (возраст - третий элемент в списке).""" 
    def get_age(student): 
        """Вспомогательная функция для извлечения возраста.""" 
        return int(student[2]) 

    students.sort(key=get_age)  # Сортировка по возрасту с использованием функции get_age 
    return students 

def age_rem(students): 
    for i in students: 
        i[2] = str(int(i[2]) - 1)  # Преобразование возраст в строку

def save_students_to_file(students, output_file_path): 
    with open(output_file_path, 'w', encoding='utf-8') as file: 
        for student in students: 
            file.write(';'.join(map(str, student)) + '\n')  # Использование map для преобразования элементов в строку

output_file_path = 'students_.txt' 

file_path = 'Практикум прога/Задания/Лаб 10/students.txt' 
students = read_students_from_file(file_path) 

if students: 
    sorted_students = sort_students_by_age(students) 
    print("\nСтуденты, отсортированные по возрасту:") 
    for student in sorted_students: 
        print(student) 

    age_rem(students) 

    print("\nСтуденты, возраст -1:") 
    for student in students: 
        print(student) 

    save_students_to_file(students, output_file_path) 

    print("\nСтуденты с уменьшенным возрастом сохранены в файл:", output_file_path)
