import sqlite3

conn = sqlite3.connect('postDB.db')

cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS redditPosts
                  (postId INTEGER PRIMARY KEY, author TEXT, likes INTEGER)''')
conn.commit()

input_dictionary = {
  "postId": 12345,
  "author": "JohnSmith",
  "likes": 123
}


def add_post():
    cursor.execute("INSERT INTO redditPosts (postId, author, likes) VALUES (?, ?, ?)",
                   (input_dictionary["postId"], input_dictionary["author"], input_dictionary["likes"]))
    conn.commit()


def update_likes(new_likes):
    input_dictionary["likes"] = new_likes
    cursor.execute("UPDATE redditPosts SET likes = ? WHERE id = ?",
                   (new_likes, input_dictionary["postId"]))
    conn.commit()


def display_table():
    cursor.execute("SELECT * FROM redditPosts")
    rows = cursor.fetchall()
    for row in rows:
        print(row)


def delete_post():
    cursor.execute("DELETE FROM redditPosts WHERE id = ?", (input_dictionary["postId"],))
    conn.commit()


conn.close()
