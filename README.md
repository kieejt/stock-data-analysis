# stock-data-analysis
## Project Description
This project leverages the yfinance API to collect, analyze, and visualize stock market data. It stores financial data in a PostgreSQL database, performs key financial analyses, and uses Power BI for creating interactive dashboards. The project is designed to help investors gain insights into stock performance through metrics such as trading volume, price trends, and total stock value.

### Project Structure

```
stock-data-analysis/
│
├── data/
│   ├── stocks_data.csv             # Collected stock data from yfinance
|   └── prices_data.py              
│
├── src/
│   ├── collect_data.py             # Script to fetch data from yfinance
│   └── insert_data.py              # Script to manage PostgreSQL data insertion
|
│
├── database/
│   ├── create_tables.sql           # SQL script for creating database tables
│
├── PowerBI/
│   └── Dashboards.pbix             # Power BI file containing dashboards
|   └── Dashboards.pdf              # PDF Dashboard
│
└── README.md                       
```

## Final Dashboard

[Dashboard](PowerBI/Dashboards.pdf)
