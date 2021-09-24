# Databases
## Keywords
<img src="https://raw.githubusercontent.com/JachymT/a-level-cs-blog/main/Computer%20Systems/1.3/1.3.2/images/database.JPG" height="200">

**Database** - A table makes a structured and organised database with data

**Information** - data with context

**Field** - a column in a database

**Entity** - information about something or someone that is being stored

**Record** - a row holds data for the entity

So fields store 1 piece of data for an entity and all of an entities data is stored in 1 row

**Validation**  - checks if an input is sensible, valid or in the right format
For example data types, dropdown lists (combo boxes) or field sizes

**Input mask** - a string of characters that indicates which inputs are valid - a format they need to follow. 
These are used in table fields and forms.

<img src="https://raw.githubusercontent.com/JachymT/a-level-cs-blog/main/Computer%20Systems/1.3/1.3.2/images/input-mask.JPG" height="400">

**Primary key** - unique identifier for each record. For example a student ID. Each databse will have atleast one column with a primary key.

## Flat file database
A single table within a database. refered to as a single **relation** in a database. Most often used for only 1 entity.

### Advantages
- Easier for small data sets, because it deals with **one entity**
- All records are sotred in one place - simple
- Most often no specialist software is needed
- Can be read and exported directly into a range of software, for example excel or a text file
- portable - easily share-able

### Issues
- high chance of data duplication - **DATA REDUNDANCY** - for example a teacher would need to add all of thier data to each students record. Causes issues with searching and sorting data
- this takes up a large amount of memory - **inefficient** in lots of ways becuase of data duplication
- requires new data everytime a new record is created
- difficult to update - for example ammending records if a lets say a class changes classrooms
- security problems, very **vunerable** - anyone should not be able to see everything in a database

## Relational database
A database using a structured tuple of tables in an ordered logic, where **links** (relations) are formed between tables. Generally, each table/relation represents one "entity type" (such as customers or products). The **records** (rows) represent instances of that type of entity (such as "Lee" or "chair") and the **fields** (columns) represent values attributed to that instance (such as address or price). Relational DBs contains the entity's **attributes and relationships**, look at the entity-relationship model for more information.

### Advantages
- Relational database management systems (**RDMS**) are used to maintain the databases. This makes them more manigable than flat file
- powerful, efficient and faster than flat file databases
- searching is faster because of more compex query support using SQL
- design of indexing makes seaching much faster as well
- Increased security of data - as user access levels can be changed and set (eg. teachers can only access students data and not other teachers)
- has **referential integrity** (data intergrity) - when changes are made to a specific field these changes are cascaded to any relation/table that also contain that field value

### Issues
- RDMS is needed so the **software must be compatibl**e with the relational database
- needs complex knowledge (eg. **normalisation and entity relational diagrams**)

## Entity Relationship modeling
An entity relationship diagram explaining the one to many relationship between the dog owners and their dogs. Ignore the arrow.

![image](https://user-images.githubusercontent.com/72783315/133996102-ac8798ef-8335-4721-8618-c00cb8496982.png)
![image](https://user-images.githubusercontent.com/72783315/133996616-58693ff7-24e2-4b16-9630-eef59b90461f.png)

*images from http://theteacher.info/index.php/computing-principles-01/1-3-exchanging-data/1-3-2-databases/2167-relational-databases-versus-flat-file-databases*

## Query 
The action of searching a database to retrieve a specific peice of data. A **complex query** has more than 1 search critera, often checking more than 1 field. Might be sorted by a primary key

<img src="https://raw.githubusercontent.com/JachymT/a-level-cs-blog/main/Computer%20Systems/1.3/1.3.2/images/query1.JPG" height="400">

## Forms
A simplified way to access a database entry, or add new entries. They make it clear which data is being presented. The image is an example of a form made on the *students database*.

<img src="https://raw.githubusercontent.com/JachymT/a-level-cs-blog/main/Computer%20Systems/1.3/1.3.2/images/Form.JPG" height="400">

## Reports
A compact way to print or **export** a query; shows data in an orginsed and presentable way. The image is a report made from the a query from the *Students* database.

<img src="https://raw.githubusercontent.com/JachymT/a-level-cs-blog/main/Computer%20Systems/1.3/1.3.2/images/Report.JPG" height="400">
