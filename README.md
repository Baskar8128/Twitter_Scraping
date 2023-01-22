 Twitter_Scraping
 
 The web application to scrape the date from twitter using keywords & hashtags with the tweet limits and range of the tweets.
 
Code Base: Python

Library used :pandas, snscrape, streamlit

Database: Mongodb.

Workflow:

collecting the  keywords & hashtags, limit and date range from user.
based on that scraping the data from twitter using snscrape library.
using pandas the scraped data's are stored as dataframe
the dataframe can be viewed in the web app using streamlit library.
then based on the user requirement the dataframe can be stored to mongodb database.
the collection of data's will be stored in the mongodb created database.
the collected data can be downloaded as CSV and JSON file.
