#the calculator project

def add(n1,n2):
  return n1+n2
def sub(n1,n2):
  return n1-n2
def mul(n1,n2):
  return n1*n2
def div(n1,n2):
  return round(n1/n2,1)

operation={
  "+":add,
  "-":sub,
  "*":mul,
  "/":div
}


num1=float(input("Enter your first number: "))

end=0
while end==0:
  for i in operation:
    print(i)

  op = input("Pick and operation from the options above:\n")
  num2 = float(input("Enter your next number: "))
  answer=operation[op](num1,num2)

  print(f"{num1} {op} {num2} = {answer}\n")

  yor=input(f"Enter 'y' if you want to continue with {answer},\nEnter 'new' to start a new calculation,\nEnter 'n' to stop\n")
  if yor=="y":
    num1=answer
    continue
  elif yor =='new':
    num1 = float(input("Enter your first number: "))
    continue
  else:
    break


