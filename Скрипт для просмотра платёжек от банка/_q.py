from os.path import isfile, join
from os import listdir, system

## settings section
show_empty_fields = 0

# define section # do not edit this values! #
HEADER = 0
H_VERSION = 1
H_SUMM = 21
H_DATE = 16
clear = lambda: system('cls')
showmenu = lambda: 	print('Введите команду:\n \
1: Отобразить число записей\n \
2: Показать мета-информацию\n \
3: Отобразить все поля определенной записи\n \
4: Отобразить все записи\n \
5: Отобразить дату формирования\n \
6: Отобразить общую сумму\n \
7: Отобразить версию документа \n \
0: Очистить экран\n \
*: Остановить программу')
#
mypath = '.'
curfile = ''
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f)) and f[-3:-1] == "BD"]
content = ''
if onlyfiles:
	if len(onlyfiles) > 1:
		print('Выберите файл для открытия:')
		for i in range(len(onlyfiles)):
			print(str(i+1) + ': ' + onlyfiles[i])
		inp = int(input())-1
		curfile = onlyfiles[inp]
	else:
		curfile = onlyfiles[0]
	clear()
	print('Открыт файл '+ curfile)
	with open(curfile, 'r') as file_to_read:
		content = file_to_read.read().split('BDPD|')
		l = list()
		for i in range(len(content)):
			l.append(content[i].split('|'))
			
	system('title открыт файл '+ curfile +' от '+ l[HEADER][H_DATE])
	showmenu()
	while 1:
		input_value = int(input())
		if input_value == 0:
			clear()
			showmenu()
		elif input_value == 1:
			print('Всего записей: ', len(content)-1)
		elif input_value == 2:
			print(l[HEADER])
		elif input_value == 3:
			print('	Введите номер записи: (1-'+str(len(content)-1)+')')
			input_value = int(input())
			for j in range(len(l[input_value])):
				if l[input_value][j] != '' or show_empty_fields:
					print(j, l[input_value][j])
		elif input_value == 4:
			for i in range(len(l)):
				print(l[i])
		elif input_value == 5:
			print('Дата формирования: '+l[HEADER][H_DATE])
		elif input_value == 6:
			print('Сумма платежей в файле: '+l[HEADER][H_SUMM])
		elif input_value == 7:
			print('Версия: '+l[HEADER][H_VERSION]+' от '+l[HEADER][H_VERSION][-2:]+'.'+l[HEADER][H_VERSION][-4:-2]+'.20'+l[HEADER][H_VERSION][-6:-4])
		else:
			break
else:
	print('Не обнаружен файл с платежами от банка.\nСкопируйте его в папку со скриптом.')