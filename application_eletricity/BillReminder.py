"""
@file BillReminder.py
@brief Calculates electricity bills and checks payment due dates.
@date 06/11/2026
"""


def calculate_bill(units, rate):
    """
    @brief Calculate the electricity bill.
    @param units Electricity consumed in kWh.
    @param rate Cost per unit.
    @return Total bill amount.
    """
    return units * rate


def check_payment(due_date, payment_date):
    """
    @brief Check electricity bill payment status.
    @param due_date Bill due date.
    @param payment_date Actual payment date.
    @return Payment status.
    """
    if payment_date < due_date:
        return "Payment made before due date."
    elif payment_date == due_date:
        return "Payment made on due date."
    else:
        return "Payment made after due date."


def main():
    """Run the electricity bill reminder system."""

    print("===== ELECTRICITY BILL REMINDER =====")
    print("Date: 06/11/2026\n")

    try:
        units = float(input("Enter electricity units consumed: "))
        rate = float(input("Enter rate per unit (Rs.): "))
        due_date = int(input("Enter due date (day of month): "))
        payment_date = int(input("Enter payment date (day of month): "))

        if (units < 0 or rate < 0 or
                not 1 <= due_date <= 31 or
                not 1 <= payment_date <= 31):
            print("Invalid input!")
            return

        bill = calculate_bill(units, rate)

        print("\n===== BILL DETAILS =====")
        print(f"Units Consumed : {units:.2f} kWh")
        print(f"Total Bill     : Rs. {bill:.2f}")
        print("Status:", check_payment(due_date, payment_date))

    except ValueError:
        print("Please enter valid numeric values.")


if __name__ == "__main__":
    main()