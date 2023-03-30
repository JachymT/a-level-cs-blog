# Structured Query Language

## SQL from the Spec

`AND` - add aditional search criteria

`LIKE` - after a where, for queries 

`IN` - after a where, for queries

`(WILDCARDS)` - `* %` replace any amount of characters when querying,  `_ ?`replace a single character when querying

`ODER BY` - select a field to oder by, defualt is `ASC` but `DESC` can be specified after

```SQL
SELECT fields FROM Table
```
fields to be displayed from Table

```SQL
FROM Table1
JOIN Table2 
ON 
Table1.PrimaryKey = Table2.ForeignKey
```
links fields in relational databases

```SQL
WHERE field = false
```
where should be followed by search criteria

```SQL
DELETE FROM Table
```
Deletes records that meet the condition set by a WHERE statement. If left blank deletes all records.

```SQL
INSERT INTO Table (column1, column2, ect)
VALUES (value1, value2, ect)
```
Inserts a new record into a table. value1 gets added to column1.

```SQL
UPDATE Table
SET Field = 'new value'
WHERE Field = 'condition'
```
Updates data contained records. Must be met by the where condition to be set.

```SQL
DROP TABLE Table
```
Deletes a table from the database and anything in it.

## Writing
`#dd/mm/yyyy` - format for querying dates

As a genral rule use '' for strings and nothing for numbers and dates

```SQL
SELECT date, type
FROM tblPlanted
WHERE date BETWEEN (#dd/mm/yyyy AND #dd/mm/yyyy)
AND type IN ('Pine','Spruce')
ODER BY date
```

### [not particluarly useful or comprehensive SQL learning site](https://sqlzoo.net/wiki/SQL_Tutorial)

### [sql worksheet complete with correct awsnsers - SQL from section B onwards](https://github.com/JachymT/a-level-cs-blog/blob/main/Computer%20Systems/1.3/1.3.2/Databases%20Worksheet.pdf)
