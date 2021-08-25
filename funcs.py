from typing import Any, Optional
import fire
import sqlite3
import logging
import sys

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler())

con = sqlite3.connect('fpl-1.0.0.sqlite')

def id_ranges(span: int) -> None:
    cur = con.cursor()
    cur.execute("select min(id), max(id) from players")
    min_id, max_id = cur.fetchone()
    logger.info(f"splitting up players table with ids from {min_id} -> {max_id} into id ranges of span {span}")
    # never force evaluation of this whole generator
    id_range = range(min_id, max_id + span, span) # go past the end of the ids on the final range.
    for num in id_range:
        sys.stdout.write(f"{num} ")

def get_names(min_id: int , max_id: Optional[int] = None, printall: bool = False) -> None:
    if not max_id:
        max_id = min_id+1
    cur = con.cursor()
    cur.execute("select web_name from players where id >= ? and id < ?", (min_id, max_id))
    players = cur.fetchall()
    logger.info(f"got names for {len(players)} players")
    if printall:
        logger.info(players)

if __name__ == "__main__":
    fire.Fire() 