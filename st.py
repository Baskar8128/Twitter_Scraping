import snscrape.modules.twitter as sntwitter
import pymongo
import pandas as pd
import streamlit as st
from PIL import Image

st.set_page_config(page_title='Twitter_scraping')  # Title
st.header('TWITTER SCRAPING')  # Subtitle

col0, col1, col2, col3 = st.columns(4)
with col1:
    image = Image.open('Streamlit.jpeg')
    st.image(image)
with col2:
    image = Image.open('python.jpg')
    st.image(image)
with col3:
    image = Image.open('Mongodb.jpeg')
    st.image(image)


def tweets_inputs():  # function to get the inputs
    with col0:
        c = st.sidebar.text_input('Enter keyword or Hashtag')
        st.sidebar.write(c)
        limit = st.sidebar.number_input('Enter the num of tweets', 0, 5000)
        st.sidebar.write(limit)
        d = st.sidebar.date_input('Tweets from:')
        st.sidebar.write(d)
        e = st.sidebar.date_input('Tweets till:')
        st.sidebar.write(e)
        query = f"(from:{c}) until:{e} since:{d}"
        return query, limit, c


result, rang, key = tweets_inputs()

tweets_data = []


def twitter_scraping():  # function to view the scraped dataframe

    for i, tweet in enumerate(sntwitter.TwitterSearchScraper(result).get_items()):
        if i > rang:
            break
        else:
            tweets_data.append([tweet.date, tweet.id, tweet.url, tweet.content, tweet.user.username,
                                tweet.replyCount, tweet.retweetCount, tweet.lang, tweet.source, tweet.likeCount])
    df = pd.DataFrame(tweets_data,
                      columns=['Date', 'ID', 'URL', 'Tweet Content', 'User', 'Reply Count', 'Retweet Count', 'Language',
                               'Source', 'Like Count'])
    if len(df) != 0:
        st.subheader("Scraped tweets")
        st.dataframe(df)
    return df.head()


df = twitter_scraping()


def database_mdb():  # function to import df to mongodb

    if len(df) != 0:
        client = pymongo.MongoClient(
            "mongodb+srv://Baskar:Baskar123@cluster0.v4dvebx.mongodb.net/?retryWrites=true&w=majority")
        db = client["TwitterScraping"]
        collection = db[f"{key}"]
        data = df.to_dict(orient="records")
        collection.insert_many(data)
        if st.button("Import to Mongodb"):
            st.write("uploaded")
        else:
            st.write("☝ Click here to upload")


database_mdb()


def receiver():  # function to download the df as CSV and JSON format

    def convert_csv():
        return df.to_csv()

    def convert_json():
        return df.to_json()

    a = convert_csv()
    b = convert_json()
    if len(df) != 0:
        st.download_button(
            label="Download as CSV file",
            data=a,
            file_name=f'{key}.csv',
            mime='text/csv'
        )
        st.download_button(
            label="Download as CSV file",
            data=b,
            file_name=f'{key}.csv',
            mime='text/json'
        )


receiver()
