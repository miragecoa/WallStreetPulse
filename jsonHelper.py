import json
import os

DATA_FILENAME = 'data.json'
input_dictionary = {
  "postId": 12345,
  "author": "JohnSmith",
  "likes": 123
}

# Creates an empty json file if json file doesn't exist
if not os.path.isfile(DATA_FILENAME):
    with open(DATA_FILENAME, mode='w', encoding='utf-8') as f:
        json.dump([], f)


# Adds a new post
def add_post():
    # load previous entries
    with open(DATA_FILENAME, "r") as file:
        data = json.load(file)

    # re-add old entries + new entry.
    entry = {'postId': input_dictionary['postId'], 'author': input_dictionary['author'], 'likes': input_dictionary['likes']}
    data.append(entry)
    with open(DATA_FILENAME, 'w') as file:
        file.write(json.dumps(data))


# deletes an entry given an entry's index.
def delete_data(index):
    new_data = []
    with open(DATA_FILENAME, "r") as file:
        data = json.load(file)

    for i, entry in enumerate(data):
        if i != int(index):
            new_data.append(entry)

    with open(DATA_FILENAME, "w") as file:
        json.dump(new_data, file)


def print_data():
    with open(DATA_FILENAME, "r") as file:
        data = json.load(file)
        # iterate over data
        for i, entry in enumerate(data):
            entry_id = entry["postId"]
            entry_author = entry["author"]
            entry_likes = entry["likes"]
            print(f"Index Number: {i}")
            print(f"postId : {entry_id}")
            print(f"author : {entry_author}")
            print(f"likes : {entry_likes}")
            print("\n\n")



