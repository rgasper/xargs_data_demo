# xargs_data_demo

demonstration of using xargs and id iteration to process a big ol pile of data

## setup

```console
pip install -r requirements.txt
```

## database

dataset taken from <https://medium.com/@jiayu./fantasy-premier-league-sqlite-dataset-5b0bfdd052d4>.
incomplete schema of `players` table:

```sql
CREATE TABLE players (
  id integer,
  photo text,
  web_name text,
  team_code integer,
  status text,
  code integer,
  first_name text,
  second_name text,
  squad_number integer,
  news text,
  now_cost integer,
  news_added text,
  chance_of_playing_this_round integer,
  chance_of_playing_next_round integer,
  value_form real,
  ...
```

## run

run the whole shebang, splitting up the table into 10 row chunks:

```console
python funcs.py id_ranges 10 | xargs -n 2 python funcs.py get_names
```

run just one of the functions:

```console
python funcs.py id_ranges 10
```

```console
 python funcs.py get_names 171 181 true
```

## note on stdout and stderr

stdout is used for real output. stderr is used for messaging. python logger writes to stderr. print writes to stdout. Don't use print.
