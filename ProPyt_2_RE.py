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
# pprint(contacts_list)

# # TODO 1: выполните пункты 1-3 ДЗ
# # ваш код
pattern_phones = r"(\+7|8)\s*\(*(\d{3})\)*(\s*|-?)(\d{3})(\s*|-?)(\d{2})(\s*|-?)(\d{2})\s*\(?\s*(\bдоб\b)?(\.?)\s*(\d{4})?\)?"
sub_phones = r"+7(\2)\4-\6-\8 \9\10\11"
for var_1 in contacts_list:     # Как бы в одном цикле всё замутить??? Идей нет, пока.
    for i1 in range (0, 2):
      var_2 = var_1[i1].split()
      if len(var_2) > 0:
        for i2 in range (0, len(var_2)):
          var_1 [i2+i1]  = var_2 [i2]    
    var_1[5] = re.sub(pattern_phones,sub_phones,var_1[5])    
    contact_list_return.append(var_1)    
    
# pprint(contact_list_return)        
del_elem_list = []
len_list = len(contact_list_return)
i3 = 0
while i3 < len_list:
    var_1 = contact_list_return [i3]
    i1 = 1 
    while i1 < len_list:
        var_2 = contact_list_return[i1]
        if var_1[0] == var_2[0] and var_1[1] == var_2[1] and i1 != i3:
         for i2 in range (2,7):
           if len(var_2[i2]) == 0:
            var_2[i2] = var_1[i2] 
           if len(var_1[i2]) == 0:
            var_1[i2] = var_2[i2]
         contact_list_return[i3] = var_2
         del contact_list_return[i1]   
         len_list = len(contact_list_return)
        i1+=1
    i3+=1   
# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w") as f:
  datawriter = csv.writer(f, delimiter=',')
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(contact_list_return)