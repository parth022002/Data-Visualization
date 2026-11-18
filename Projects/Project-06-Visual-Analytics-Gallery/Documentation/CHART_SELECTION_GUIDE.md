# Chart Selection Guide — Tableau 63 Charts Reference

## Decision Matrix: How to Choose the Right Visualization

| Business Goal | Recommended Chart Types | Anti-Patterns to Avoid |
| :--- | :--- | :--- |
| **Comparing Categories** | Horizontal Bar Chart, Column Bar, Lollipop Chart | 3D bar charts, pie charts with >4 slices |
| **Tracking Trends Over Time** | Line Chart, Area Chart, Sparklines | Bar charts with >50 chronological points |
| **Viewing Proportions of a Whole** | Treemap, 100% Stacked Bar, Waffle Chart | Multi-ring donut charts, excessive pies |
| **Evaluating Variable Correlations** | Scatter Plot with Trend Line, Bubble Chart | Dual-axis lines with non-zero misaligned scales |
| **Analyzing Frequency Distributions** | Histogram, Box & Whisker Plot | Bar charts masking internal variance |
| **Geographic Density & Spread** | Symbol / Bubble Map, Choropleth Map | Choropleths without population normalization |
| **Tracking Multi-Stage Conversions** | Funnel Chart, Waterfall Chart | Pie charts showing conversion loss |
| **Ranking Position Changes** | Bump Chart, Ranked Dumbbell Plot | Unsorted tables with raw ranking numbers |

---

## Tableau Order of Operations
Understanding the Tableau pipeline is critical for correct calculation outputs:

1. **Extract Filters**
2. **Data Source Filters**
3. **Context Filters**
4. **`FIXED` LOD Expressions & Sets**
5. **Dimension Filters**
6. **`INCLUDE` / `EXCLUDE` LOD Expressions**
7. **Measure Filters**
8. **Table Calculations (`RUNNING_SUM`, `WINDOW_AVG`)**
9. **Table Calculation Filters**
