# Daily Notes rdb docker

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
-
