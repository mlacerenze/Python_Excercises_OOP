"""
Realizar una clase que administre una agenda. Se debe almacenar para cada contacto el nombre, el teléfono y el email. 
Además deberá mostrar un menú con las siguientes opciones

  - Añadir contacto
  - Lista de contactos
  - Buscar contacto
  - Editar contacto
  - Cerrar agenda
"""

class ContactBook:
  def __init__(self):
    self.contacts = [] # creo una lista donde guardo los contactos
    
  def show_menu(self):
    print()
    menu = [
      ['----- CONTACT BOOK -----'],
      ['1- Add Contact'],
      ['2- Show Contact List'],
      ['3- Search Contact'],
      ['4- Edit Contact'],
      ['5- Close']
    ]    
    
    for x in range(6):
      print(menu[x][0])
      
    option = int(input('Choose a option: '))
    if option == 1:
      self.add_contact()
    elif option == 2:
      self.show_list()
    elif option == 3:
      self.search_contact()
    elif option == 4:
      self.edit_contact()
    elif option == 5:
      print('See you later!')
      exit()
    else:
      print('Enter a correct option')
      
    self.show_menu()

  def add_contact(self):
    print('------------------')
    print('Add a new contact')
    print('------------------')
    n = input('Name: ')
    p = input('Phone: ')
    e = input('Email: ')
    self.contacts.append({'Name': n, 'Phone': p, 'Email': e})
    
  def show_list(self):
    print('------------')
    print('Contact List')
    print('------------')
    if len(self.contacts) == 0:
      print('No contacts added.')
    else:
      for x in range(len(self.contacts)):
        print(self.contacts[x]['Name'])
  
  def search_contact(self):
    print('--------------')
    print('Search Contact')
    print('--------------')
    n = input('Enter a contact Name to search: ')
    for x in range(len(self.contacts)):
      if n == self.contacts[x]['Name']:
        print('Contact Info: ')
        print('Name: ', self.contacts[x]['Name'], '\nPhone: ', self.contacts[x]['Phone'], '\nEmail: ', self.contacts[x]['Email'])
        return x 
  
  def edit_contact(self):
    print('------------')
    print('Edit Contact')
    print('------------')
    data = self.search_contact()
    condition = False
    
    while condition == False:
      print('Choose option to edit: ')
      print('1- Name')
      print('2- Phone')
      print('3- Email')
      print('4- Go back')
      
      opt = int(input('Choose a option: '))
      if opt == 1:
        n = input('Enter a new name: ')
        self.contacts[data]['Name']=n
      if opt == 2:
        t = input('Enter a new phone: ')
        self.contacts[data]['Phone']=t 
      if opt == 3:
        e = input('Enter a new email: ')
        self.contacts[data]['Name']=e
      if opt == 4:
        condition = True
        
book = ContactBook()
book.show_menu()      