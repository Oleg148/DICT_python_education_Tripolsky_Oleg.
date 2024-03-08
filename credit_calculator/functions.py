from math import ceil, log


def nominal_interest_rate(loan_interest):
    return loan_interest / (12 * 100)


def number_of_months(loan_principal, monthly_payment, loan_interest):
    i = nominal_interest_rate(loan_interest)
    return ceil(log(float(monthly_payment) / (float(monthly_payment) - i * float(loan_principal)), 1 + i))


def amount_of_time(months):
    if months % 12 == 0:
        print("It will take", int(months / 12), "years to repay this loan!")

    elif months / 12 < 1:
        print("It will take", int(months % 12), "months to repay this loan!")

    else:
        print(months // 12, "years", "and", months % 12, "months to repay this loan!")


def annual_payment(loan_principal, number_of_periods, loan_interest):
    i = nominal_interest_rate(loan_interest)
    j = (1 + i) ** number_of_periods
    return loan_principal * ((i * j) / (j - 1))


def principal_loan_amount(monthly_payment, number_of_periods, loan_interest):
    i = nominal_interest_rate(loan_interest)
    j = (1 + i) ** number_of_periods
    return int(monthly_payment / ((i * j) / (j - 1)))


def diff(loan_principal, number_of_periods, loan_interest):
    i = nominal_interest_rate(loan_interest)
    for m in range(1, number_of_periods + 1):
        print(f"Month {m}: payment is", end=" ")
        print(ceil((loan_principal / number_of_periods) + i * (loan_principal - ((loan_principal * (m - 1)) /
                                                                                 number_of_periods))))


def overpayment(loan_principal, monthly_payment, number_of_periods):
    return (ceil(monthly_payment) * ceil(number_of_periods)) - loan_principal
