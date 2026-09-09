import json
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
from pathlib import Path

# Load the AMD data
with open('amd_data.json', 'r') as f:
    data = json.load(f)

# Create images directory if it doesn't exist
Path('images').mkdir(exist_ok=True)

# Extract facts
facts = data.get('facts', {})
us_gaap = facts.get('us-gaap', {})

# Function to extract time series data
def extract_time_series(metric_name):
    """Extract dates and values for a given metric"""
    metric = us_gaap.get(metric_name, {})
    units = metric.get('units', {})
    
    dates = []
    values = []
    
    for unit, entries in units.items():
        for entry in entries:
            if 'end' in entry and 'val' in entry:
                try:
                    date = datetime.strptime(entry['end'], '%Y-%m-%d')
                    dates.append(date)
                    values.append(entry['val'])
                except (ValueError, KeyError):
                    continue
    
    # Sort by date
    if dates and values:
        sorted_pairs = sorted(zip(dates, values))
        return [d for d, v in sorted_pairs], [v for d, v in sorted_pairs]
    return [], []

# Extract various metrics
shares_outstanding_dates, shares_outstanding = extract_time_series('EntityCommonStockSharesOutstanding')
revenue_dates, revenue = extract_time_series('Revenues')
net_income_dates, net_income = extract_time_series('NetIncomeLoss')
total_assets_dates, total_assets = extract_time_series('Assets')

# Create visualizations
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('AMD Financial Metrics Over Time', fontsize=16, fontweight='bold')

# Plot 1: Shares Outstanding
if shares_outstanding_dates and shares_outstanding:
    axes[0, 0].plot(shares_outstanding_dates, shares_outstanding, marker='o', color='blue', linewidth=2)
    axes[0, 0].set_title('Shares Outstanding Over Time')
    axes[0, 0].set_xlabel('Date')
    axes[0, 0].set_ylabel('Shares Outstanding')
    axes[0, 0].xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
    axes[0, 0].tick_params(axis='x', rotation=45)
    axes[0, 0].grid(True, alpha=0.3)

# Plot 2: Revenue
if revenue_dates and revenue:
    axes[0, 1].plot(revenue_dates, revenue, marker='s', color='green', linewidth=2)
    axes[0, 1].set_title('Revenue Over Time')
    axes[0, 1].set_xlabel('Date')
    axes[0, 1].set_ylabel('Revenue (USD)')
    axes[0, 1].xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
    axes[0, 1].tick_params(axis='x', rotation=45)
    axes[0, 1].grid(True, alpha=0.3)

# Plot 3: Net Income
if net_income_dates and net_income:
    axes[1, 0].plot(net_income_dates, net_income, marker='^', color='orange', linewidth=2)
    axes[1, 0].set_title('Net Income Over Time')
    axes[1, 0].set_xlabel('Date')
    axes[1, 0].set_ylabel('Net Income (USD)')
    axes[1, 0].xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
    axes[1, 0].tick_params(axis='x', rotation=45)
    axes[1, 0].grid(True, alpha=0.3)

# Plot 4: Total Assets
if total_assets_dates and total_assets:
    axes[1, 1].plot(total_assets_dates, total_assets, marker='d', color='red', linewidth=2)
    axes[1, 1].set_title('Total Assets Over Time')
    axes[1, 1].set_xlabel('Date')
    axes[1, 1].set_ylabel('Total Assets (USD)')
    axes[1, 1].xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
    axes[1, 1].tick_params(axis='x', rotation=45)
    axes[1, 1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('images/amd_metrics_dashboard.png', dpi=300, bbox_inches='tight')
print("Dashboard saved to images/amd_metrics_dashboard.png")

# Create individual high-resolution charts
if shares_outstanding_dates and shares_outstanding:
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(shares_outstanding_dates, shares_outstanding, marker='o', color='blue', linewidth=2, markersize=6)
    ax.set_title('AMD Shares Outstanding Over Time', fontsize=14, fontweight='bold')
    ax.set_xlabel('Date', fontsize=12)
    ax.set_ylabel('Shares Outstanding', fontsize=12)
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
    plt.xticks(rotation=45)
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('images/shares_outstanding.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("Shares outstanding chart saved to images/shares_outstanding.png")

if revenue_dates and revenue:
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(revenue_dates, revenue, marker='s', color='green', linewidth=2, markersize=6)
    ax.set_title('AMD Revenue Over Time', fontsize=14, fontweight='bold')
    ax.set_xlabel('Date', fontsize=12)
    ax.set_ylabel('Revenue (USD)', fontsize=12)
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
    plt.xticks(rotation=45)
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('images/revenue.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("Revenue chart saved to images/revenue.png")

if net_income_dates and net_income:
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(net_income_dates, net_income, marker='^', color='orange', linewidth=2, markersize=6)
    ax.set_title('AMD Net Income Over Time', fontsize=14, fontweight='bold')
    ax.set_xlabel('Date', fontsize=12)
    ax.set_ylabel('Net Income (USD)', fontsize=12)
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
    plt.xticks(rotation=45)
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('images/net_income.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("Net income chart saved to images/net_income.png")

if total_assets_dates and total_assets:
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(total_assets_dates, total_assets, marker='d', color='red', linewidth=2, markersize=6)
    ax.set_title('AMD Total Assets Over Time', fontsize=14, fontweight='bold')
    ax.set_xlabel('Date', fontsize=12)
    ax.set_ylabel('Total Assets (USD)', fontsize=12)
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
    plt.xticks(rotation=45)
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('images/total_assets.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("Total assets chart saved to images/total_assets.png")

print("\nAll visualizations completed!")
