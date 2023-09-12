from selenium import webdriver
from selenium.webdriver.common.by import By


class Crawler:
    def __init__(self, url='https://app.prizepicks.com') -> None:
        self.url = url
        self.driver = webdriver.Chrome()


    def get(self, url) -> None:
        self.driver.get(url)

    
    def add_cookie(self, cookie):
        self.driver.add_cookie(cookie)


    def find_league_elements(self):
        _league_container = self.driver.find_element(By.XPATH, '//*[@id="scrollable-area"]')

        return _league_container.find_elements(By.CLASS_NAME, 'league')


    def parse_available_leagues(self):
        _league_elements = self.find_league_elements()

        return [_league.find_element(By.CLASS_NAME, 'name').text for _league in _league_elements]


    def find_league_element(self, league):
        _league_elements = self.find_league_elements()

        for _league in _league_elements:
            if _league.find_element(By.CLASS_NAME, 'name').text == league:
                return _league
          
        return None


    def find_stat_elements(self):
        _stat_container = self.driver.find_element(By.XPATH, '//*[@id="board"]/div[1]/div')

        return _stat_container.find_elements(By.CLASS_NAME, 'stat')


    def parse_available_stats(self):
        _stat_elements = self.find_stat_elements()

        return [_stat for _stat in _stat_elements]


    def find_stat_element(self, stat):
        _stat_elements = self.find_stat_elements()

        for _stat in _stat_elements:
            if _stat.text == stat:
                return _stat
          
        return None


    def find_player_wrapper_elements(self):
        _player_wrapper_container = self.driver.find_element(By.XPATH, '//*[@id="projections"]/div/div')
        return _player_wrapper_container.find_elements(By.CLASS_NAME, 'projection')


    def find_player_elements(self):
        player_elements = []

        _player_wrappers = self.find_player_wrapper_elements()

        for _player_wrapper in _player_wrappers:
            _player = _player_wrapper.find_element(By.CLASS_NAME, 'proj-container')
            _player = _player.find_element(By.CLASS_NAME, 'player-container')
            player_elements.append(_player.find_element(By.CLASS_NAME, 'player'))

        return player_elements


    def parse_available_player_data(self):
        player_data = []

        _players = self.find_player_elements()

        for _player in _players:
            _name = _player.find_element(By.CLASS_NAME, 'name').text
            _team_position = _player.find_element(By.CLASS_NAME, 'team-position').text
            _date = _player.find_element(By.CLASS_NAME, 'date').text
            _opponent = _player.find_element(By.CLASS_NAME, 'opponent').text

            player_data.append({
                'name': _name,
                'team_position': _team_position,
                'date': _date,
                'opponent': _opponent
            })

        return player_data