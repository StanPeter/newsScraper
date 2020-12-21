# you can change rate(the last line) to get more popular or less popular news


# required libraries
import requests
import time
import pdb
import pprint
from bs4 import BeautifulSoup


# main function
def popular_hacker_news(rate):
    hacker_news = []
    skipped = 0  # counts those news without any popularity rate

    for i in range(1, 21):  # has max 20 pages
        res = requests.get("https://news.ycombinator.com/news?p=" + str(i))
        soup = BeautifulSoup(res.text, "html.parser")

        # acquiring neccesary content from website
        links = soup.select(".storylink")
        subtext = soup.select(".subtext")
        ranks = soup.select(".rank")
        for index, item in enumerate(links):  # loop through each website
            try:
                name = links[index].getText()
                href = links[index].get("href", None)
                vote = subtext[index].select(".score")[0].getText()
                rank = ranks[index].getText()

                print(rank, name, vote)
                # how many people voted for the article
                if int(vote.split()[0]) > rate:
                    hacker_news.append((rank, name, href, vote))
            except IndexError as e:  # those without votes
                skipped += 1
                print(f"ERROR {name}: skipped for not having votes")

        print("scraped page: " + str(i))
        time.sleep(3)

    print("articles without votes: " + str(skipped))
    print("total popular news " + str(len(hacker_news)))
    return pprint.pprint(hacker_news)


popular_hacker_news(500)
