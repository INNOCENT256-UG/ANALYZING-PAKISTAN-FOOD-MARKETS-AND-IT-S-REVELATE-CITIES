"""
PK Foods Price Intelligence — Improved Chart Generation
Generates business-oriented visualizations with consistent color scheme
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from matplotlib.patches import FancyBboxPatch
import pandas as pd

# ============================================================================
# COLOR PALETTE
# ============================================================================

COLORS = {
    # Primary colors
    'emerald': '#059669',      # Highest performer
    'blue': '#2563EB',         # High performers
    'teal': '#0D9488',         # Mid-range
    'amber': '#F59E0B',        # Lower mid / warnings
    'red': '#DC2626',          # Lowest performer
    'purple': '#7C3AED',       # Premium categories
    'slate': '#64748B',        # Reference lines, gridlines
    
    # Theme colors (dark)
    'bg_dark': '#1E293B',
    'card_bg_dark': '#334155',
    'text_primary': '#F8FAFC',
    'text_secondary': '#94A3B8',
    
    # Category colors
    'premium': '#7C3AED',      # Beverages, Meat, Oil
    'mid': '#0D9488',          # Condiment, Dairy, Pulses
    'affordable': '#F59E0B'    # Fruit, Grain, Vegetable
}

# ============================================================================
# DATA
# ============================================================================

# Revenue by City data
CITY_DATA = {
    'Hyderabad': {'revenue': 1608801, 'share': 12.0, 'avg_price': 417.6},
    'Karachi': {'revenue': 1568588, 'share': 11.7, 'avg_price': 421.0},
    'Islamabad': {'revenue': 1460893, 'share': 10.9, 'avg_price': 343.8},
    'Quetta': {'revenue': 1459146, 'share': 10.9, 'avg_price': 399.7},
    'Faisalabad': {'revenue': 1382163, 'share': 10.3, 'avg_price': 347.9},
    'Rawalpindi': {'revenue': 1342984, 'share': 10.0, 'avg_price': 409.4},
    'Lahore': {'revenue': 1279284, 'share': 9.5, 'avg_price': 349.4},
    'Sialkot': {'revenue': 1174601, 'share': 8.8, 'avg_price': 368.8},
    'Multan': {'revenue': 1114521, 'share': 8.3, 'avg_price': 325.3},
    'Peshawar': {'revenue': 1032082, 'share': 7.7, 'avg_price': 338.3}
}

# Category data
CATEGORY_DATA = {
    'Beverage': {'avg_price': 911.6, 'max': 1185.1, 'min': 638.1, 'records': 48},
    'Meat': {'avg_price': 847.8, 'max': 1102.1, 'min': 593.5, 'records': 174},
    'Oil': {'avg_price': 721.7, 'max': 938.1, 'min': 505.2, 'records': 65},
    'Condiment': {'avg_price': 450.7, 'max': 585.9, 'min': 315.5, 'records': 62},
    'Dairy': {'avg_price': 413.8, 'max': 537.9, 'min': 289.7, 'records': 94},
    'Pulses': {'avg_price': 256.6, 'max': 333.5, 'min': 179.6, 'records': 102},
    'Fruit': {'avg_price': 185.6, 'max': 241.3, 'min': 129.9, 'records': 184},
    'Grain': {'avg_price': 141.9, 'max': 184.5, 'min': 99.3, 'records': 180},
    'Vegetable': {'avg_price': 94.9, 'max': 123.4, 'min': 66.5, 'records': 191}
}

# ============================================================================
# CHART 1: REVENUE BY CITY (Horizontal Bar Chart)
# ============================================================================

def create_revenue_by_city_chart():
    """Generate improved revenue by city chart"""
    
    # Sort cities by revenue (highest first)
    cities = sorted(CITY_DATA.keys(), key=lambda x: CITY_DATA[x]['revenue'], reverse=True)
    revenues = [CITY_DATA[city]['revenue'] / 1_000_000 for city in cities]  # Convert to millions
    shares = [CITY_DATA[city]['share'] for city in cities]
    
    # Color gradient based on ranking
    colors = [
        COLORS['emerald'],   # Hyderabad - highest
        COLORS['blue'],      # Karachi
        COLORS['blue'],      # Islamabad
        COLORS['blue'],      # Quetta
        COLORS['teal'],      # Faisalabad
        COLORS['teal'],      # Rawalpindi
        COLORS['teal'],      # Lahore
        COLORS['amber'],     # Sialkot
        COLORS['amber'],     # Multan
        COLORS['red']        # Peshawar - lowest
    ]
    
    # Create figure
    fig, ax = plt.subplots(figsize=(12, 7))
    fig.patch.set_facecolor(COLORS['bg_dark'])
    ax.set_facecolor(COLORS['bg_dark'])
    
    # Create horizontal bar chart
    bars = ax.barh(cities, revenues, color=colors, height=0.6, edgecolor='none')
    
    # Add data labels
    for i, (bar, revenue, share) in enumerate(zip(bars, revenues, shares)):
        width = bar.get_width()
        label = f'PKR {revenue:.1f}M ({share:.1f}%)'
        ax.text(width + 0.05, bar.get_y() + bar.get_height()/2, 
                label, va='center', ha='left', 
                color=COLORS['text_primary'], fontsize=10, weight='bold')
    
    # Add average reference line
    avg_revenue = sum(revenues) / len(revenues)
    ax.axvline(x=avg_revenue, color=COLORS['slate'], linestyle='--', 
               linewidth=2, alpha=0.7, label=f'Average: PKR {avg_revenue:.2f}M')
    ax.text(avg_revenue + 0.05, len(cities) - 0.5, 
            f'Average: PKR {avg_revenue:.2f}M', 
            va='top', ha='left', color=COLORS['slate'], fontsize=9, style='italic')
    
    # Styling
    ax.set_xlabel('Revenue (PKR Millions)', color=COLORS['text_primary'], 
                  fontsize=12, weight='bold')
    ax.set_ylabel('')
    ax.set_title('Total Revenue by City (PKR) — Hyderabad Leads at PKR 1.6M',
                 color=COLORS['text_primary'], fontsize=14, weight='bold', pad=20)
    
    # Gridlines
    ax.grid(axis='x', alpha=0.3, color=COLORS['slate'], linewidth=0.5)
    ax.set_axisbelow(True)
    
    # Remove spines
    for spine in ['top', 'right', 'left']:
        ax.spines[spine].set_visible(False)
    ax.spines['bottom'].set_color(COLORS['slate'])
    
    # Tick styling
    ax.tick_params(colors=COLORS['text_secondary'], labelsize=10)
    ax.set_xticks(np.arange(0, int(max(revenues)) + 1, 0.5))
    
    # Invert y-axis to show highest at top
    ax.invert_yaxis()
    
    plt.tight_layout()
    plt.savefig('Chart_Revenue_by_City_v2.png', dpi=300, bbox_inches='tight', 
                facecolor=COLORS['bg_dark'])
    plt.close()
    print("[OK] Generated: Chart_Revenue_by_City_v2.png")

# ============================================================================
# CHART 2: AVERAGE PRICE BY CATEGORY (Horizontal Bar Chart)
# ============================================================================

def create_price_by_category_chart():
    """Generate improved price by category chart"""
    
    # Sort categories by price (highest first)
    categories = sorted(CATEGORY_DATA.keys(), 
                       key=lambda x: CATEGORY_DATA[x]['avg_price'], reverse=True)
    prices = [CATEGORY_DATA[cat]['avg_price'] for cat in categories]
    records = [CATEGORY_DATA[cat]['records'] for cat in categories]
    
    # Color coding by price tier
    colors = []
    for cat in categories:
        if cat in ['Beverage', 'Meat', 'Oil']:
            colors.append(COLORS['purple'])      # Premium
        elif cat in ['Condiment', 'Dairy', 'Pulses']:
            colors.append(COLORS['teal'])        # Mid
        else:
            colors.append(COLORS['amber'])       # Affordable
    
    # Create figure
    fig, ax = plt.subplots(figsize=(12, 7))
    fig.patch.set_facecolor(COLORS['bg_dark'])
    ax.set_facecolor(COLORS['bg_dark'])
    
    # Create horizontal bar chart
    bars = ax.barh(categories, prices, color=colors, height=0.6, edgecolor='none')
    
    # Add data labels
    for bar, price, record in zip(bars, prices, records):
        width = bar.get_width()
        label = f'PKR {price:,.0f}/kg ({record} records)'
        ax.text(width + 20, bar.get_y() + bar.get_height()/2, 
                label, va='center', ha='left', 
                color=COLORS['text_primary'], fontsize=10, weight='bold')
    
    # Add average reference line
    avg_price = sum(prices) / len(prices)
    ax.axvline(x=avg_price, color=COLORS['slate'], linestyle='--', 
               linewidth=2, alpha=0.7, label=f'Overall Average: PKR {avg_price:.0f}/kg')
    ax.text(avg_price + 20, len(categories) - 0.5, 
            f'Overall Average: PKR {avg_price:.0f}/kg', 
            va='top', ha='left', color=COLORS['slate'], fontsize=9, style='italic')
    
    # Styling
    ax.set_xlabel('Average Price (PKR/kg)', color=COLORS['text_primary'], 
                  fontsize=12, weight='bold')
    ax.set_ylabel('')
    ax.set_title('Average Price per Kg by Category — Beverages Command Premium at PKR 912/kg',
                 color=COLORS['text_primary'], fontsize=14, weight='bold', pad=20)
    
    # Gridlines
    ax.grid(axis='x', alpha=0.3, color=COLORS['slate'], linewidth=0.5)
    ax.set_axisbelow(True)
    
    # Remove spines
    for spine in ['top', 'right', 'left']:
        ax.spines[spine].set_visible(False)
    ax.spines['bottom'].set_color(COLORS['slate'])
    
    # Tick styling
    ax.tick_params(colors=COLORS['text_secondary'], labelsize=10)
    
    # Invert y-axis to show highest at top
    ax.invert_yaxis()
    
    plt.tight_layout()
    plt.savefig('Chart_Price_by_Category_v2.png', dpi=300, bbox_inches='tight', 
                facecolor=COLORS['bg_dark'])
    plt.close()
    print("[OK] Generated: Chart_Price_by_Category_v2.png")

# ============================================================================
# CHART 3: KPI CARDS (Visual Representation)
# ============================================================================

def create_kpi_cards_visualization():
    """Generate a visual representation of the KPI card layout"""
    
    fig, ax = plt.subplots(figsize=(14, 6))
    fig.patch.set_facecolor(COLORS['bg_dark'])
    ax.set_facecolor(COLORS['bg_dark'])
    ax.axis('off')
    
    # KPI card data
    kpi_cards = [
        {'title': 'Total Revenue', 'value': 'PKR 13.4M', 'subtitle': '1,100 transactions',
         'color': COLORS['blue'], 'x': 0.05, 'width': 0.27, 'height': 0.85},
        {'title': 'Total Records', 'value': '1,100', 'subtitle': 'Transactions',
         'color': COLORS['teal'], 'x': 0.35, 'width': 0.18, 'height': 0.4},
        {'title': 'Avg Price/Kg', 'value': 'PKR 372', 'subtitle': 'National average',
         'color': COLORS['purple'], 'x': 0.56, 'width': 0.18, 'height': 0.4},
        {'title': 'Top Revenue City', 'value': 'Hyderabad', 'subtitle': 'PKR 1.6M (12.0%)',
         'color': COLORS['emerald'], 'x': 0.77, 'width': 0.18, 'height': 0.4},
        {'title': 'Most Expensive Item', 'value': 'Fish (Pomfret)', 'subtitle': 'PKR 1,113/kg',
         'color': COLORS['red'], 'x': 0.35, 'width': 0.18, 'height': 0.4, 'y_offset': 0.45},
        {'title': 'Items Above Average', 'value': '29.9%', 'subtitle': '330 of 1,100',
         'color': COLORS['amber'], 'x': 0.56, 'width': 0.18, 'height': 0.4, 'y_offset': 0.45}
    ]
    
    for card in kpi_cards:
        y_offset = card.get('y_offset', 0.05)
        
        # Card background
        rect = FancyBboxPatch((card['x'], y_offset), card['width'], card['height'],
                              boxstyle="round,pad=0.01,rounding_size=0.02",
                              facecolor=COLORS['card_bg_dark'],
                              edgecolor=card['color'], linewidth=3)
        ax.add_patch(rect)
        
        # Card text
        ax.text(card['x'] + card['width']/2, y_offset + card['height'] - 0.08,
                card['title'], ha='center', va='top',
                color=COLORS['text_secondary'], fontsize=10, weight='bold')
        ax.text(card['x'] + card['width']/2, y_offset + card['height']/2 + 0.05,
                card['value'], ha='center', va='center',
                color=COLORS['text_primary'], fontsize=16, weight='bold')
        ax.text(card['x'] + card['width']/2, y_offset + 0.08,
                card['subtitle'], ha='center', va='bottom',
                color=COLORS['text_secondary'], fontsize=9)
    
    ax.set_title('Key Performance Indicators', color=COLORS['text_primary'], 
                fontsize=16, weight='bold', pad=20)
    
    plt.tight_layout()
    plt.savefig('Chart_KPI_Cards_v2.png', dpi=300, bbox_inches='tight', 
                facecolor=COLORS['bg_dark'])
    plt.close()
    print("[OK] Generated: Chart_KPI_Cards_v2.png")

# ============================================================================
# CHART 4: PRICE VOLATILITY (Error Bar Chart)
# ============================================================================

def create_volatility_chart():
    """Generate price volatility chart showing min/max/avg ranges"""
    
    # Sort by volatility (range)
    categories = sorted(CATEGORY_DATA.keys(), 
                       key=lambda x: CATEGORY_DATA[x]['max'] - CATEGORY_DATA[x]['min'],
                       reverse=True)
    
    avg_prices = [CATEGORY_DATA[cat]['avg_price'] for cat in categories]
    min_prices = [CATEGORY_DATA[cat]['min'] for cat in categories]
    max_prices = [CATEGORY_DATA[cat]['max'] for cat in categories]
    ranges = [max_prices[i] - min_prices[i] for i in range(len(categories))]
    
    # Color by price tier
    colors = []
    for cat in categories:
        if cat in ['Beverage', 'Meat', 'Oil']:
            colors.append(COLORS['purple'])
        elif cat in ['Condiment', 'Dairy', 'Pulses']:
            colors.append(COLORS['teal'])
        else:
            colors.append(COLORS['amber'])
    
    # Create figure
    fig, ax = plt.subplots(figsize=(12, 7))
    fig.patch.set_facecolor(COLORS['bg_dark'])
    ax.set_facecolor(COLORS['bg_dark'])
    
    # Create error bar chart (horizontal)
    y_pos = np.arange(len(categories))
    ax.barh(y_pos, ranges, left=min_prices, color=colors, height=0.5, alpha=0.7)
    
    # Add average markers
    ax.scatter(avg_prices, y_pos, color=COLORS['blue'], s=100, zorder=5, 
               marker='D', edgecolors='white', linewidths=2)
    
    # Add range labels
    for i, (cat, range_val) in enumerate(zip(categories, ranges)):
        ax.text(max_prices[i] + 20, i, f'±{range_val:.0f}', 
                va='center', ha='left', color=COLORS['text_secondary'], fontsize=9)
    
    # Styling
    ax.set_yticks(y_pos)
    ax.set_yticklabels(categories, color=COLORS['text_primary'], fontsize=10)
    ax.set_xlabel('Price (PKR/kg)', color=COLORS['text_primary'], 
                  fontsize=12, weight='bold')
    ax.set_title('Price Volatility by Category — Pulses Show Highest Price Range (PKR 154)',
                 color=COLORS['text_primary'], fontsize=14, weight='bold', pad=20)
    
    # Gridlines
    ax.grid(axis='x', alpha=0.3, color=COLORS['slate'], linewidth=0.5)
    ax.set_axisbelow(True)
    
    # Remove spines
    for spine in ['top', 'right', 'left']:
        ax.spines[spine].set_visible(False)
    ax.spines['bottom'].set_color(COLORS['slate'])
    
    # Tick styling
    ax.tick_params(colors=COLORS['text_secondary'], labelsize=10)
    
    # Legend
    legend_elements = [
        mpatches.Patch(color=COLORS['purple'], label='Premium (>PKR 500/kg)'),
        mpatches.Patch(color=COLORS['teal'], label='Mid (PKR 200-500/kg)'),
        mpatches.Patch(color=COLORS['amber'], label='Affordable (<PKR 200/kg)'),
        plt.Line2D([0], [0], marker='D', color='w', markerfacecolor=COLORS['blue'],
                   markersize=10, label='Average Price')
    ]
    ax.legend(handles=legend_elements, loc='lower right', 
             facecolor=COLORS['card_bg_dark'], edgecolor=COLORS['slate'],
             labelcolor=COLORS['text_primary'], fontsize=9)
    
    ax.invert_yaxis()
    plt.tight_layout()
    plt.savefig('Chart_Price_Volatility_v2.png', dpi=300, bbox_inches='tight', 
                facecolor=COLORS['bg_dark'])
    plt.close()
    print("[OK] Generated: Chart_Price_Volatility_v2.png")

# ============================================================================
# CHART 5: REVENUE CONCENTRATION (Pareto Chart)
# ============================================================================

def create_pareto_chart():
    """Generate revenue concentration Pareto chart"""
    
    cities = list(CITY_DATA.keys())
    revenues = [CITY_DATA[city]['revenue'] for city in cities]
    total_revenue = sum(revenues)
    
    # Sort by revenue
    sorted_indices = np.argsort(revenues)[::-1]
    cities = [cities[i] for i in sorted_indices]
    revenues = [revenues[i] for i in sorted_indices]
    
    # Calculate cumulative percentage
    cumulative = np.cumsum(revenues) / total_revenue * 100
    
    # Create figure with dual axis
    fig, ax1 = plt.subplots(figsize=(12, 7))
    fig.patch.set_facecolor(COLORS['bg_dark'])
    ax1.set_facecolor(COLORS['bg_dark'])
    
    # Bar chart
    x_pos = np.arange(len(cities))
    bars = ax1.bar(x_pos, [r/1_000_000 for r in revenues], 
                   color=COLORS['blue'], alpha=0.8, width=0.6)
    
    # Cumulative line
    ax2 = ax1.twinx()
    ax2.plot(x_pos, cumulative, color=COLORS['emerald'], marker='o', 
             linewidth=3, markersize=8, label='Cumulative %')
    
    # 80% reference line
    ax2.axhline(y=80, color=COLORS['amber'], linestyle='--', 
                linewidth=2, alpha=0.7, label='80% Threshold')
    ax2.text(len(cities) - 1, 82, '80% Threshold', 
             va='bottom', ha='right', color=COLORS['amber'], fontsize=9)
    
    # Styling
    ax1.set_xlabel('City', color=COLORS['text_primary'], fontsize=12, weight='bold')
    ax1.set_ylabel('Revenue (PKR Millions)', color=COLORS['text_primary'], 
                   fontsize=12, weight='bold')
    ax2.set_ylabel('Cumulative %', color=COLORS['emerald'], fontsize=12, weight='bold')
    ax1.set_title('Revenue Concentration — Top 3 Cities Account for 33% of Total Revenue',
                  color=COLORS['text_primary'], fontsize=14, weight='bold', pad=20)
    
    # X-axis labels
    ax1.set_xticks(x_pos)
    ax1.set_xticklabels(cities, rotation=45, ha='right', 
                        color=COLORS['text_secondary'], fontsize=9)
    
    # Gridlines
    ax1.grid(axis='y', alpha=0.3, color=COLORS['slate'], linewidth=0.5)
    ax1.set_axisbelow(True)
    
    # Remove spines
    for spine in ['top', 'right']:
        ax1.spines[spine].set_visible(False)
    ax1.spines['left'].set_color(COLORS['slate'])
    ax1.spines['bottom'].set_color(COLORS['slate'])
    ax2.spines['top'].set_visible(False)
    
    # Tick styling
    ax1.tick_params(colors=COLORS['text_secondary'], labelsize=9)
    ax2.tick_params(colors=COLORS['emerald'], labelsize=9)
    
    # Legend
    ax2.legend(loc='center right', facecolor=COLORS['card_bg_dark'], 
              edgecolor=COLORS['slate'], labelcolor=COLORS['text_primary'], fontsize=9)
    
    plt.tight_layout()
    plt.savefig('Chart_Revenue_Concentration_v2.png', dpi=300, bbox_inches='tight', 
                facecolor=COLORS['bg_dark'])
    plt.close()
    print("[OK] Generated: Chart_Revenue_Concentration_v2.png")

# ============================================================================
# MAIN EXECUTION
# ============================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("PK Foods Price Intelligence — Chart Generation")
    print("=" * 60)
    print()
    
    print("Generating improved visualizations...")
    print()
    
    create_revenue_by_city_chart()
    create_price_by_category_chart()
    create_kpi_cards_visualization()
    create_volatility_chart()
    create_pareto_chart()
    
    print()
    print("=" * 60)
    print("[SUCCESS] All charts generated successfully!")
    print("=" * 60)
    print()
    print("Generated files:")
    print("  • Chart_Revenue_by_City_v2.png")
    print("  • Chart_Price_by_Category_v2.png")
    print("  • Chart_KPI_Cards_v2.png")
    print("  • Chart_Price_Volatility_v2.png")
    print("  • Chart_Revenue_Concentration_v2.png")
    print()
    print("Next steps:")
    print("  1. Review generated charts")
    print("  2. Update Excel dashboard with new chart specifications")
    print("  3. Replace screenshots in README.md")
    print("  4. Commit changes to repository")