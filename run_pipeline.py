from scripts.process_sales import process_sales
from scripts.generate_report import generate_report


sales = process_sales()

report = generate_report(sales)

print(report)
print("Sales report generated successfully.")
