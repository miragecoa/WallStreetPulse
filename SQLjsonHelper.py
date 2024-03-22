from itertools import islice
import sqlite3

# https://docs.python.org/3/library/sqlite3.html
conn = sqlite3.connect('postDB.db')

cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS redditPosts
                  (postId INTEGER PRIMARY KEY, author TEXT, likes INTEGER)''')
conn.commit()

input_dictionary1 = {
    "postId": 12345,
    "author": "JohnSmith",
    "likes": 123
}

input_dictionary2 = {
    "postId": 12345,
    "author": "Greg",
    "likes": 483
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
    for x in range(len(input_dict) - 1):
        sql_prompt += "?, "
    sql_prompt += "?)"

    # Executes prompt
    cursor.execute(sql_prompt, list(input_dict.values()))
    conn.commit()


def delete_post(table_name, input_dict):
    sql_prompt = "DELETE FROM "
    sql_prompt += table_name
    sql_prompt += " WHERE postId = ?"
    cursor.execute(sql_prompt, (input_dict["postId"],))
    conn.commit()


# Replaces a post with another post which has an identical postID
def replace_post(table_name, old_input_dict, new_input_dict):
    keys = list(old_input_dict.keys())
    keys.pop(0)

    old_id = list(old_input_dict.values())[0]
    new_list = list(new_input_dict.values())
    new_id = new_list[0]
    new_list.pop(0)
    new_list.append(old_id)

    if old_id != new_id:
        print("ERROR: postIds", old_id, "(old) and", new_id, "(new) don't match. Cannot replace post")
        exit(0)

    # create Sql_prompt
    sql_prompt = "UPDATE "+table_name+" SET "
    sql_prompt += "=?, ".join(str(v) for v in keys)
    sql_prompt += "=? WHERE postId=?"

    # Execute command
    cursor.execute(sql_prompt, new_list)


def display_table(table_name):
    sql_prompt = "SELECT COUNT(*) FROM "
    sql_prompt += table_name
    cursor.execute(sql_prompt)
    result = cursor.fetchall()
    if result[0][0] == 0:
        print("Table", table_name, "is currently empty")

    else:
        sql_prompt = "SELECT * FROM "
        sql_prompt += table_name
        cursor.execute(sql_prompt)
        rows = cursor.fetchall()
        for row in rows:
            print(row)


def clear_table(table_name):
    cursor.execute("DELETE FROM " + table_name)
    conn.commit()


def drop_table(table_name):
    sql_prompt = "DROP TABLE if EXISTS "
    sql_prompt += table_name
    cursor.execute(sql_prompt)
    conn.commit()
    print("Dropped table", table_name)
    main()


# Modifies the table
def table_modifier(main_table_name):
    action = "0"
    print("Enter an action:\nn - table name\n a - add_post \n d - delete post\n r - replace post\n v - view table\n "
          "c - clear table\nf - drop table\ns - change tables\nh - help\nq - quit\n "
          "----------------------")
    while action != "q":
        action = input()
        print("Action: '", action, "'")
        if action == "h":
            print("Commands:\nn - table name\n a - add_post \n d - delete post\n r - replace post\n v - view table\n "
                  "c - clear table\nf - drop table\ns - change tables\nh - help\nq - quit")
        if action == "n":
            print("Table Name: ", main_table_name)
        if action == "a":
            add_post(main_table_name, input_dictionary1)
        if action == "d":
            delete_post(main_table_name, input_dictionary1)
        if action == "r":
            replace_post(main_table_name, input_dictionary1, input_dictionary2)
        if action == "v":
            display_table(main_table_name)
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
