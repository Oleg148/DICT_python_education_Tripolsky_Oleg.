import argparse
import functions as fun

parser = argparse.ArgumentParser()
parser.add_argument("--type", help="type")
parser.add_argument("--principal", help="principal", type=int)
parser.add_argument("--periods", help="periods", type=int)
parser.add_argument("--interest", help="interest", type=float)
parser.add_argument("--payment", help="payment", type=float)
args = parser.parse_args()
ann_or_diff = args.type

if ann_or_diff == "annuity":
    if args.principal is not None and args.payment is not None and args.interest is not None and args.periods is None:
        n = fun.number_of_months(args.principal, args.payment, args.interest)
        fun.amount_of_time(n)
        print(f"Overpayment = {fun.overpayment(args.principal, args.payment, n)}!")
        print()

    elif args.principal is not None and args.periods is not None and args.interest is not None and args.payment is None:
        a = fun.annual_payment(args.principal, args.periods, args.interest)
        print("Your monthly payment =", fun.ceil(a), '!')
        print(f"Overpayment = {fun.overpayment(args.principal, a, args.periods)}!")
        print()

    elif args.payment is not None and args.periods is not None and args.interest is not None and args.principal is None:
        p = fun.principal_loan_amount(args.payment, args.periods, args.interest)
        print("Your loan principal =", p, '!')
        print(f"Overpayment = {fun.overpayment(p, args.payment, args.periods)}!")
        print()

    else:
        print("Incorrect parameters\n")

elif ann_or_diff == "diff":
    if args.principal is not None and args.periods is not None and args.interest is not None and args.payment is None:
        fun.diff(args.principal, args.periods, args.interest)
        a = fun.annual_payment(args.principal, args.periods, args.interest)
        print(f"Overpayment = {fun.overpayment(args.principal, a, args.periods)}!")
        print()

else:
    print("Incorrect parameters\n")
