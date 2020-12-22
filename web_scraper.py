# Will write the web scraping required for the ski comp file here
# I need requests lib and beautiful soup?

# First url to scrape: https://www.alta.com/weather

# Create master array of arrays with the required data, setup custom scrape for each mountain
# master array

import requests
from bs4 import BeautifulSoup


master = []

def scrap_alta():

    url = 'https://www.alta.com/weather'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    print(soup.prettify())
    # search all html lines containing table data
    # news_row = soup.find_all('tr', {'class': ['nn']})
    # news = []
    # return ''
    
scrap_alta()


def scrap_webpage():
    webpage_url = "WEBPAGE_URL"
    page = urlopen(webpage_url)
    soup = BeautifulSoup(page, "html.parser")
    # search all html lines containing table data
    news_row = soup.find_all('tr', {'class': ['nn']})
    news = []
    for story in news_row:
        news.append(story.find('a').contents[0])

    df = pd.DataFrame.from_dict(news)

    def dataframe_sum_words(words, dataframe):
        summary = []
        for each in words:
        count = df[0].str.count('\\b'+each+'\\b', re.I).sum()
        summary.append([str(each), str(count)])
        summary_df = pd.DataFrame.from_records(summary, columns=['word','count'])
        return summary_df

    summary = dataframe_sum_words([ENTER_WORDS_OF_INTEREST], df)
    write_data = summary.to_csv(index=False)

    return write_data

