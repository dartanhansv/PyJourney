import pandas as pd

# Create a DataFrame with the specified columns
# This will serve as the structure for the trading spreadsheet
df = pd.DataFrame(
    columns=[
        "Start Date",  # Start date of the trade
        "End Date",  # End date of the trade
        "Duration",  # Duration of the trade
        "Asset Code",  # Code of the traded asset
        "Strike",  # Strike price of the option (if applicable)
        "Expiration",  # Expiration date of the option (if applicable)
        "Quantity",  # Quantity of the asset traded
        "Initial Cost",  # Initial cost of the trade
        "Final Cost",  # Final cost of the trade
        "Financial Result",  # Financial result of the trade
        "Percentage Result",  # Percentage result of the trade
    ]
)

# Define the file path where the Excel file will be saved
file_path = "trade_log.xlsx"  # Save the file in the current working directory

# Save the DataFrame to an Excel file
df.to_excel(file_path, index=False)

# Output the file path for reference
file_path
