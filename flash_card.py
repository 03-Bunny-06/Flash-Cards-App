import random

name = input('Enter your name to start: ')
print('\n')

def flash_card_choice():
    print(f'Hello {name}, Welcome to the Flash Cards App.\n1. Create a Flash Card.\n2. Display Flash Cards.\n3. Test the knowledge using Flash Cards.\n4. Exit.\n')

a = True
flash_cards = [
  {"serial": 1, "title": "What is Node.js?", "answer": "Node.js is a tool that lets you use JavaScript to build websites and apps on the server."},
  {"serial": 2, "title": "How to Check Node.js Installation", "answer": "Type `node -v` in the terminal to see if Node.js is installed."},
  {"serial": 3, "title": "What is SQL?", "answer": "SQL is a language used to store and manage data in databases."},
  {"serial": 4, "title": "Starting a Node.js Project", "answer": "Run `npm init` to create a new project and set up your app."},
  {"serial": 5, "title": "How to Install a Node.js Package", "answer": "Run `npm install <package-name>` to add tools or libraries to your project."},
  {"serial": 6, "title": "What is a Database?", "answer": "A database is a place to store and organize data, like tables in Excel."},
  {"serial": 7, "title": "How to Select Data with SQL", "answer": "Use `SELECT * FROM table_name;` to get all the data from a table."},
  {"serial": 8, "title": "Running a Node.js File", "answer": "Type `node filename.js` in the terminal to run a Node.js file."},
  {"serial": 9, "title": "How to Insert Data with SQL", "answer": "Use `INSERT INTO table_name (column1, column2) VALUES ('value1', 'value2');`."},
  {"serial": 10, "title": "What is npm?", "answer": "npm (Node Package Manager) is a tool that helps you install and manage libraries in Node.js."}
]


while a:
    def flash_card_functionality(choice):
        if choice not in ['1','2','3','4']:
            print("The choice is invalid. Please select a valid option.")
        else:
            if (choice == '1'):
                print("-Flash Card Creation-")
                create()
            elif (choice == '2'):
                print("-Flash Card Display-")
                display()
            elif (choice == '3'):
                print("-Flash Card Testing-")
                answer()
            elif (choice == '4'):
                exit()

    def create():
        title = input('Enter the title of flashcard: ')
        answer = input('Enter the description for the flashcard: ')
        serial = len(flash_cards) + 1
        new_card = {"serial": serial, "title": title, "answer": answer}
        flash_cards.append(new_card)
        print('New flash cards created successfully!!')

    def display():
        for card in flash_cards:
            print(f'{card['serial']}: {card['title']}' )
            print(f'A: {card['answer']}\n')
    
    def answer():
        random_question = random.choice(flash_cards)
        print(f'Q: {random_question['title']}')

        user_answer = input('Enter the answer for the question: ')
        if (user_answer == random_question['answer']):
            print('You have got it right!')
        else:
            print('Sorry! Your answer is wrong :(')
    
    def exit():
        global a
        print('Thanks for using our Flash Cards App.')
        a = False

    flash_card_choice()
    choice = input('Enter the choice (1-4): ')
    flash_card_functionality(choice)