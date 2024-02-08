def newton_interpolation(x_list, y_list, x_value):
    length = len(x_list)
    y_copy = y_list

    for i in range(1, length):
        print("Interação_principal: "+str(i))
        for j in range(length-1, i-1, -1):
            print("interação_segundaria: "+str(j))
            y_copy[j] = (y_copy[j] - y_copy[j-1])/(x_list[j] - x_list[j-i])
            print(y_copy[i])
        print("\n")

    new_value = y_copy[length - 1]
    for x in range(length - 2, -1, -1):
        print("Interação de p: " + str(x))
        print("Inicio: " + str(new_value))
        new_value = new_value * (x_value - x_list[x]) + y_copy[x]
        print("Fim: " + str(new_value))
        print("\n")
    return new_value


def menu():
    x_input = input('Digite os valores de x, os separando por espaços: ')
    y_input = input('Digite os valores de y, os separando por espaços: ')
    x_value = float(input('Digite o valor de x que se quer interpolar: '))

    x = x_input.split(" ")
    y = y_input.split(" ")

    x_float = []
    y_float = []

    for i in range(len(x)):
        x_number = float(x[i])
        y_number = float(y[i])

        x_float.append(x_number)
        y_float.append(y_number)

    result = newton_interpolation(x_float, y_float, x_value)
    print("o resultado da interpolação é: "+str(result))

def start_menu():
    try:
        menu()
    except:
        print("Reinicie o processo")
        print("\n")
        start_menu()

start_menu()
