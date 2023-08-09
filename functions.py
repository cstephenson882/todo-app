import os
def readToDO(filepath='../app1/files/toDos.txt'):
	if not os.path.exists('../app1/files/toDos.txt'):
		file = open('../app1/files/toDos.txt', 'w')
	with open(filepath, 'r') as file:
		toDos = file.readlines()
		return toDos
def writeToDo(toDos,filepath = '../app1/files/toDos.txt'):
	with open(filepath, 'w') as file:
		file.writelines(toDos)

if __name__ == '__main__':
	print ( f'Now running "functions" ')