#This is Jose Mata's submission for COMP 540 - Automata's CFG Project. Fall 2024, Bridgewater State University



while True: 
    answer = input("Please enter '1' to produce a random string from the CFG shown in the assignment instructions, '2' to display the production rules of this grammar, or '3' to exit the pogram.\n")
    if answer == '1':
        print("The following is a random string produced by the CFG Grammar.\n\n")
    elif answer == '2':
        print("The following are the production rules of this grammar:\nS:AB\nS:aS\nA:aA\nA:b\nB:bB\nB:a\nStart symbol: S\n\n")
    elif answer == '3':
        print("Exiting the program...\n")
        break
    else:
        print("Answer is invalid.\n")
