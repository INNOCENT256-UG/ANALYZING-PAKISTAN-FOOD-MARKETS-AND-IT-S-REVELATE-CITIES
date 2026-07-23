# Visualization Style Guide — PK Foods Price Intelligence

## Color Palette

### Primary Data Colors
```python
# High performers / Premium values
BLUE_PRIMARY = '#2563EB'      # Deep blue for high revenue, high prices
TEAL_SECONDARY = '#0D9488'    # Teal for mid-range values
RED_ACCENT = '#DC2626'        # Red for low performers, warnings

# Accent Colors
EMERALD_HIGHLIGHT = '#059669' # Green for highest performer (Hyderabad)
AMBER_WARNING = '#D97706'     # Orange for lowest performer (Peshawar)
SLATE_REFERENCE = '#64748B'   # Gray for average/reference lines
```

### Dashboard Theme Colors
```python
# Dark Theme (Current)
BACKGROUND_DARK = '#1E293B'   # Dark slate background
CARD_BG_DARK = '#334155'      # Slightly lighter for cards
TEXT_PRIMARY = '#F8FAFC'      # White/light gray for primary text
TEXT_SECONDARY = '#94A3B8'    # Muted gray for secondary text

# Light Theme (Alternative)
BACKGROUND_LIGHT = '#FFFFFF'  # Pure white
CARD_BG_LIGHT = '#F1F5F9'     # Light gray for cards
TEXT_PRIMARY_LIGHT = '#0F172A' # Dark slate for primary text
TEXT_SECONDARY_LIGHT = '#64748B' # Medium gray for secondary text
```

### Category Color Coding (Price-Based)
```python
# High-price categories (>PKR 500/kg)
CATEGORY_PREMIUM = '#7C3AED'  # Purple for Beverages, Meat, Oil

# Mid-price categories (PKR 200-500/kg)
CATEGORY_MID = '#0D9488'      # Teal for Condiment, Dairy, Pulses

# Low-price categories (<PKR 200/kg)
CATEGORY_AFFORDABLE = '#F59E0B' # Amber for Fruit, Grain, Vegetable
```

## Typography Standards

### Font Specifications
```python
FONT_FAMILY = 'Segoe UI'      # Primary font (Windows/Excel default)
FONT_FAMILY_ALT = 'Helvetica' # Alternative for cross-platform

# Size Hierarchy
TITLE_SIZE = 24                # Dashboard title
SECTION_HEADER = 14            # Section headers
BODY_TEXT = 11                 # General text and labels
DATA_LABELS = 10               # Chart data labels
FOOTNOTES = 9                  # Source notes, timestamps
```

### Number Formatting
```python
# Currency Format
CURRENCY_FORMAT = 'PKR #,##0'           # Full values: PKR 1,608,801
CURRENCY_SHORT = 'PKR #.#M'             # Millions: PKR 1.6M
CURRENCY_KG = 'PKR #,##0/kg'            # Per kg: PKR 372/kg

# Percentage Format
PERCENTAGE_FORMAT = '#.0%'              # 12.0%
PERCENTAGE_ONE_DECIMAL = '#.0%'         # Consistent 1 decimal

# Decimal Places
DECIMAL_2 = '#,##0.00'                  # 417.60
DECIMAL_1 = '#,##0.0'                   # 417.6
DECIMAL_0 = '#,##0'                     # 418
```

## Chart Specifications

### Chart 1: Revenue by City (Horizontal Bar Chart)

**Business Question:** Which cities generate the most revenue?

**Chart Type:** Horizontal bar chart, sorted descending

**Title:** "Total Revenue by City (PKR) — Hyderabad Leads at PKR 1.6M"

**Color Scheme:**
```python
# Gradient from highest to lowest
colors = [
    '#059669',  # Emerald (Hyderabad - highest)
    '#2563EB',  # Blue (Karachi, Islamabad, Quetta - top tier)
    '#0D9488',  # Teal (Faisalabad, Rawalpindi, Lahore - mid tier)
    '#F59E0B',  # Amber (Sialkot, Multan - lower mid)
    '#DC2626',  # Red (Peshawar - lowest)
]
```

**Axis Formatting:**
- Y-axis: City names, sorted by revenue (highest at top)
- X-axis: "Revenue (PKR Millions)" with format 0.0M
- Gridlines: Horizontal only, 30% opacity, color #64748B

**Data Labels:**
- Show value at end of each bar: "PKR 1.6M"
- Show percentage in parentheses: "(12.0%)"
- Font: Segoe UI, 10pt, color #F8FAFC

**Reference Lines:**
- Average revenue line at PKR 1.34M (color: #64748B, dashed)
- Label: "Average: PKR 1.34M"

**Spacing:**
- Chart area padding: 20px
- Bar height: 80% of available space
- Gap between bars: 10px

---

### Chart 2: Average Price by Category (Horizontal Bar Chart)

**Business Question:** Which food categories are most expensive?

**Chart Type:** Horizontal bar chart, sorted descending

**Title:** "Average Price per Kg by Category — Beverages Command Premium at PKR 912/kg"

**Color Scheme:**
```python
# Three-tier color coding
colors = {
    'Beverage': '#7C3AED',      # Purple - Premium
    'Meat': '#7C3AED',          # Purple - Premium
    'Oil': '#7C3AED',           # Purple - Premium
    'Condiment': '#0D9488',     # Teal - Mid
    'Dairy': '#0D9488',         # Teal - Mid
    'Pulses': '#0D9488',        # Teal - Mid
    'Fruit': '#F59E0B',         # Amber - Affordable
    'Grain': '#F59E0B',         # Amber - Affordable
    'Vegetable': '#F59E0B',     # Amber - Affordable
}
```

**Axis Formatting:**
- Y-axis: Category names, sorted by price (highest at top)
- X-axis: "Average Price (PKR/kg)" with format #,##0
- Gridlines: Vertical only, 30% opacity

**Data Labels:**
- Show price at end of bar: "PKR 912/kg"
- Show record count: "(48 records)"
- Font: Segoe UI, 10pt

**Reference Lines:**
- Overall average line at PKR 372/kg (color: #64748B, dashed)
- Label: "Overall Average: PKR 372/kg"

**Alternative: If Keeping Pie Chart**
- Use donut style with center text: "Avg: PKR 372/kg"
- Limit to top 5 categories, group rest as "Other"
- Order: Largest slice at top, clockwise
- Colors: Purple → Teal → Amber gradient

---

### Chart 3: KPI Cards

**Layout:** 3x2 grid (6 cards total)

**Card Specifications:**

#### Primary Card (Top Left - Largest)
```python
{
    'title': 'Total Revenue',
    'value': 'PKR 13.4M',
    'subtitle': '1,100 transactions',
    'icon': '💰',
    'color': '#2563EB',  # Blue
    'size': 'large'      # 2x width
}
```

#### Secondary Cards (Top Row)
```python
{
    'title': 'Total Records',
    'value': '1,100',
    'subtitle': 'Transactions',
    'icon': '📋',
    'color': '#0D9488',  # Teal
    'size': 'medium'
},
{
    'title': 'Avg Price/Kg',
    'value': 'PKR 372',
    'subtitle': 'National average',
    'icon': '⚖️',
    'color': '#7C3AED',  # Purple
    'size': 'medium'
}
```

#### Tertiary Cards (Bottom Row)
```python
{
    'title': 'Top Revenue City',
    'value': 'Hyderabad',
    'subtitle': 'PKR 1.6M (12.0%)',
    'icon': '🏆',
    'color': '#059669',  # Emerald
    'size': 'small'
},
{
    'title': 'Most Expensive Item',
    'value': 'Fish (Pomfret)',
    'subtitle': 'PKR 1,113/kg',
    'icon': '🐟',
    'color': '#DC2626',  # Red
    'size': 'small'
},
{
    'title': 'Items Above Average',
    'value': '29.9%',
    'subtitle': '330 of 1,100',
    'icon': '📊',
    'color': '#F59E0B',  # Amber
    'size': 'small'
}
```

**Card Design:**
- Background: #334155 (dark) or #F1F5F9 (light)
- Border radius: 8px
- Padding: 20px internal
- Shadow: Subtle drop shadow for depth
- Font: Title (11pt, #94A3B8), Value (18pt bold, #F8FAFC), Subtitle (10pt, #64748B)

**Spacing:**
- Gap between cards: 20px
- Align to 3-column grid
- Equal card heights within each row

---

### Chart 4: Price Volatility by Category (Error Bar Chart)

**Business Question:** Which categories have the most price instability?

**Chart Type:** Horizontal error bar chart showing Min, Max, and Average

**Title:** "Price Volatility by Category — Pulses Show Highest Price Range (PKR 154)"

**Color Scheme:**
```python
# Error bars in slate gray
error_bar_color = '#64748B'

# Average marker in blue
average_marker_color = '#2563EB'

# Category bars colored by price tier (same as Chart 2)
```

**Axis Formatting:**
- Y-axis: Category names
- X-axis: "Price Range (PKR/kg)"
- Gridlines: Vertical only, light

**Data Representation:**
- Horizontal line: Min to Max range
- Vertical marker: Average price
- Label: Show range value: "PKR 154 range"

---

### Chart 5: Price Gap Analysis (Diverging Bar Chart)

**Business Question:** How much do prices vary between cities for each item?

**Chart Type:** Diverging bar chart centered on national average

**Title:** "Price Gap Analysis — Fish (Pomfret) Shows PKR 400+ Gap Between Cities"

**Color Scheme:**
```python
# Below average: Blue
below_avg_color = '#2563EB'

# Above average: Red/Orange
above_avg_color = '#DC2626'

# Center line: Gray
center_line_color = '#64748B'
```

**Axis Formatting:**
- Y-axis: Top 10 items by price gap
- X-axis: Diverging from center (national average)
- Center line at PKR 0 (national average)

---

### Chart 6: Revenue Concentration (Pareto Chart)

**Business Question:** What percentage of revenue comes from top cities?

**Chart Type:** Combo chart (bar + line)

**Title:** "Revenue Concentration — Top 3 Cities Account for 33% of Total Revenue"

**Color Scheme:**
```python
# Bars: Blue gradient
bar_color = '#2563EB'

# Cumulative line: Emerald
line_color = '#059669'

# 80% reference line: Amber
reference_line_color = '#F59E0B'
```

**Axis Formatting:**
- Primary Y-axis (left): "Revenue (PKR Millions)"
- Secondary Y-axis (right): "Cumulative %"
- X-axis: Cities sorted by revenue

**Data Labels:**
- Bars: Show revenue value
- Line: Show cumulative percentage at each point

---

## Implementation Checklist

### Excel Implementation

#### Chart 1: Revenue by City
- [ ] Convert to horizontal bar chart
- [ ] Sort cities by revenue (descending)
- [ ] Apply color gradient (emerald → blue → teal → amber → red)
- [ ] Add data labels: "PKR 1.6M (12.0%)"
- [ ] Add average reference line at PKR 1.34M
- [ ] Format X-axis as "PKR (Millions)"
- [ ] Reduce gridline opacity to 30%
- [ ] Update title to business-oriented version

#### Chart 2: Average Price by Category
- [ ] Convert pie chart to horizontal bar chart
- [ ] Sort categories by price (descending)
- [ ] Apply three-tier color coding (purple/teal/amber)
- [ ] Add data labels: "PKR 912/kg (48 records)"
- [ ] Add average reference line at PKR 372/kg
- [ ] Format X-axis as "PKR/kg"
- [ ] Update title to business-oriented version

#### KPI Cards
- [ ] Reorganize into 3x2 grid
- [ ] Apply size hierarchy (large → medium → small)
- [ ] Use consistent card design (background, padding, shadow)
- [ ] Apply color coding by metric type
- [ ] Ensure equal spacing (20px gap)
- [ ] Align to grid system

#### Additional Charts
- [ ] Create Price Volatility error bar chart
- [ ] Create Price Gap diverging bar chart
- [ ] Create Revenue Concentration Pareto chart
- [ ] Apply consistent color palette
- [ ] Add business-oriented titles
- [ ] Format all axes consistently

### Python Implementation (Alternative)

If regenerating charts with Python:

```python
# Required libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set style
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")

# Color palette
colors = {
    'emerald': '#059669',
    'blue': '#2563EB',
    'teal': '#0D9488',
    'amber': '#F59E0B',
    'red': '#DC2626',
    'purple': '#7C3AED',
    'slate': '#64748B'
}
```

## Accessibility Standards

### Contrast Ratios (WCAG AA)
- Normal text: Minimum 4.5:1 contrast ratio
- Large text (18pt+): Minimum 3:1 contrast ratio
- Charts: Test in grayscale to ensure readability

### Color Blindness
- Use patterns/symbols in addition to color
- Avoid red/green combinations as sole differentiator
- Test with color blindness simulator

### Print-Friendly
- Ensure charts readable in grayscale
- Use patterns/hatching for chart elements
- Include data labels (don't rely on color alone)

## File Naming Convention

```
Pk_Food_project_dashboard_v2.png      # Updated main dashboard
Chart_Revenue_by_City.png             # Individual chart exports
Chart_Price_by_Category.png
Chart_Price_Volatility.png
Chart_Price_Gap_Analysis.png
Chart_Revenue_Concentration.png
```

## Version Control

- Version: 2.0
- Date: 2025
- Changes: Improved color scheme, chart types, and business-oriented titles
- Previous: 1.0 (original dashboard)

---

*Style guide created: 2025 | Based on dashboard review and data visualization best practices*