class MonthlyData:
    def __init__ (self, month, payment, principal, interest, total_interest, balance):
        """
        store all monthly loan data
        """
        self.month = month  #number of month
        self.payment = payment  #amount of the loan
        self.principal = principal  #monthly principal
        self.interest = interest    #monthly interest
        self.total_interest = total_interest    #total interest so far
        self.balance = balance  #amount left to pay back

class EndYear:
    def __init__ (self, end_year_msg):
        """
        place an end of year message in the 
        interest column
        """
        self.interest = end_year_msg
