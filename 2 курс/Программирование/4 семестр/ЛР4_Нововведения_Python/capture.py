# Простой пример приветствия нового пользователя

def Hi(name=None):
  match name:
    case None:
      print('Enter UserName!')
    case UserName:
      print(f'Hello my dear {UserName}')
      
print('1) name = None')
Hi()

Name = str(input('2) Enter a UserName:'))
Hi(Name)