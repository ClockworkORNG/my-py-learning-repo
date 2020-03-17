test_db_file = open("D:/tmp/testDB.txt", "r")
database_file = test_db_file.read()

def count_special_chars(database_file):
    special_chars = {
        "=": 0,
        "-": 0,
        "|": 0,
        "alpha": 0
    }
    for char in database_file:
        if char == "=":
            special_chars["="] += 1
        elif char == "-":
            special_chars["-"] += 1
        elif char == "|":
            special_chars["|"] += 1
        else:
            special_chars["alpha"] += 1

    return special_chars

print(count_special_chars(database_file))

#database_list = [{sales} = "snum": 1001, {customers} = "cnum": 2001, {orders} = "onum": 3001]

# либо так
# database_list = [{"snum": 1001}, {"cnum": 2001}, {"onum": 3001}]
# еще можно вот так
# {"sales": {"snum": 1001}, "customers": {"cnum": 2001}, "orders": {"onum": 3001}}

res = count_special_chars("====================  sales  ================")
if res["="] > 10:
    database_file.strip("=")
    database_file.strip()
print(res)

test_db_file.close()