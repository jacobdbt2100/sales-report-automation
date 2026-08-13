import pandas as pd
from datetime import datetime


def generate_report(sales):

    total_sales = sales["sales_amount"].sum()
    total_units = sales["units"].sum()
    total_transactions = len(sales)

    report = pd.DataFrame({
        "metric": [
            "Total Sales",
            "Total Units Sold",
            "Total Transactions"
        ],
        "value": [
            total_sales,
            total_units,
            total_transactions
        ]
    })

    report_timestamp = datetime.now().strftime("%Y-%m-%d_%H%M%S")

    from pathlib import Path

    Path("reports").mkdir(exist_ok=True)

    report.to_csv(
        f"reports/sales_report_{report_timestamp}.csv",
        index=False
    )

    return report
