groupmates = [
 {
 "name": "Владимир",
 "surname": "Путин",
 "exams": ["Информатика", "ЭЭиС", "Web"],
 "marks": [4, 3, 5]
 },
 {
 "name": "Александр",
 "surname": "Лукашенко",
 "exams": ["История", "АиГ", "КТП"],
 "marks": [4, 4, 4]
 },
 {
 "name": "Дональд",
 "surname": "Трамп",
 "exams": ["Философия", "ИС", "КТП"],
 "marks": [5, 5, 5]
 },
 {
  "name": "Владимир",
  "surname": "Зеленский",
  "exams": ["Философия", "ИС", "КТП"],
  "marks": [3, 4, 5]
 },
{
  "name": "Александр",
  "surname": "Первый",
  "exams": ["Философия", "ИС", "КТП"],
  "marks": [4, 4, 5]
 }
]


def count_mark(students, mark):
 print(u"name".ljust(15), u"surname".ljust(10), u"exams".ljust(30), u"marks".ljust(20))
 for student in students:
  marks_list = student['marks']
  result = (sum(marks_list) / len(marks_list))
  if result > mark:
    print(student["name"].ljust(15),
       student["surname"].ljust(10), str(student["exams"]).ljust(30),
       str(student["marks"]).ljust(20))

need = float(input('Input :'))

count_mark(groupmates, need)