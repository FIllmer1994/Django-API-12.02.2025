# Django-API-12.02.2025

1.	Steps to run program
•	Basically all works like general Django APIs.
•	To include built in mock data use url-extension „/api/create-mock/“.
•	For requests include compnay_id and date like „/api/data/1/2025-02-11“.

2.	Design decisions and assumptions; maintainability, scalability, performance
•	Basically, I used a standard design of a Django API and tried to keep things simple. While the creation of mock data in views is clearly not very beautiful, it ensures that the mock data can be created in one step. This leads to simple testing which makes the use of the program easier similar to the use of comments in code, telling variable-names and code separation over different classed in separate files. I used rest_framework since it makes views and serialization easier.
•	I added the ID manually as a separate field because I think this fits the assignment better but it would have worked otherwise as well.
•	The main issue is the search after the correct date in cases where the query_date is not in the database itself for the respective company_id. I set it up in a way that only needs to order half of the list and does it only if the query_date itself is not in the database but nevertheless this could be a problem if there were many entries in the database.

3.	Problems with setup
•	Searching for correct date can be time-consuming.
•	There are no rules for length of list „values“ which can lead to storing useless data.

4.	Possible optimisations
•	If the time since the first forecast would not be too long it would be possible to store the data with a column query_date such that we could directly get the correct data and wouldn’t need the possible time-consuming searching mentioned above. However, this would increase the rows in the database dramatically since we would need entries for every day since the first forecast, so it would only be possible if we would have enough resources.
•	Rate-limit, load-balancer and job-scheduler all would be good possibilities to improve performance if the database would be big and the API should be able to handle many requests. Applying cache would be interesting as well, however, since the query date allows a lot of different queries, I’m unsure how useful it would be.
•	By better knowledge of forecast values there could be rules implemented or searches after more precise variables.
