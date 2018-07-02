from pypco import PCO
import sqlite3
import pandas as pd


pco = PCO("074b34b9536e48fd02134e1a4a1da8efd88d091e661d23cb76a8fafcef4e5c54","bdbb4fef4d377e6f3106d9edca5862d0f372628669575e80b6874530a278eb7d")
db_file = 'songs.sqlite'
# for person in pco.people.people.list():
#     print(person)

def get_pco_songs():
    for song in pco.services.songs.list():
        print(song.data['attributes']['title'])
        #for arrangement in song.rel.arrangements.list():
            #print(arrangement.data['attributes']['lyrics'])


def to_csv():
    db = sqlite3.connect(db_file)
    cursor = db.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    for table_name in tables:
        table_name = table_name[0]
        table = pd.read_sql_query("SELECT * from %s" % table_name, db)
        table.to_csv(table_name + '.csv', index_label='index')
    cursor.close()
    db.close()

def get_sql_songs():
    conn = sqlite3.connect(db_file)
    df = pd.read_sql_query("select * from songs limit 5;",conn)
    print(df['last_modified'])
    conn.close()

def get_sql_last_modified(id):
    conn = sqlite3.connect(db_file)
    df = pd.read_sql_query("select last_modified from songs where id={id:d};".format(id=id), conn)
    if df.empty:
        print('Song with id={id:d} does not exist'.format(id=id))
    else:
        print(df)


def insert_sql_song(id, lyrics):
    values = (id, lyrics)
    conn = sqlite3.connect(db_file)
    cur = conn.cursor()
    cur.execute("insert into songs values ("
                "?," 
                " 'title',"
                " 'alt title',"
                " ?,"
                " '',"
                " '',"
                " '',"
                " '',"
                " '',"
                " '',"
                " '',"
                " null,"
                " null,"
                " null)",
                values)
    conn.commit()
    cur.close()
    conn.close()




#to_csv()
#get_sql_songs()
#insert_sql_song(1988,'oi letra')
get_sql_last_modified(1989)



# for arrangement in pco.services.arrangements.list():
#     print(arrangement)

