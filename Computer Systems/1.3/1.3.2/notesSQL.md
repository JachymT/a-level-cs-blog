# Structured Query Language

## SQL from the Spec

select a field to oder by, defualt is `ASC` but `DESC` can be specified after
```SQL
ODER BY
```

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

where should be followed by search criteria, always use single equals sign
```SQL
WHERE field = false
```

in used same as python, can replace using lots of `AND`s
```SQL
WHERE field IN [1,2]
```

LIKE is used for wildcards. `*` and  `%` replace any amount of characters, `_` and `?`replace a single character when querying.
```SQL
WHERE field LIKE 'S%'
```

Deletes records that meet the condition set by a WHERE statement. If left blank deletes all records.
```SQL
DELETE FROM Table
```

Inserts a new record into a table. value1 gets added to column1.
```SQL
INSERT INTO Table (column1, column2, ect)
VALUES (value1, value2, ect)
```

Updates data contained records. Must be met by the where condition to be set.
```SQL
UPDATE Table
SET Field = 'new value'
WHERE Field = 'condition'
```

Deletes a table from the database and anything in it.
```SQL
DROP TABLE Table
```

not in spec 
```SQL
CREATE TABLE Table (
  id INTEGER PRIMARY KEY,
  customer_id INTEGER,
  product TEXT,
  quantity INTEGER
)
```

## Writing
`#dd/mm/yyyy` - format for querying dates

As a genral rule use '' for strings and nothing for numbers and dates

```SQL
SELECT date, type
FROM tblPlanted
WHERE date BETWEEN (#dd/mm/yyyy AND #dd/mm/yyyy)
AND type IN ('Pine','Spruce')
ODER BY date ASC
```

### [not particluarly useful or comprehensive SQL learning site](https://sqlzoo.net/wiki/SQL_Tutorial)

### [sql worksheet complete with correct awsnsers - SQL from section B onwards](https://github.com/JachymT/a-level-cs-blog/blob/main/Computer%20Systems/1.3/1.3.2/Databases%20Worksheet.pdf)
