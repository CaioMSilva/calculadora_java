print('BEM-VINDO A CALCULADORA')

num1 = float(input('escreva o primeiro numero: '))
num2 = float(input('escreva o segundo numero: '))
op = input('escreva o operador: ')

match op:
      case '+':
        print(num1 + num2)
      case '-':
        print(num1 - num2)
      case '*':
        print(num1 * num2)
      case '/':
        print(num1 / num2)
      case '//':
        print(num1 // num2)
      case '**':
        print(num1 ** num2)
      case '%':
        print(num1 % num2)
      case _:
        print('operador invalido')
