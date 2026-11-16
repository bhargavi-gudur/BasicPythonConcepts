"""
@file monthly_forecast.py
@brief Forecasts monthly electricity consumption and cost.
@date 16/11/2026
"""

def calculate_daily_average(previous_units, previous_days):
    """
    @brief Calculates average daily electricity consumption.
    @param previous_units Previous electricity usage in kWh.
    @param previous_days Number of days in the previous period.
    @return Average daily consumption in kWh.
    """
    return previous_units / previous_days


def forecast_units(daily_average, forecast_days):
    """
    @brief Forecasts electricity consumption.
    @param daily_average Average daily consumption in kWh.
    @param forecast_days Number of days in the forecast month.
    @return Forecast consumption in kWh.
    """
    return daily_average * forecast_days


# Main program
print("MONTHLY ELECTRICITY FORECAST CALCULATOR")

previous_units = float(
    input("Enter previous electricity units (kWh): ")
)
previous_days = int(input("Enter previous period days: "))
forecast_days = int(input("Enter forecast month days: "))
rate = float(input("Enter electricity rate per kWh (Rs.): "))

if (previous_units < 0 or previous_days <= 0 or
        forecast_days <= 0 or rate < 0):
    print("Invalid input.")
else:
    daily_average = calculate_daily_average(
        previous_units, previous_days
    )

    predicted_units = forecast_units(
        daily_average, forecast_days
    )

    estimated_bill = predicted_units * rate

    print(f"\nAverage Daily Consumption: {daily_average:.2f} kWh")
    print(f"Forecast Monthly Consumption: {predicted_units:.2f} kWh")
    print(f"Estimated Electricity Bill: Rs. {estimated_bill:.2f}")