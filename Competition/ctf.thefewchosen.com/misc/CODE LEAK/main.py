import ast

from controller import Controller

user = input("Enter your name: ")
controller = Controller(user)

def safe_eval(code):
  tree = compile(code, "<string>", 'exec', flags=ast.PyCF_ONLY_AST)
  for x in ast.walk(tree):
    if type(x) not in (ast.Module, ast.Expr, ast.Attribute, ast.Name, ast.Load):
      return "Invalid operation"

  return eval(code)

def secret_debugger():
  while True:
    try:
      code = input("DEBUG>>> ")
      print(safe_eval(code))
    except Exception as x:
      print(x)
      break

def menu():
  while True:
    print("""What would you like to do?
    1. Check balance
    2. Work
    3. Buy hint ($30)
    4. Buy flag ($1337)
    5. Exit
    """)

    choice = input(">>> ")
    message = ""

    if choice == "1":
      message = controller.check_balance()
    elif choice == "2":
      message = controller.work()
    elif choice == "3":
      message = controller.buy_hint()
    elif choice == "4":
      message = controller.buy_flag()
    elif choice == "5":
      print("Bye!")
      exit()

    if choice == "42":
      secret_debugger()

    print(message)

menu()