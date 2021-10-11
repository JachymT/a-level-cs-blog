# Databases
## Keywords
<img src="https://raw.githubusercontent.com/JachymT/a-level-cs-blog/main/Computer%20Systems/1.3/1.3.2/images/database.JPG" height="200">

**Database** - A table makes a structured and organised database with data

**Information** - data with context

**Field** - a column in a database

**Entity** - a catergory of things, people or events of interest about which data is being held. A person is an instance of an entity.

**Record** - a row holds data for the entity

**Validation**  - checks if an input is sensible, valid or in the right format
For example data types, dropdown lists (combo boxes) or field sizes

**Primary key** - unique identifier for each record. For example a student ID. Each databse will have atleast one column with a primary key. A primary key cannot be repeated as another primary key again.

**Candidate key** - all keys that qualify as primary keys

**Secondary key** - An alternative key is a key not selected to be a primary key. It can be used to query for data in addition to the primary key. All candidate keys which are not primary become a secondary key.

![image](https://user-images.githubusercontent.com/72783315/136781871-bb0072ac-47b5-4036-ac1b-0a7ee10d7c3d.png)

**Composite key** - If two or more fields make a primary key, they are called the composite keys.

**Foreign key** - When two tables have matching primary keys. A foreign key refers to a primary key in another table

**Link table** - For example a table of invoices contains customer info and product info. A relational database could have a customers as one entity, products as one entity, and invoices (orders) which would link the other two entities. The link table uses a foreign key to link to other tables, (as well as having a primary key).

**Non atomic data** - data that can be brocken up into smaller chunks. Each feild should have 1 single peice of data. Atomic data is much easier to search for. 

**Referencial Intergity** - In a database a foreign key can not reference a non-existant primary key. So an order cannot be placed for a customer that has not signed up yet. The foreign key must depend on a primary key. 

**Normalisation** - []

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
A database using a structured tuple of tables in an ordered logic, where **links** (relations) are formed between tables. Generally, each table/relation represents one "entity type" (such as customers or products). Relational DBs contains the entity's **attributes and relationships**, look at the entity-relationship model for more information.

### Advantages
- Can be accessed over a network, and **mulitple people** can access it at once.
- **Powerful**, **efficient** and **faster** than flat file databases
- Searching is faster because of more compex query support using SQL
- Design of **indexing** makes seaching much faster as well
- Increased security of data - as **user access levels** can be changed and set (eg. teachers can only access students data and not other teachers)
- Has **referential integrity** (data intergrity) - when changes are made to a specific field these changes are cascaded to any relation/table that also contain that field value

### Issues
- Relational database management systems (**RDMS**) are required to maintain the databases. Therefore software must be compatible with the relational database
- Needs advanced knowledge and structuring (eg. **normalisation and entity relational diagrams**)
- Expensive to design, implement and maintain
- Requires training for all users

## Entity Relationship modeling
The 3 main models
- **One to many** (1:M)
- **One to One** (1:1)
- **Many to Many** (M:M) - this one causes problems

<img src="https://raw.githubusercontent.com/JachymT/a-level-cs-blog/main/Computer%20Systems/1.3/1.3.2/images/modeling.JPG">

*diagram notation*
*another key point is that primary keys are underlined and foreign keys are stared* *

An **entity relationship diagram** (ERD) explaining the one to many relationship between the dog owners and their dogs. Ignore the arrow.

![image](https://user-images.githubusercontent.com/72783315/133996102-ac8798ef-8335-4721-8618-c00cb8496982.png)
![image](https://user-images.githubusercontent.com/72783315/133996616-58693ff7-24e2-4b16-9630-eef59b90461f.png)

*images from http://theteacher.info/index.php/computing-principles-01/1-3-exchanging-data/1-3-2-databases/2167-relational-databases-versus-flat-file-databases*

**Example from the RevisionSub.accdb database**
<img src="https://raw.githubusercontent.com/JachymT/a-level-cs-blog/main/Computer%20Systems/1.3/1.3.2/images/relationships.JPG" height="400">

Foriegn key is the many side of the 1:M link

the costomer ID in the first table is the primary key and its linked to the customer ID in the sencond table, which is the foreign key, and does not have to be unique in that table. The **referential intereity** box is ticked when making these links so that a **foreign keys** depends on a an existant **primary key**.

## Query 
The action of searching a database to retrieve a specific peice of data. A **complex query** has more than 1 search critera, often checking more than 1 field. Might be sorted by a primary key

<img src="https://raw.githubusercontent.com/JachymT/a-level-cs-blog/main/Computer%20Systems/1.3/1.3.2/images/query1.JPG" height="400">

## Forms
A simplified way to access a database entry, or add new entries. They make it clear which data is being presented. The image is an example of a form made on the *Students* database.

<img src="https://raw.githubusercontent.com/JachymT/a-level-cs-blog/main/Computer%20Systems/1.3/1.3.2/images/Form.JPG" height="400">

## Reports
A compact way to print or **export** a query; shows data in an orginsed and presentable way. The image is a report made from the a query from the *Students* database.

<img src="https://raw.githubusercontent.com/JachymT/a-level-cs-blog/main/Computer%20Systems/1.3/1.3.2/images/Report.JPG" height="400">

## Input mask
A string of characters that indicates which inputs are valid - a format they need to follow. 
These are used in table fields and forms.

<img src="https://raw.githubusercontent.com/JachymT/a-level-cs-blog/main/Computer%20Systems/1.3/1.3.2/images/input-mask.JPG" height="400">
