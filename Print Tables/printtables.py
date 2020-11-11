def find_max_length(rows):
    """Find the max length of the strings in the columns"""

    max_lens = []
    for row in rows:
        max_len = 0
        for r in row:
            if len(r) > max_len:
                max_len = len(r)
        max_lens.append(max_len)
    return max_lens


def get_max_lengths(columns):
    """Find the max lengths of all columns"""

    all_max_lens = find_max_length(columns)
    return all_max_lens


def read_in_games():
    """Read in the games.txt and store the rows and columns in arrays"""

    with open(r'games.txt', 'r', encoding="utf-8") as file:
        table_rows = []
        table_columns = []
        columns = 0

        # Adding the data held within the txt file
        # Get rid of any existing whitespace in the file
        # Add single whitespace at the start and end of each string to ensure consistent padding
        lines = file.read().split("\n")
        for index, line in enumerate(lines):
            if index == 0:
                for item in line.split(","): columns += 1
            rows = line.split(',')
            new_row = [f" {r.strip()} " for r in rows]
            table_rows.append(new_row)

        # Reading in the data in columns in order to find the maximum length of characters easily
        for index in range(columns):
            table_columns.append([row[index] for row in table_rows])

    return table_rows, table_columns


def display_table(all_max_lens, rows, columns):
    """Display the table itself"""

    # Define symbols for table separators
    plus = "+"
    dash = "-"
    sep = plus + plus.join(dash * r for r in all_max_lens) + plus

    # Print out the table
    print(sep)
    print("".join(f"|{rows[0][num]:<{all_max_lens[num]}s}" for num in range(len(columns))) + "|")
    print(sep)
    for row in range(1, len(rows)):
        print("".join(f"|{rows[row][num]:<{all_max_lens[num]}s}" for num in range(len(columns))) + "|")
    print(sep)


def main():
    """Print out a table of games.txt"""

    table_rows, table_columns = read_in_games()
    all_max_lens = get_max_lengths(table_columns)
    display_table(all_max_lens, table_rows, table_columns)


main()
