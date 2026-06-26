CREATE TABLE dim_fund (
    fund_id INTEGER PRIMARY KEY,
    fund_name TEXT
);

CREATE TABLE dim_date (
    date_id INTEGER PRIMARY KEY,
    date DATE
);

CREATE TABLE fact_nav (
    nav_id INTEGER PRIMARY KEY,
    fund_id INTEGER,
    date_id INTEGER,
    nav REAL
);

CREATE TABLE fact_transactions (
    transaction_id INTEGER PRIMARY KEY,
    fund_id INTEGER,
    amount REAL,
    transaction_type TEXT
);

CREATE TABLE fact_performance (
    performance_id INTEGER PRIMARY KEY,
    fund_id INTEGER,
    return_1y REAL,
    return_3y REAL,
    expense_ratio REAL
);

CREATE TABLE fact_aum (
    aum_id INTEGER PRIMARY KEY,
    fund_id INTEGER,
    aum REAL
);