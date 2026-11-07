# Daily Notes Credit Card Default Analysis

### 2026-10-30
- Got raw data converted from a zip file to excel to DataFrame to SQL after exploring it the minimum amount 
- Started queries create tables but recalled that since all the values came in as integers looked to see if there was additional info so I can convert some of the values to integers probably best to convert them first so I can b sure to have the right datatype when making the new tables
### 2026-11-01
- got 3 more custom functions going:
  - base sql query just select , from and where to it 
  - got a case create function able to make multiple when statements
  - and made a table insert function fairly basic but from my understanding on how sql lite works it gets its uses.
 - need to get doc strings written better on them however did enough for me to fully create them but there is probably more to add 
   - actually finished them after I wrote that :P
 - tested in both sqlite's method of inspection as well as pandas + sqlalchemy  
    table was passed properly and appears as intended
- still should research between sql and pandas for the data transform but I think SQL is in the lead  with its ease into window functions


### 2026-11-03
- Had the README started previously but cleaned it up and made sure it all worked
- decided to move credit limit from the monthly_reports table to the cardholder table since its based on the cardholder only and not the month (at least here its not) 

### 2026-11-05
- Both tables are imported and working in the sql database
- need to either create a new table for payment history record(?) or add it to a current table

### 2026-11-06
- started moving files around and making sure connections still work encountered and issue with the notebook holding the old file location still had to close and restart to fix
- 
