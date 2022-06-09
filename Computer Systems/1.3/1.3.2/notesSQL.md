# Structured Query Language

## SQL from the Spec

`SELECT fields FROM Table` - fields to be displayed from Table

`JOIN Table1 ON Table1.primary key = Table2.foreign key` - links fields in relational databases

<img width="720" alt="craigndave SQL" src="https://user-images.githubusercontent.com/72783315/172877603-924631e4-cccd-4ce7-a6b0-78af3ce11a14.png">

`WHERE` - list of search criteria

`AND` - add aditional search criteria

`LIKE` - after a where, for queries 

`IN` - after a where, for queries

`(WILDCARDS)` - `* %` replace any amount of characters when querying,  `_ ?`replace a single character when querying

`ODER BY` - select a field to oder by, defualt is `ASC` but `DESC` can be specified after

`DELETE FROM Table` Deletes records specified by WHERE statement, or deletes all records

```
INSERT INTO Table
Values(field1, filed2 ...)
```
Inserts a new row into a table.

`DROP TABLE Table` Deletes the whole table and anything 

`#dd/mm/yyyy` - format for querying dates

As a genral rule use '' for strings and nothing for numbers and dates

## Writing

```
SELECT date, type
FROM tblPlanted
WHERE date BETWEEN (#dd/mm/yyyy AND #dd/mm/yyyy)
AND type IN ('Pine','Spruce')
ODER BY date
```

### [not particluarly useful or comprehensive SQL learning site](https://sqlzoo.net/wiki/SQL_Tutorial)

### [sql worksheet complete with correct awsnsers - SQL from section B onwards](https://github.com/JachymT/a-level-cs-blog/blob/main/Computer%20Systems/1.3/1.3.2/Databases%20Worksheet.pdf)
