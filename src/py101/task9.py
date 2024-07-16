from to_do import TODO


def task9() -> str:
    return """
        WHILE TRUE
            DISPLAY "Welcome to Python Bank ATM - Cash Withdrawal"
            while insert the card:
                Enter Your Password
                IF Password==True:
                    Enter amount of money you wanted to withdraw
                    IF (amount MOD 10) != 0 THEN
                      DISPLAY "You can only withdraw a multiple of ten!"
                    ELSE
                      IF amount<10 OR amount>200 THEN
                         DISPLAY "You can only withdraw between £10 and £200"
                      ELSE
                         notes20 = amount DIV 20
                         notes10 = (amount MOD 20) / 10
                         DISPLAY "Collect your money: "
                         DISPLAY "    >> £20 Banknotes: " + notes20
                         DISPLAY "    >> £10 Banknotes: " + notes10
                         DISPLAY "Thank you for using this Python Bank ATM."
                         DISPLAY "Good Bye."
                    
                ELSE
                    password is not True
    """
