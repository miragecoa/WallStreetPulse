from itertools import islice
import sqlite3
# https://docs.python.org/3/library/sqlite3.html
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
    # Creates the sql prompt to insert a post
    sql_prompt = "INSERT INTO redditPosts("
    for key in islice(input_dictionary.keys(), 0, len(input_dictionary)-1, 1):
        sql_prompt += key
        sql_prompt += ", "
    sql_prompt += list(input_dictionary.keys())[-1]
    sql_prompt += ") VALUES ("
    for x in range(len(input_dictionary)-1):
        sql_prompt += "?, "
    sql_prompt += "?)"
    print("sql_prompt: ", sql_prompt)

    # Executes prompt
    cursor.execute(sql_prompt, list(input_dictionary.values()))
    conn.commit()


def update_likes(new_likes):
    input_dictionary["likes"] = new_likes
    cursor.execute("UPDATE redditPosts SET likes = ? WHERE id = ?",
                   (new_likes, input_dictionary["postId"]))
    conn.commit()


def display_table():
    cursor.execute("SELECT COUNT(*) FROM redditPosts")
    result = cursor.fetchall()
    if result[0][0] == 0:
        print("redditPosts is currently empty\n")

    else:
        cursor.execute("SELECT * FROM redditPosts")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        print("\n")


def delete_post():
    cursor.execute("DELETE FROM redditPosts WHERE postId = ?", (input_dictionary["postId"],))
    conn.commit()


def clear_table():
    cursor.execute("DELETE FROM redditPosts")


def main():
    action = "s"
    while action != "q":
        action = input("Enter an action:\n a - add_post \n d - delete post\n v - view table\n "
                       "c - clear table\nq - quit\n "
                       "----------------------\n")
        print("Action: '", action, "'")
        print("Output: ")
        if action == "a":
            add_post()
        if action == "d":
            delete_post()
        if action == "v":
            display_table()
        if action == "c":
            clear_table()
        if action == "q":
            print("Shutting down...")
        print("-----------------------------------")


if __name__ == "__main__":
    main()

conn.close()
