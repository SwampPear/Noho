from sqlite3 import Connection


class Database:
    def __init__(self, db_path='DATA.db'):
        self.db_path = db_path
        self.con = Connection(db_path)
        self.cur = self.con.cursor()

    
    def execute(self, statement):
        self.cur.execute(statement)


    def init_database(self):
        self.execute(
            """
            CREATE TABLE IF NOT EXISTS team (
                -- Custodial:
                team_id INT NOT NULL,
                team_name VARCHAR(15) NOT NULL,

                -- Keys
                PRIMARY KEY (team_id)
            );

            CREATE TABLE IF NOT EXISTS game (
                -- Custodial:
                game_id INT NOT NULL,
                team_1_id INT NOT NULL,
                team_2_id INT NOT NULL,

                -- Keys:
                PRIMARY KEY (game_id),
                CONSTRAINT fk_team_1_id FOREIGN KEY (team_1_id) REFERENCES team(team_id),
                CONSTRAINT fk_team_2_id FOREIGN KEY (team_2_id) REFERENCES team(team_id)
            );

            CREATE TABLE IF NOT EXISTS player (
                -- Custodial:
                player_id INT NOT NULL,
                team_id INT NOT NULL,
                player_name VARCHAR(127) NOT NULL,
                --player_position SET(need to set),

                -- Player Stats:
                
                -- need to set player stats,

                -- Keys:
                PRIMARY KEY (player_id),
                CONSTRAINT fk_team_id FOREIGN KEY (team_id) REFERENCES team(team_id)
            );

            CREATE TABLE IF NOT EXISTS game_stats_per_player (
                -- Custodial:
                game_id INT NOT NULL,
                player_id INT NOT NULL,

                -- Game Stats per Player:
                pass_yards FLOAT(6, 2),
                rush_yards FLOAT(6, 2),
                receiving_yards FLOAT(6, 2),
                pass_rush_rec_tds FLOAT(6, 2),
                fg_made FLOAT(6, 2),
                pass_tds FLOAT(6, 2),
                rush_rec_tds_combo FLOAT(6, 2),
                fantasy_score FLOAT(6, 2),
                rush_yards_combo FLOAT(6, 2),
                receiving_yards_combo FLOAT(6, 2),
                completions_first_10_pass_attempts FLOAT(6, 2),
                rush_yards_first_5_attempts FLOAT(6, 2),
                receiving_yards_first_2_receptions FLOAT(6, 2),
                sacks_combo FLOAT(6, 2),
                pass_attempts FLOAT(6, 2),
                rush_rec_yds_combo FLOAT(6, 2),
                kicking_points FLOAT(6, 2),
                rush_rec_yds_combo FLOAT(6, 2),
                rec_targets FLOAT(6, 2),
                tackles_ast FLOAT(6, 2),
                sacks FLOAT(6, 2),
                tackles_for_loss FLOAT(6, 2),

                -- Keys:
                CONSTRAINT fk_game_id FOREIGN KEY (game_id) REFERENCES game(game_id),
                CONSTRAINT fk_player_id FOREIGN KEY (player_id) REFERENCES player(player_id)
            );
            """
        )
