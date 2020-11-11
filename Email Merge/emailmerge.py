def read_in_csv():
    """Read in CSV file and store the data"""

    with open(r"Email_List.csv", 'r', encoding="utf-8") as file:
        # Initialising variables to hold data about the csv file
        headings = {}
        rows = 0

        # Store each column as a dict key with an empty array as the value
        csv_headings = file.readline().split("\n")[0].split(",")
        for col in csv_headings:
            headings[col] = []

        # Store data according to the column that it is from
        # Count the number of rows
        for line in file.readlines():
            rows += 1
            data = line.split('\n')
            clean_data = data[0].split(",")
            for num in range(len(csv_headings)):
                headings[csv_headings[num]].append(clean_data[num])

    return headings, rows


def read_in_file():
    """Read in template text file"""

    # Store lines of text files as arrays
    file_lines = open(r'email_template.txt', 'r', encoding="utf-8").readlines()
    return file_lines


def substitute_variables(file_lines, headings, row_num):
    """Sub in the variables into the template"""

    new_file_lines = []

    # Split the lines based on the template variable '%%'
    # Modify the list in place with the new values from the csv file

    for line in file_lines:
        new_email_line = line.split("%%")
        for index, item in enumerate(new_email_line):
            for heading, variable in headings.items():
                if item == heading:
                    new_email_line[index] = variable[row_num]
        new_file_lines.append(new_email_line)

    return new_file_lines


def write_to_file(new_file_lines, num):
    """Write the new data to a file"""

    # Inefficient as it will always rewrite the data in existing files no matter what
    with open(f"email_template_complete_{num + 1}.txt", "w+", encoding="utf-8") as file:
        for line in new_file_lines:
            file.write("".join(line))


def main():
    """Generate emails based on a template"""

    headings, rows = read_in_csv()
    file_lines = read_in_file()

    # For each row in the table, make a new email
    for num in range(rows):
        new_file_lines = substitute_variables(file_lines, headings, num)
        write_to_file(new_file_lines, num)


main()
