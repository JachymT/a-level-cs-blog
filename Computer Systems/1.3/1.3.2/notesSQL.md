# Structured Query Language

## SQL from the Spec

fields to be displayed from Table
```SQL
SELECT fields FROM Table
```

links fields in relational databases
```SQL
FROM Table1
JOIN Table2 
ON 
Table1.PrimaryKey = Table2.ForeignKey
```

followed by search criteria
```SQL
WHERE field = false
```

`AND` - add aditional search criteria

`LIKE` - after a where, for queries 

`IN` - after a where, for queries

`(WILDCARDS)` - `* %` replace any amount of characters when querying,  `_ ?`replace a single character when querying

`ODER BY` - select a field to oder by, defualt is `ASC` but `DESC` can be specified after

`DELETE FROM Table` Deletes records that meet the condition set by a WHERE statement. If left blank deletes all records.

```SQL
INSERT INTO Table (column1, column2, ect)
VALUES (value1, value2, ect)
```
Inserts a new record into a table. value1 gets added to column1.

`DROP TABLE Table` Deletes the whole table and anything in it

`#dd/mm/yyyy` - format for querying dates

As a genral rule use '' for strings and nothing for numbers and dates

## Writing

```SQL
SELECT date, type
FROM tblPlanted
WHERE date BETWEEN (#dd/mm/yyyy AND #dd/mm/yyyy)
AND type IN ('Pine','Spruce')
ODER BY date
```

### [not particluarly useful or comprehensive SQL learning site](https://sqlzoo.net/wiki/SQL_Tutorial)

### [sql worksheet complete with correct awsnsers - SQL from section B onwards](https://github.com/JachymT/a-level-cs-blog/blob/main/Computer%20Systems/1.3/1.3.2/Databases%20Worksheet.pdf)
