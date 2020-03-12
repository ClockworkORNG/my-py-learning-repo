test_db_file = open("D:/tmp/testDB.txt", "r")
database_file = test_db_file.read()

def count_special_chars(database_file):
    special_chars = {
        "=": 0,
        "-": 0,
        "|": 0,
        "other_chars": 0
    }
    for char in database_file:
        if char == "=":
            special_chars["="] += 1
        elif char == "-":
            special_chars["-"] += 1
        elif char == "|":
            special_chars["|"] += 1
        else:
            special_chars["other_chars"] += 1

    return special_chars

print(count_special_chars(database_file))

test_db_file.close()