from crawler import Crawler
from database import Database


if __name__ == '__main__':
  crawler = Crawler()
  db = Database()

  # navigate to url
  crawler.get(crawler.url)

  leagues = crawler.parse_available_leagues()
  stats = crawler.parse_available_stats()
  player_data = crawler.parse_available_player_data()

  print(player_data)