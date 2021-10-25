# Transaction Processing

## EDI
Electronic Data Interchange is the exchange of business documents between companies in a standardised format to replace post and email.

![image](https://user-images.githubusercontent.com/72783315/138685173-a31ca1d1-ac11-48cd-bdfe-717459667d12.png)

![image](https://user-images.githubusercontent.com/72783315/138689833-3a3c2ff8-d8be-4beb-8d43-c7354c5f494f.png)

This electronic data can then be handled and translated into a database

## Transactions
In a database, a single logical opperation perfomed is handed by transaction processing as a transaction

Transactions, whilst in principle indivisible, can be broken down into serveral processess, we can group them together and also refer to them as transactions. The following statement is true for any transaction: Each transaction must succeed or fail all-together; it can never be only partially complete.

For example accepting a card payment is commen transaction that must be regulated and checked.

INSERT, SELECT, UPDATE, DELETE are all SQL commands that can be used in the context of transactions.

## ACID
Properties that garantee intergity and reliablity for all transactions.

### Atomicity
Following the definition of a transaction, a change to a database must be performed completely or not at all. There should be no possibility of a partially performed transaction.

### Consistency
Any change in the database must retain the overall state of the database. This means keeping referential integrity and so any validation rules will be upheld.

For example money removed from one account should be added to another so the balance total is maintained.

### Isolation
Transactions happening simultaiously must be processsed equivilantly to them being processed one after the other.

This means they are not interrupted and other processes cannot accesss the data concerned at that time - they are in isolation.

A DBMS implements this with **record locking**

### Durability
Once a change has been successfuly made to a database, it must not be lost. The transactions must remain even under a system failure or power outage.

This is done by writing all transactions onto non-volitile secondary storage and holding them until the transcation has completed. Only once everything is backed up are the changes finalized.

Furthermore once commited to the database the changes stay commited.

## Record Locking
Prevents simultaneous access to records in a database to avoid inconsistencies. 

Whilst a transaction by user A is happening on a record, that record is locked and user B has to wait for the tranasction to be finished before they can perform thier transaction

This can lead to deadlocks where both users A and B are waiting for each other to proceed.

<img width="1002" alt="https://youtu.be/lhSVTsRLEDM" src="https://user-images.githubusercontent.com/72783315/138735056-7a26536d-d96b-419e-801b-c6ea096a8254.png">

## Serialisation
Ensures transactions do not overlap with each other or effect each other, the following techniques prevent, for example, a record being updated twice simultaniously by different users.

### Timestamp ordering
Read and write timestamps are saved for objects in a database. There are used to identify if an object has been changed in the time it has been tried to edit. If so updating it is denied.

### Commitment ordering
Transactions are ordered based on thier dependencies and thier time of creation. This prevents two transactions being lost if they simultaiously try to update a record (prevents deadlocking). One request is blocked based on the commitment order untill the other is completed

## Redundancy
Intentional data redundancy is created when companies do not want to loose important information and so store the same data across many physical locations. These computer systems then save them money and trouble, since the overall system is not affected if one goes down.
