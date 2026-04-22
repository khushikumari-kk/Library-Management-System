
# database
books = []
issued_books = []
# add function
def add_book():
     name = input('Enter the book name:')
     books.append(name)
     print(name,'is added successfully')
# show function
def show_books():
     if len(books) ==0:
          print('No books available')
     else:
          print('Available books')
          for b in books:
               print(b)
#issue function
def issue_book():
     if len(books) ==0:
          print('No books available')
          return
     else:
          show_books()
          name = input('Enter the book name you want to issue')
          if name in books:
           issued_books.append(name)
           books.remove(name)
           print(name,'is issued')
          else:
               print(name,'is not available')
#return function
def return_book():
     name = input('Enter the book name you want to return: ')
     if name in issued_books:
          issued_books.remove(name)
          books.append(name)
          print(name,'book returned')
     else:
          print(name,'book was never issued')

          
def library():
 while True:
         print('Menu')
         print('1.Add Book')
         print('2.Show Books')
         print('3.Issue Book')
         print('4.Return Book')
         print('5.Exit')
         choice = int(input('Enter your choice: '))
         if choice == 1:
               add_book()
         elif choice == 2:
              show_books()
         elif choice == 3:
              issue_book()
         elif choice == 4:
              return_book()
         elif choice == 5:
              print('Thank you!')
              break
library()
     


