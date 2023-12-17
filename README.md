# Website Traffic Analysis with SimilarWeb API

This Python script utilizes the SimilarWeb API to retrieve and analyze website traffic data for a list of specified websites. The collected data includes the total number of visits on a monthly basis over a specified date range.

## Prerequisites

Before using the script, make sure you have the following:

- **SimilarWeb API Key**: Replace `"Add_Your_API_KEY"` with your valid SimilarWeb API key.
- **Python Environment**: Ensure that you have Python installed on your machine.
- **Dependencies**: Install the required Python libraries using the following:
  ```bash
  pip install requests pandas xlsxwriter
## Script Configuration
- **Date Range**: Set the `start_date` and `end_date` variables to define the desired date range for the analysis.
- **Other Parameters**: Adjust optional parameters such as `country`, `granularity`, `main_domain_only`, `format_type` based on your requirements.
- **Show Verified Parameter (Optional)**: Set `show_verified` to `True` if you want to include only verified data. Default is `False`.
- **MTD Parameter (Optional)**: Set `mtd` to `True` if you want month-to-date data. Default is `False`.
- **Engaged Only Parameter (Optional)**: Set `engaged_only` to `True` if you want to include engaged users only. Default is `False`.

## Usage 
1. **Run the Script**: Execute the script, and it will prompt you to enter a list of websites separated by a new line.
2. **Output**: The script will generate a Pandas DataFrame containing the total visits data for each website. Additionally, it will save the data to an Excel file named `total_visits_data.xlsx`.

## Output Structure

The output Excel file consists of two sheets:

- **Data Sheet**: Contains the total visits data for each website over time.
- **Errors Sheet**: Lists websites for which data retrieval encountered errors.

## Notes

- Make sure to handle your SimilarWeb API key securely and avoid sharing it publicly.
- Review the [SimilarWeb API documentation](https://developer.similarweb.com/) for more details on available parameters and response formats.

Feel free to customize the script according to your specific needs or contribute to its improvement.

---

**Disclaimer**: Ensure compliance with SimilarWeb's terms of service and usage policies while using the API. This script is provided as-is, and the user assumes responsibility for its usage and any modifications made.

**Author**: @dlysh



