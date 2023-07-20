import functions  # import readToDO, writeToDo
import time
# file = open(r'C:\Users\e10111732\Documents\file.txt','r')
# toDos = list()
now = time.strftime('%b %d, %Y %H:%M:%S')
print(f"It is {now}")
toDos = functions.readToDO()
while True:
    if [] == toDos:
        user_action = input('To Do Actions: add/show/edit/exit: ')
        user_action = user_action.strip()

    else:
        user_action = input('To Do Actions: add/show/edit/complete/exit : ')
        user_action = user_action.strip()
    if  user_action.startswith('add'):
        toDos.append(user_action[3:].strip())
        functions.writeToDo(toDos)


    elif user_action.startswith('show'):
        for i in range(len(toDos)):
            print(f'{i + 1}. {toDos[i].strip()}')
    elif user_action.startswith('edit'):
        try:
            toDos[int(user_action[4:].strip())-1] = input('Enter the change: ')
            print(toDos)

        except IndexError:
            print('You do not have that many toDos')
        except ValueError:
            print("Your input is not valid")
        finally:
            continue
    elif user_action.startswith('complete'):
        if toDos == []:
            print('You are all caught up')
            continue
        else:
            try:
                # complete_prompt = int(input('Enter the number of the toDo you want to complete: '))
                removed_todo = toDos.pop(int(user_action[8:].strip()) - 1).strip('\n')
                functions.writeToDo(toDos)

                print(f'You have completed the TO DO: {removed_todo}')

            except IndexError:
                print('There is no to do item at your selection')
    elif user_action.startswith('cancel'):
        continue

    elif user_action.startswith('exit'):
        print('bye')
        break
    else:
        print('Invalid Command')
