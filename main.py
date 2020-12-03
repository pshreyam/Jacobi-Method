import sys

from jacobi import JacobiMethod

def setup():
    try:
        print('\n--- Jacobi Iterative Solver 🚀 ---\n')
        number_of_variables = int(input('\nEnter the number of variables (at least 2): '))

        if number_of_variables < 2:
            print('There must be at least two variables.')
            raise ValueError('The equation must contain at least 2 variables.')
 
        print('\nFormat of your system of equations:')
        for i in range(number_of_variables):
            for j in range(number_of_variables):
                print(f"a_{i+1}_{j+1} * x{j+1}", end="")
                if not j == number_of_variables - 1:
                    print(" + ", end="")
            print(f" = b_{i+1}")

        return number_of_variables
    
    except Exception:
        return setup()  
           

def get_user_input(number_of_variables):
    M = [[0 for _ in range(number_of_variables)] for _ in range(number_of_variables)]
    N = [0 for _ in range(number_of_variables)]

    print('\nEnter the constants of the equations:')
    for i in range(number_of_variables):
        print()
        for j in range(number_of_variables):
            M[i][j] = float(input(f"a_{i+1}_{j+1} : ") or 0)
        N[i] = float(input(f"b_{i+1} : ") or 0)

    print('\nSystem of linear equations:')
    for i in range(number_of_variables):
        for j in range(number_of_variables):
            print(f"({str(M[i][j])}) * x{j+1}", end="")
            if not j == number_of_variables - 1:
                print(" + ", end="")
        print(f" = ({N[i]})")    
    print()

    return M, N

def main():
    n = setup()
    A, b = get_user_input(n)
    acc = int(input("Enter the number of decimal digits for accuracy: "))
    print("\nEnter initial guess (Defaults to 0):")
    ini_guess = [float(input(f"x{i+1}: ") or 0) for i in range(n)]
    jm = JacobiMethod(A, b, ini_guess, acc)
    jm.calculate()

try:
    main()
except KeyboardInterrupt:
    print('\n--- Program Terminated! Sad to see you go ---\n')  
except ZeroDivisionError:
    print('Sorry! Division by zero witnessed')
finally:
    sys.exit(0)
