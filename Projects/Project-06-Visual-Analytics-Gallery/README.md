# Visual Analytics & Calculation Architecture Reference

## Executive Summary
This reference repository serves as an architectural blueprint for modern Tableau development, featuring **15 specialized workbooks**, comprehensive implementations of modern calculation patterns (Level of Detail LOD expressions, Table Calculations, Parameter Actions, and Data Source relationships).

This catalog demonstrates how to model relational data, structure calculation pipelines, and format optimal visual representations for analytical questions.

---

## Comprehensive Workbook Architecture (15 Modular Workbooks)

| Workbook Name | Core Architectural Topics Demonstrated |
| :--- | :--- |
| `Data Sources.twbx` | Multi-table physical joins (Inner, Left, Right, Full), unions, live connection vs. hyper extract tradeoffs. |
| `Metadata.twbx` | Dimensional vs. Measure roles, Discrete vs. Continuous data types, geographic role assignments. |
| `Renaming.twbx` | Field aliasing, custom header formatting, data cleaning at the presentation metadata layer. |
| `Organizing Data.twbx` | Hierarchical drills, static & dynamic grouping, combined sets, set actions for asymmetric drilling. |
| `Filtering Data.twbx` | Tableau Order of Operations, Context Filters, Dimension vs. Measure filters, Top-N filtering. |
| `Parameters.twbx` | Dynamic metric swappers, reference lines, what-if scenario forecasting and sensitivity modeling. |
| `Actions.twbx` | Interactive filter actions, Go-To-Sheet cross-navigation, URL web page embedding, parameter actions. |
| `Aggregate Calculations.twbx` | Aggregation rules, `ATTR()`, disaggregating data, handling nulls with `ZN()`. |
| `LOD Expressions.twbx` | `FIXED` (cohort analysis), `INCLUDE` (finer grain), `EXCLUDE` (broader grain) calculations. |
| `Row Level Calculations.twbx` | String manipulation (`SPLIT`, `LEFT`, `TRIM`), Date math (`DATEDIFF`, `DATEADD`), Logical branching. |
| `Table Calculations.twbx` | `RUNNING_SUM`, `PERCENT_OF_TOTAL`, `RANK_UNIQUE`, Addressing vs. Partitioning rules. |
| `Multi-Measures.twbx` | Blended axes, synchronized dual-axes, measure names & values architectures. |
| `Visual-Analytics-Catalog.twbx` | Master visual calculation encyclopedia across core analytical categories. |
| `Dashboard.twbx` | Layout containers (tiled vs floating), inner/outer padding, responsive sizing modes, visual hierarchy. |
| `Sales & Customer Dashboards.twbx` | End-to-end commercial analytics capstone project with custom navigation menus. |

---

## Reference Datasets & Technical Documentation
- **Datasets:** Stored under `Data/raw/` (`small-dataset/` and `big-dataset/`), including `Customers.csv`, `Orders.csv`, `Products.csv`, `LOD.csv`, and `Product_prices.json`.
- **Architectural Documentation:** Stored under `Documentation/`:
  - `CHART_SELECTION_GUIDE.md`
  - `PROJECT_OVERVIEW.md`
  - `DATA_DICTIONARY.md`
