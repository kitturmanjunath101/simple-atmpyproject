def main():
    print('Welcome To ATM')
    restart = 'Y'
    attempts = 3
    balance = 10000.13
    while attempts >= 0:
        pin = int(input('Please Enter Your 4 Digit Pin : '))
        if pin == 9019:
            print('Correct Pin :)\n')
            while restart not in ('n', 'NO', 'no', 'N'):
                print('Enter 1 for Balance Enquiry : \n')
                print('Enter 2 for Withdrawal : \n')
                print('Enter 3 for Deposit Money : \n')
                print('Enter 4 for Quit : \n')
                option = int(input('What Would you like to choose? '))
                if option == 1:
                    print('Your Balance is Rs', balance, '\n')
                    restart = input('Would You you like to go back? ')
                    if restart in ('n', 'NO', 'no', 'N'):
                        print('Thank You')
                        break
                elif option == 2:
                    option2 = 'y'
                    withdrawal = float(input('How Much Would you like to withdraw? '
                                             '\n(Rs 10/Rs 20/Rs 40/Rs 60/Rs 80/Rs 100) : '))
                    if withdrawal in [10, 20, 40, 60, 80, 100]:
                        balance = balance - withdrawal
                        print('\nYour Balance is now Rs', balance)
                        restart = input('Would You you like to go back? ')
                        if restart in ('n', 'NO', 'no', 'N'):
                            print('Thank You')
                            break
                    elif withdrawal != [10, 20, 40, 60, 80, 100]:
                        print('Invalid Amount, Please Re-try\n ')
                        restart = 'y'
                    elif withdrawal == 1:
                        withdrawal - float(input('Please Enter Desired amount: '))
                elif option == 3:
                    deposit = float(input('How Much Would You Like To Deposit? '))
                    balance = balance + deposit
                    print('\nYour Balance is now Rs', balance)
                    restart = input('Would You you like to go back? ')
                    if restart in ('n', 'NO', 'no', 'N'):
                        print('Thank You')
                        break
                elif option == 4:
                    print('Please wait whilst your card is Returned...\n')
                    print('Thank you...')
                    break
                else:
                    print('Please Enter a correct number. \n')
                    restart = 'y'
        elif pin != 9019:
            print('Incorrect Password')
            chances = chances - 1
            if chances == 0:
                print('\nNo more tries :(')
                break

if __name__ == '__main__':
    main()