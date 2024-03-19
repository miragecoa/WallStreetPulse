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


def clear_table(table_name):
    cursor.execute("DELETE FROM " + table_name)
    conn.commit()


def drop_table(table_name):
    sql_prompt = "DROP TABLE if EXISTS "
    sql_prompt += table_name
    cursor.execute(sql_prompt)
    conn.commit()
    main()


# Modifies the table
def table_modifier(main_table_name):
    action = "s"
    while action != "q":
        action = input("Enter an action:\nn - table name\n a - add_post \n d - delete post\n v - view table\n "
                       "c - clear table\nf - drop table\ns - change tables\nq - quit\n "
                       "----------------------\n")
        print("Action: '", action, "'")
        if action == "n":
            print("Table Name: ", main_table_name, "\n")
        if action == "a":
            add_post(main_table_name, input_dictionary)
        if action == "d":
            delete_post()
        if action == "v":
            display_table()
        if action == "c":
            clear_table(main_table_name)
        if action == "f":
            drop_table(main_table_name)
        if action == "q":
            print("Shutting down...")
            conn.close()
            exit(0)
        if action == "s":
            main()
        print("-----------------------------------")


# Creates a new table
def create_table(main_table_name):
    sql_prompt = "CREATE TABLE IF NOT EXISTS "
    sql_prompt += main_table_name
    sql_prompt += " (postId INTEGER PRIMARY KEY, author TEXT, likes INTEGER)"
    cursor.execute(sql_prompt)
    conn.commit()


# Asks to create a new table
def ask_new_table(main_table_name):
    print("The table called \"", main_table_name, "\" does not exist.")
    action = input("Do you want to create a new table? Y\\N\n")
    action = action.lower()
    if action == "y":
        create_table(main_table_name)
        table_modifier(main_table_name)
    else:
        main()


# Check if table exists
def check_table_exists(main_table_name):
    sql_prompt = "SELECT count(*) FROM sqlite_master WHERE type='table' AND name='"
    sql_prompt += main_table_name + "'"
    cursor.execute(sql_prompt)
    result = cursor.fetchall()
    if result[0][0] == 0:
        return False
    else:
        return True


# The first menu the user sees when code runs
def jump_start_menu():
    main_table_name = "l"

    while main_table_name == "l" or main_table_name == "q":
        main_table_name = input("Which table do you want to access? Enter l to list all tables, enter q to quit\n")
        if main_table_name == "q":
            conn.close()
            exit(0)

        if main_table_name == "l":
            sql_prompt = "SELECT name FROM sqlite_master WHERE type='table';"
            cursor.execute(sql_prompt)
            result = cursor.fetchall()
            print(result)

    return main_table_name


def main():
    name = jump_start_menu()
    # Checks if table exists
    if check_table_exists(name):
        table_modifier(name)

    # Asks if you want to make a new table
    else:
        ask_new_table(name)


if __name__ == "__main__":
    main()

conn.close()
