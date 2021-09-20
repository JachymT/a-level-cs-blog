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
A single table within a database. refered to as a single **relation** in a database

### Advantages
- Easier for small data sets, because it deals with **one entity**.
- All records are sotred in one place.
- Most often no specialist software is needed.

### Issues
- can ONLY deal with one entity
- high chance of data duplication - **DATA REDUNDANCY** - for example a teacher would need to add all thier data to all of thier students records
- this takes up a large amount of memory - inefficient in lots of ways
- security problems, very **vunerable** 
- anyone should not be able to see everything in a database
- difficult to update - for example ammending records if a lets say a class changes classrooms

## Relational database
A database using a structure tuple of tables in an ordered logic. Where links (relations) are formed between tables. Generally, each table/relation represents one "entity type" (such as customer or product). The record (rows) represent instances of that type of entity (such as "Lee" or "chair") and the fields (columns) represent values attributed to that instance (such as address or price).

### Advantages
- Relational database management systems (**RDMS**) are used to maintain the databases. This makes them more manigable.

### Issues
- RDMS is needed so the software must be compatible with the relational database

## Entity Relationship modeling
An entity relationship diagram explaining the one to many relationship between the dog owners and their dogs. Ignore the bottom arrow.

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
A compact way to print a query, shows data in an orginsed and presentable way. The image is a report made from the a query from the *Students* database.

<img src="https://raw.githubusercontent.com/JachymT/a-level-cs-blog/main/Computer%20Systems/1.3/1.3.2/images/Report.JPG" height="400">
