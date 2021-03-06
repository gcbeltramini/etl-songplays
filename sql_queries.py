table_names = ('songs', 'artists', 'time', 'users', 'songplays')

# CREATE TABLES

song_table_create = """
CREATE TABLE IF NOT EXISTS songs (
  song_id VARCHAR(64) PRIMARY KEY,
  title VARCHAR,
  artist_id VARCHAR,
  year SMALLINT,
  duration DOUBLE PRECISION
);
"""

artist_table_create = """
CREATE TABLE IF NOT EXISTS artists (
  artist_id VARCHAR(64) PRIMARY KEY,
  name VARCHAR,
  location VARCHAR,
  latitude DOUBLE PRECISION,
  longitude DOUBLE PRECISION
);
"""

time_table_create = """
CREATE TABLE IF NOT EXISTS time (
  start_time TIMESTAMP WITH TIME ZONE PRIMARY KEY,
  hour SMALLINT,
  day SMALLINT,
  week SMALLINT,
  month SMALLINT,
  year SMALLINT,
  weekday SMALLINT
);
"""

user_table_create = """
CREATE TABLE IF NOT EXISTS users (
  user_id INTEGER PRIMARY KEY,
  first_name VARCHAR,
  last_name VARCHAR,
  gender CHAR(1),
  level CHAR(4)
);
"""
# gender = "M" or "F"
# level = "free" or "paid"

songplay_table_create = """
CREATE TABLE IF NOT EXISTS songplays (
  songplay_id SERIAL PRIMARY KEY,
  start_time TIMESTAMP WITH TIME ZONE NOT NULL,
  user_id INTEGER NOT NULL,
  level CHAR(4),
  song_id VARCHAR(64),
  artist_id VARCHAR(64),
  session_id INTEGER,
  location VARCHAR,
  user_agent VARCHAR
);
"""

# INSERT RECORDS

SONG_TABLE_INSERT = """
INSERT INTO songs (song_id, title, artist_id, year, duration)
VALUES (%s, %s, %s, %s, %s)
ON CONFLICT (song_id) DO NOTHING;
"""

ARTIST_TABLE_INSERT = """
INSERT INTO artists (artist_id, name, location, latitude, longitude)
VALUES (%s, %s, %s, %s, %s)
ON CONFLICT (artist_id) DO NOTHING;
"""

TIME_TABLE_INSERT = """
INSERT INTO time (start_time, hour, day, week, month, year, weekday)
VALUES (%s, %s, %s, %s, %s, %s, %s)
ON CONFLICT (start_time) DO NOTHING;
"""

USER_TABLE_INSERT = """
INSERT INTO users (user_id, first_name, last_name, gender, level)
VALUES (%s, %s, %s, %s, %s)
ON CONFLICT (user_id) DO UPDATE SET level = EXCLUDED.level
"""

SONGPLAY_TABLE_INSERT = """
INSERT INTO songplays (start_time, song_id, artist_id, user_id, level,
                       session_id, location, user_agent)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
"""

# FIND SONGS

SONG_SELECT = """
SELECT songs.song_id, songs.artist_id
FROM songs
INNER JOIN artists ON artists.artist_id = songs.artist_id
WHERE
      songs.title = %s
  AND artists.name = %s
  AND songs.duration = %s;
"""

# QUERY LISTS

CREATE_TABLE_QUERIES = [song_table_create, artist_table_create,
                        time_table_create, user_table_create,
                        songplay_table_create]
DROP_TABLE_QUERIES = [f'DROP TABLE IF EXISTS {table:s}'
                      for table in table_names]
