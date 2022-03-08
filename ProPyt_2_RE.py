import re
from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
import os
contact_list_return = []

file_path = (os.path.split(__file__)) # Считывает текущую директорию скрипта, тут же должен храниться файл CSV
os.chdir(file_path [0]) # Устанавливает директорию
with open("phonebook_raw.csv", encoding='utf_8') as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
pprint(contacts_list)

# # TODO 1: выполните пункты 1-3 ДЗ
# # ваш код
pattern_phones = r"(\+7|8)\s*\(*(\d{3})\)*(\s*|-?)(\d{3})(\s*|-?)(\d{2})(\s*|-?)(\d{2})\s*\(?\s*(\bдоб\b)?(\.?)\s*(\d{4})?\)?"
sub_phones = r"+7(\2)\4-\6-\8 \9\10\11"
for var_1 in contacts_list:
    var_2 = var_1[0].split()
    if len(var_2) > 1:
        for var_3 in range (0, len(var_2)):
          var_1 [var_3] = var_2 [var_3]
    var_1[5] = re.sub(pattern_phones,sub_phones,var_1[5])    
    pprint(var_1)     
    contact_list_return.append(var_1)    
pprint(contact_list_return)        
    


# # TODO 2: сохраните получившиеся данные в другой файл
# # код для записи файла в формате CSV
# with open("phonebook.csv", "w") as f:
#   datawriter = csv.writer(f, delimiter=',')
#   # Вместо contacts_list подставьте свой список
#   datawriter.writerows(contacts_list)