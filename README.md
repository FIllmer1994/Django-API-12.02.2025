# Django-API-12.02.2025

**Steps to run program**
- Basically all works like general Django APIs.
- To include built in mock data use url-extension „/api/create-mock/“.
- For requests include compnay_id and date like „/api/data/1/2025-02-11“.

**Design decisions and assumptions; maintainability, scalability, performance**
- Basically, I used a standard design of a Django API and tried to keep things simple. While the creation of mock data in views is clearly not very beautiful, it ensures that the mock data can be created by calling one url. This leads to simple testing which makes the use of the program easier. Also, the use of comments in code, telling names of variables and code separation over different classed in separate files makes the code more understandable. I used rest_framework since it makes views and serialization easier to handle.
- I added the ID manually as a separate field because I think this fits the assignment better. Nevertheless it would have worked otherwise as well.
- The main issue is the search after the correct date in cases in which the query_date is not contained in the database itself for the respective company_id. I set up the program in a way that only needs to order data with forecast_date prior to query date and does it only if the query date itself is not in the database.  However, this could be a problem if there were many entries in the database.

**Problems with setup**
- Searching for correct date can be time-consuming.
- There are no rules for the length of list „values“. This can lead to storing useless data.

**Possible optimisations**
- If the time since the first forecast isn't too long it would be possible to store the data for every possible relevant query_date with the correct forecast_date. This way we could directly get the correct data and wouldn’t need the possibly time-consuming search mentioned above. However, this could increase the rows in the database dramatically since we would need entries for every day since the first forecast. Therefore it would only be possible if we had enough resources.
- If the database was big and there would be many requests, rate-limit, load-balancer and job-scheduler all would be good possibilities to improve performance. Applying cache could be an interesting solution as well under th same circumstances. In addition, since the query date allows a lot of different queries, I’m unsure how useful it would be.
- With better knowledge of the field values there could be rules implemented for the length, or searches could be enabled for more precise variables instead of only one general list.
