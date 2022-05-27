# Structured Query Language

## SQL from the Spec

`SELECT` - list of fields to be displayed

`FROM` - list the table or tables the data will come from

`JOIN … ON` - links fields in relational databases

`WHERE` - list of search criteria

`AND` - add aditional search criteria

`LIKE` - after a where, for queries `IN` - after a where, for queries

`(WILDCARDS)` - `* %` replace any amount of characters when querying,  `_ ?`replace a single character when querying

`ODER BY` - select a field to oder by, defualt is `ASC` but `DESC` can be specified after

`DELETE`

`INSERT`

`DROP`

`#dd/mm/yyyy#` - format for querying dates

## Writing

```
SELECT field1, field2
FROM database
WHERE field1 BETWEEN #dd/mm/yyyy# AND #dd/mm/yyyy#
ODER BY field1
```

### [not particluarly useful or comprehensive SQL learning site](https://sqlzoo.net/wiki/SQL_Tutorial)

### [sql worksheet complete with correct awsnsers - SQL from section B onwards](https://github.com/JachymT/a-level-cs-blog/blob/main/Computer%20Systems/1.3/1.3.2/Databases%20Worksheet.pdf)
