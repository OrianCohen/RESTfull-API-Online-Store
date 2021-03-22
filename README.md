Use cases
•	User can retrieve all products in the store.
•	User can retrieve a single product in the store according to its ID.
•	User can add a new product or remove an existing product.
•	User can change some detail of the already existing product.
•	User can download products report.

Database
The application data should be persisted to an in-memory database (like H2).

Reporting API
The application should generate a report every 5 minutes and save it as a snapshot into the database. 
Make the interval configurable as an application property.
The products in each report snapshot should be sorted by random (shuffle) order.
