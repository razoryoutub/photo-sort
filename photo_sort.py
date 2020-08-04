from PIL import Image
import os
import shutil
import time
os.system('cls')
month_c = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
sort = input('Сортировать фото?[y/n]: ')
del_ = input('Удалить пустые папки?[y/n]: ')
if sort == 'y':
	path = input('Введите путь: ')
	print('перемещение фото...')
	time.sleep(3)
	zero_path = path
	def get_date_taken(path): 
		global month_c
		global zero_path
		print(path)
		try:
			year = Image.open(path)._getexif()[36867][0:4]
			month = Image.open(path)._getexif()[36867][5:7]
			try:
				os.mkdir(zero_path + '/' + str(year))			
			except FileExistsError:
				pass
			try:
				os.mkdir(zero_path + '/' + str(year) + '/' + str(month) + '.' + str(month_c[int(month)-1]))
			except FileExistsError:
				pass
			try:
				shutil.move(os.path.join(dirname, filename), zero_path + '/' + str(year) + '/' + str(month) + '.' + str(month_c[int(month)-1]))
			except shutil.Error:
				pass
		except TypeError:
			pass
		except KeyError:
			pass
		except:
			pass
		print('\n')
	for dirname, dirnames, filenames in os.walk(path):
		for filename in filenames:
				if os.path.join(dirname, filename).lower()[-4:] == '.jpg':
					get_date_taken(os.path.join(dirname, filename))
				elif os.path.join(dirname, filename).lower()[-4:] == '.png':
					get_date_taken(os.path.join(dirname, filename))
	#			elif os.path.join(dirname, filename).lower()[-4:] == '.mp4':
	#				get_date_taken(os.path.join(dirname, filename))
	#			elif os.path.join(dirname, filename).lower()[-4:] == '.mov':
	#				get_date_taken(os.path.join(dirname, filename))
	#			elif os.path.join(dirname, filename).lower()[-4:] == '.wmv':
	#				get_date_taken(os.path.join(dirname, filename))
if del_ == 'y':
	if sort != 'y':
		path = input('Введите путь: ')
		zero_path = path
	os.system('cls')
	print('удаление пустых папок...')
	time.sleep(3)
	rm_temp = 0
	def del_empty_dirs(path):
		for d in os.listdir(path):
			a = os.path.join(path, d)
			if os.path.isdir(a):
				del_empty_dirs(a)
				if not os.listdir(a):
					os.rmdir(a)
					print(a, 'удалена')
					global rm_temp
					if rm_temp == 0:
						rm_temp = 1
	del_empty_dirs(zero_path)
	if rm_temp == 0:
		print('пустых папок обнаружено не было!')