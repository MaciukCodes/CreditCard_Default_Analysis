# Credit Card Default Analysis DataBase Schema

default_cc_clients
- raw_data
  - ID    INT
  - ~LIMIT_BAL    INT~
  - ~SEX    INT~
  - ~EDUCATION    INT~
  - ~MARRIAGE    INT~
  - ~AGE    INT~
  - PAY_0    INT
  - PAY_1    INT
  - PAY_2    INT
  - PAY_3    INT
  - PAY_4    INT
  - PAY_5    INT
  - PAY_6    INT
  - BILL_AMT1    INT
  - BILL_AMT2    INT
  - BILL_AMT3    INT
  - BILL_AMT4    INT
  - BILL_AMT5    INT
  - BILL_AMT6    INT
  - PAY_AMT1    INT
  - PAY_AMT2    INT
  - PAY_AMT3    INT
  - PAY_AMT4    INT
  - PAY_AMT5    INT
  - PAY_AMT6    INT
  - default_payment_next_month    INT

 - cardholder
   - cardholder_id INT PRIMARY KEY
   - sex TEXT CHECK IN ( 'Male', 'Female', 'Other', 'Prefer not to say')
   - education TEXT CHECK IN ( 'Graduate School', 'University', 'High School', 'Other')
   - marital_status TEXT CHECK IN( 'Married', 'Single', 'Other')
   - age INT
   - balance_limit INT

- monthly reports
  - statement_id INTEGER PRIMARY KEY
  - id INT FOREIGN KEY to cardholder
  - Month TEXT
  - Pay INT
  - Bill_amount INT
  - Pay_amount INT
