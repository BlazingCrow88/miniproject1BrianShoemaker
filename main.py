"""
INF601 - Advanced Programming in Python
Brian Shoemaker
Mini Project 1

This program collects stock data for 5 companies and creates visualizations
showing their closing prices over the last 10 trading days.
"""

import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
import os
from datetime import datetime, timedelta


def create_charts_folder():
    """Create charts folder if it doesn't exist"""
    if not os.path.exists('charts'):
        os.makedirs('charts')
        print("Created 'charts' folder")


def get_stock_data(ticker, period="10d"):
    """
    Get stock data for a given ticker
    Args:
        ticker (str): Stock ticker symbol
        period (str): Period to fetch data for
    Returns:
        list: List of closing prices
    """
    try:
        stock = yf.Ticker(ticker)
        hist = stock.history(period=period)

        if hist.empty:
            print(f"Warning: No data found for {ticker}")
            return []

        # Get closing prices and convert to list
        closing_prices = hist['Close'].tolist()
        return closing_prices[-10:]  # Ensure we get exactly 10 days

    except Exception as e:
        print(f"Error fetching data for {ticker}: {e}")
        return []


def create_stock_chart(ticker, prices, trading_days):
    """
    Create and save a chart for a stock
    Args:
        ticker (str): Stock ticker symbol
        prices (list): List of closing prices
        trading_days (list): List of trading day numbers
    """
    # Convert to NumPy array as required
    prices_array = np.array(prices)
    days_array = np.array(trading_days)

    # Create the plot
    plt.figure(figsize=(10, 6))
    plt.plot(days_array, prices_array, marker='o', linewidth=2, markersize=6)

    # Customize the chart
    plt.title(f'{ticker} - Closing Prices (Last 10 Trading Days)', fontsize=16, fontweight='bold')
    plt.xlabel('Trading Day', fontsize=12)
    plt.ylabel('Closing Price ($)', fontsize=12)
    plt.grid(True, alpha=0.3)

    # Add value labels on each point
    for i, price in enumerate(prices_array):
        plt.annotate(f'${price:.2f}', (days_array[i], price),
                     textcoords="offset points", xytext=(0, 10), ha='center', fontsize=9)

    # Format y-axis to show currency
    plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x:.2f}'))

    # Adjust layout and save
    plt.tight_layout()

    # Save to charts folder
    filename = f'charts/{ticker}_chart.png'
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    print(f"Saved chart: {filename}")

    # Close the figure to free memory
    plt.close()


def main():
    """Main function to execute the program"""
    print("Stock Market Data Visualization")
    print("=" * 40)

    # Create charts folder
    create_charts_folder()

    # Define 5 popular stock tickers - you can change these to your favorites
    tickers = ['AAPL', 'GOOGL', 'MSFT', 'TSLA', 'AMZN']

    print(f"\nFetching data for tickers: {', '.join(tickers)}")

    # Process each ticker
    for ticker in tickers:
        print(f"\nProcessing {ticker}...")

        # Get stock data
        closing_prices = get_stock_data(ticker)

        if not closing_prices:
            print(f"Skipping {ticker} due to data issues")
            continue

        # Ensure we have exactly 10 data points
        if len(closing_prices) < 10:
            print(f"Warning: Only {len(closing_prices)} data points available for {ticker}")

        # Create trading days list (1 through number of available days)
        trading_days = list(range(1, len(closing_prices) + 1))

        # Convert to NumPy arrays as required
        prices_array = np.array(closing_prices)

        print(f"Data for {ticker}:")
        print(f"  Days: {len(closing_prices)}")
        print(f"  Price range: ${np.min(prices_array):.2f} - ${np.max(prices_array):.2f}")
        print(f"  Average: ${np.mean(prices_array):.2f}")

        # Create and save chart
        create_stock_chart(ticker, closing_prices, trading_days)

    print("\n" + "=" * 40)
    print("All charts have been created and saved to the 'charts' folder!")
    print("Check the 'charts' directory for your PNG files.")


if __name__ == "__main__":
    main()