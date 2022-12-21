BOOLEAN_LIST = ['True', 'False']
COMMA = ','
NEWLINE = '\n'


def read_data(file_name):
    file = open(file_name)
    content = file.read().splitlines()
    return content


def str_(data):
    return '"' + data + '"'


def spaces(n):
    return n * ' '


def format_text(a, b):
    return spaces(4) + str_(a) + ': ' + b


def format_type(text):
    if len(text) == 0:
        return 'null'
    if text.isalpha():
        if text not in BOOLEAN_LIST:
            return str_(text)
        return text.lower()
    return text


def write_data(file_name, data):
    file = open(file_name, "w")
    file.write(data)
    file.close()


def convert_in_json_text(csv_data, spliterator=COMMA):
    if len(csv_data) < 2:
        return '[]'
    keys = csv_data[0].split(spliterator)
    result = '[' + NEWLINE
    row_count = len(csv_data[1:])

    for row_i, row in enumerate(csv_data[1:]):
        result += spaces(2) + '{' + NEWLINE
        values = row.split(spliterator)
        zipped_key_value = dict(zip(keys, values))
        len_dict = len(zipped_key_value)

        for key_i, key in enumerate(zipped_key_value):
            result += format_text(key, format_type(zipped_key_value[key]))
            if key_i + 1 != len_dict:
                result += COMMA
            result += NEWLINE

        result += spaces(2) + '}'
        if row_i + 1 != row_count:
            result += COMMA
        result += NEWLINE
    result += ']'
    return result


def csv_to_json_file(input_, output_):
    csv_content = read_data(input_)
    json_result = convert_in_json_text(csv_content)
    write_data(output_, json_result)


csv_to_json_file('input.csv.py', 'out.json.py')
