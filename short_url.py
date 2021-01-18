import random
import string
import sqlite3

# open a connection to the db - create a new db if there is no such db - first step always
conn = sqlite3.connect('test.db')

c = conn.cursor()

# creates a table in db if not already present
c.execute('''CREATE TABLE IF NOT EXISTS urltable(LONG_URL TEXT NOT NULL, 
SHORT_URL CHAR(7));''')


# define random gen/short url gen function and db reads and writes here

def char_gen():
    collision = True
    while collision:
        char = ''.join([random.choice(string.ascii_letters + string.digits) for i in range(7)])
        print(char)
        # do a db look up to make sure random string is not already in db, none is returned if there is no match
        if db_short_search(char)==None:
            collision = False
    return char

def db_insert(long_url, short_url):
    short_url_list = short_url.split("/") # split short url to get key word for the lookup and storage
    key_word = short_url_list.pop() # gets the path or key word chars from the list
    URLs = [long_url,key_word]
    c.execute("INSERT OR IGNORE INTO urltable VALUES (?,?)", URLs)
    print("Successfully inserted into db")

def db_short_search(key_word):
    charac = (key_word,) # forming a tuple to search in db as ?
    c.execute('SELECT * FROM urltable WHERE SHORT_URL=?', charac)
    return c.fetchone()

def db_long_search(key_word):
    charac = (key_word,) # forming a tuple to search in db as ?
    c.execute('SELECT * FROM urltable WHERE LONG_URL=?', charac)
    return c.fetchone()

def db_url_retrieve(key_word):
    charac = (key_word,) # forming a tuple to search in db as ?
    c.execute('SELECT * FROM urltable WHERE SHORT_URL=?', charac)
    row_retrieved = c.fetchone()
    #print(row_retrieved)
    if (row_retrieved == None):
        print("Tiny url doesn't exist")
    else:
        return row_retrieved[0] # long url output from the tuple or list

def show_rows():
    for row in c.execute('SELECT * FROM  urltable'):
        print(row)

def main():

    # main code
    result = input("Are you here to generate a tiny url? (press y or n)...")
    if (result == "y" or result== "yes"):
        long = input("Enter the long url for which you want to create a tiny url: ")
        if db_long_search(long) == None:
            if long==None:
                print("enter valid url")
                exit()
            short = char_gen()
            db_insert(long, short)
            print(f"Here is the tiny url http://harish.com/{short}, please save it for future use")
        else:
            print("long url you provided is already present, please use the short url search tool instead")

        conn.commit()
    else:
        short = input("Enter tiny url to retrieve long url: ")
        short_url_list = short.split("/")  # split short url to get key word for the lookup and storage
        keyword = short_url_list.pop()  # gets the path or key word chars from the list
        #print(keyword)
        long = db_url_retrieve(keyword)
        if long !=None:
            print("Here is the long url for the tinyurl you provided: {}".format(long))

    # just to check our db table
    #print("Displaying all rows in current table") - z6LBFbB/UvMDS0u/RQHJHMp examples of keywords
    #show_rows()


    conn.close()

if __name__ == '__main__': main()


