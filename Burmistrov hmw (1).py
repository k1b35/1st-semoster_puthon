SOURCE_CODE_DELIMITER = "# ---<source code delimeter>---"
SOURCE_MARKDOWN_DELIMITER = "<!---source markdown delimeter--->"


def read_data(file_name):
    file = open(file_name)
    content = file.read()
    return content


def write_data(file_name, data):
    f = open(file_name, "w")
    f.write(data)
    f.close()


def prepare_md_title(data):
    splitted = data.split('\n')
    title, description = "", ""
    for line in splitted:
        if line.startswith('# title'):
            title = line.lstrip("# title ")
        elif line.startswith('# description '):
            description = line.lstrip("# description ")
    return title, description


def md_text_formatted(title, description, source_code):
    md_link = '-'.join(title.lower().split())
    template = '+ [{}](#{})\n\n## {}\n\n{}\n\n```python\n{}\n```'

    return template.format(title, md_link, title, description, source_code)


def convert_to_md(data):
    data = content.split(SOURCE_CODE_DELIMITER)
    titles, source_code = data[0], data[1]
    title, description = prepare_md_title(titles)
    result = md_text_formatted(title, description, source_code.lstrip())
    return result


content = read_data('solution.txt')
md_content = convert_to_md(content)
write_data('out.txt', md_content)
