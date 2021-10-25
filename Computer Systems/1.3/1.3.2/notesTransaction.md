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

## ACID
Properties that garantee intergity and reliablity for all transactions.

### Atomicity

### Consistency

### Isolation

### Durability
Once a change has been successfuly made to a database, it must not be lost. The transactions must remain even under a system failure or power outage.

This is done by writing all transactions onto non-volitile secondary storage and holding them until the transcation has completed. Only once everything is backed up are the changes finalized.

Furthermore once commited to the database the changes stay commited.
