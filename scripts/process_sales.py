import pandas as pd
import glob


def process_sales():
    files = glob.glob("incoming/*.csv")

    sales = pd.concat(
        [pd.read_csv(file) for file in files],
        ignore_index=True
    )

    sales["sales_amount"] = sales["units"] * sales["unit_price"]

    return sales
