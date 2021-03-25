Develop a management application for an online store.
This application is RESTful API for product management and reporting

**Use cases**

•	User can retrieve all products in the store.
•	User can retrieve a single product in the store according to its ID.
•	User can add a new product or remove an existing product.
•	User can change some detail of the already existing product.
•	User can download products report.

**Database**

The application data should be persisted to an in-memory database (like H2).

**Reporting API**

The application should generate a report every 5 minutes and save it as a snapshot into the database. 
Make the interval configurable as an application property.
The products in each report snapshot should be sorted by random (shuffle) order.



 **pull orianc561/online-store:part1**
 _pull out docker image from public repository at hub.docker.com_
part1: Pulling from orianc561/online-store
Digest: sha256:ccabbed1b866741e264e05a971333aedae6d4c57fff5182771fbbcff9051fe9a
Status: Image is up to date for orianc561/online-store:part1
docker.io/orianc561/online-store:part1
