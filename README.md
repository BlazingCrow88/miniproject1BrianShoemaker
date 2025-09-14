### INF601 - Advanced Programming in Python
### [Your Name Here]
### Mini Project 1

# Stock Market Data Visualization

A Python program that fetches real-time stock data and creates visualization charts for 5 popular stocks, showing their closing prices over the last 10 trading days.

## Description

This project uses the Yahoo Finance API (yfinance) to collect closing price data for 5 stock tickers over the past 10 trading days. The data is stored in Python lists, converted to NumPy arrays, and then visualized using Matplotlib. Each stock gets its own individual chart saved as a PNG file in a dedicated charts folder. The program demonstrates data collection from APIs, data manipulation with NumPy, and data visualization with Matplotlib.

## Getting Started

### Dependencies

* Python 3.7 or higher
* Operating System: Windows, macOS, or Linux
* Internet connection (required for fetching stock data)
* Required Python packages (see requirements.txt):
  * numpy >= 1.24.0
  * matplotlib >= 3.7.0
  * yfinance >= 0.2.0

### Installing

1. Clone this repository or download the project files
```bash
git clone [your-repository-url]
cd [your-project-folder]
```

2. Install required packages using pip:
```bash
pip install -r requirements.txt
```

Alternatively, install packages individually:
```bash
pip install numpy matplotlib yfinance
```

### Executing program

1. Navigate to the project directory in your terminal/command prompt

2. Run the main program:
```bash
python main.py
```

3. The program will:
   * Create a 'charts' folder automatically
   * Fetch stock data for AAPL, GOOGL, MSFT, TSLA, and AMZN
   * Generate 5 individual PNG chart files
   * Save all charts in the 'charts' folder

4. Check the 'charts' folder for your generated PNG files after execution

## Help

Common issues and solutions:

**No data found for ticker**: This usually means the stock market is closed or there's a network issue.
```bash
# Ensure you have internet connection and try again
python main.py
```

**ModuleNotFoundError**: Install the required packages:
```bash
pip install -r requirements.txt
```

**Permission errors when creating charts folder**: Ensure you have write permissions in the project directory.

## Authors

Brian Shoemaker  

## Version History

* 1.0
    * Initial Release
    * Features: Stock data fetching, NumPy array conversion, Matplotlib visualization
    * Supports 5 stock tickers with 10-day historical data
    * Automatic chart generation and PNG export

## License

This project is licensed under the MIT License - see the LICENSE.md file for details

## Acknowledgments

* [yfinance](https://github.com/ranaroussi/yfinance) - Yahoo Finance API wrapper
* [NumPy](https://numpy.org/) - Numerical computing library
* [Matplotlib](https://matplotlib.org/) - Data visualization library
* [Yahoo Finance](https://finance.yahoo.com/) - Stock data source
* INF601 Course Materials and Examples