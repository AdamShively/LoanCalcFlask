from scheduledata import MonthlyData, EndYear

class LoanCalc:

    def get_data(initial_bal, rate, term):
        """
        get loan data
        :param initial_bal: float
        :param rate: float
        :param term: float
        :return: list of a list with monthly data and 
        a list of overall data including monthly payment
        """
        remaining_bal = initial_bal
        num_of_months = int(12*term)  # number of months, convert years to months
        monthly_payment = calc_monthly_payment(remaining_bal, rate, num_of_months)
        total_interest = 0
        schedule_data = []

        for month in range(1, num_of_months+1):

            monthly_interest = calc_monthly_interest(rate, remaining_bal)

            total_interest = calc_total_interest(total_interest, monthly_interest)

            monthly_principal = calc_monthly_principal(monthly_payment, monthly_interest)

            remaining_bal = calc_remaining_balance(remaining_bal, monthly_principal)

            md = MonthlyData(
                    month, 
                    format_dollar(monthly_payment), 
                    format_dollar(monthly_principal), 
                    format_dollar(monthly_interest), 
                    format_dollar(total_interest), 
                    format_dollar(remaining_bal)
                    )
            schedule_data.append(md)

            #If end of a year add a meddage indicating so.
            if month % 12 == 0:
                ey = EndYear(f'End of Year {month//12}')
                schedule_data.append(ey)

        total_cost = initial_bal + total_interest
        
        overview_data = [
                        format_dollar(monthly_payment),
                        format_dollar(initial_bal), 
                        format_dollar(total_interest), 
                        format_dollar(total_cost)
                        ]

        return schedule_data, overview_data

def calc_monthly_payment(amount, rate, n):
        """
        Calculate monthly payment using formula
        a is loan amount
        r is recalculated interest rate
        n is number of months
        p is monthly payment
        p = a / [(((1+r)^n)-1) / (r(1+r)^n)]

        :param amount: float
        :param rate: float
        :param n: int
        :return float: monthly payment
        """

        #convert % to decimal and multiple by 12 for monthly rate
        convert_to_monthly =  100*12 
        r = rate/convert_to_monthly #recalulated rate

        divisor_1 = (((1+r)**n)-1)
        divisor_2 = (r*((1+r)**n))

        monthly_payment = amount/(divisor_1/divisor_2)

        return monthly_payment

def calc_monthly_interest(rate, remaining_balance):
    """
    Calculate monthly interest
    :param rate: float
    :param remaining_balance: float
    :return: float monthly interest
    """

    convert_to_monthly =  100*12 
    r = rate/convert_to_monthly 
    return remaining_balance * r

def calc_monthly_principal(monthly_payment, monthly_interest):
    """
    Calculate monthly principal
    :param monthly_payment: float
    :param monthly_interest: float
    :return: float monthly principal
    """

    return monthly_payment - monthly_interest

def calc_remaining_balance(remaining_balance, monthly_principal):
    """
    Calculate monthly remaining balance
    :param remaining_balance: float
    :param monthly_interest: float
    :return: float monthly remaining balance
    """

    return remaining_balance - monthly_principal

def calc_total_interest(total_interest, monthly_interest):
    """
    :param total_interest: float
    :param monthly_interest: float
    Calculate total interest
    :return: float monthly total interest
    """

    return total_interest + monthly_interest

def format_dollar(number):
    """
    :param number: float
    Format dollar amount to two decimal places with commas
    :return: str formatted dollar amount
    """

    number = abs(number)
    number = "{:,.2f}".format(number)
    return f'${number}'
