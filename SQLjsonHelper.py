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


def add_post(table_name, input_dict):
    # Checks if post already exists in database
    sql_prompt = "SELECT 1 FROM "
    sql_prompt += table_name
    sql_prompt += " WHERE postId = "
    sql_prompt += str(input_dict["postId"])
    cursor.execute(sql_prompt)
    result = cursor.fetchall()
    if result:
        print("ERROR: Post already added/ Same postID")
        return

    # Creates the sql prompt to insert a post
    sql_prompt = "INSERT INTO "
    sql_prompt += table_name
    sql_prompt += "("
    sql_prompt += ", ".join(str(v) for v in input_dict.keys())
    sql_prompt += ") VALUES ("
    for x in range(len(input_dict)-1):
        sql_prompt += "?, "
    sql_prompt += "?)"
    print("sql_prompt: ", sql_prompt)

    # Executes prompt
    cursor.execute(sql_prompt, list(input_dict.values()))
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
        print("redditPosts Table is currently empty\n")

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
        if action == "a":
            add_post("redditPosts", input_dictionary)
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
