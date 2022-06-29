from os.path import exists
from re import sub

from tool.text import text_join, text_lines


def convert_to_headings(text, line=1):
    text = suboutline(text, line)
    text = sub('\n *\n', '\n', text)
    text = text_join([('# '+t) if not t.startswith(' ') else t for t in text_lines(text) ])
    text = text.replace('\n                    ', '\n\n###### ')
    text = text.replace('\n                ', '\n\n##### ')
    text = text.replace('\n            ', '\n\n#### ')
    text = text.replace('\n        ', '\n\n### ')
    text = text.replace('\n    ', '\n\n\n## ')
    return text


def convert_to_outline(headings):
    text = text_lines(headings)
    text = [t.rstrip() for t in text if t.startswith('#')]
    text = [t.replace('###### ', '                    ') for t in text]
    text = [t.replace('##### ', '                ') for t in text]
    text = [t.replace('#### ', '            ') for t in text]
    text = [t.replace('### ', '        ') for t in text]
    text = [t.replace('## ', '\n    ') for t in text]
    text = [t.replace('# ', '\n\n') for t in text]
    return text_join(text)


def convert_to_slides(text):
    text = text.replace('\n###### ', '        * ')
    text = text.replace('\n##### ', '    * ')
    text = text.replace('\n#### ', '* ')
    return text


def find_chapters(text):
    text = text_lines(text)
    text = [(i+1, line) for i, line in enumerate(text) if line.strip() and not line.startswith('            ')]
    return text


def main_topics(text, depth=3):
    text = text_lines(text)
    indent = ' ' * depth * 4
    text = [('    '+line) for i, line in enumerate(text) if line.strip() and not line.startswith(indent)]
    text = [line[4:] for line in text]
    return text_join(text)


def outline_as_indent(tree):
    output = ''
    for node in tree:
        output += f'{node[0]}\n'
        for n2 in node[1:]:
            output += f'    {n2[0]}\n'
            for n3 in n2[1:]:
                output += f'        {n3[0]}\n'
                for n4 in n3[1:]:
                    output += f'            {n4[0]}\n'
                    for n5 in n4[1:]:
                        output += f'                {n5[0]}\n'
    return output


def outline_as_markdown(tree, indent='#'):
    text = ''
    for n in tree:
        text += indent + ' ' + n[0] + '\n\n'
        if n[1:]:
            text += outline_as_markdown(n[1:], indent + '#')
    return text


def outline_as_json(tree):
    nodes = []
    for node in tree:
        nodes.append(dict(name=node[0], kids=outline_as_json(node[1:])))
    return nodes


def outline_as_text(tree, indent=''):
    output = ''
    for node in tree:
        kids = outline_as_text(node[1:], indent+'    ')
        output += f'{indent}{node[0]}\n {kids}'
    return output


def outline_stats(tree):
    text = outline_as_text(tree)
    return f'{len(text_lines(text))} lines in outline\n'


def outline_tree(lines, indent=''):
    tree = []
    child_indent = ' ' * 4 + indent
    while lines and lines[0].startswith(indent):
        label = lines[0].strip()
        lines = lines[1:]
        kids, lines = outline_tree(lines, child_indent)
        tree.append([label] + kids)
    return tree, lines


def read_outline(path):
    if exists(path):
        return open(path).read()
    else:
        return f"**error** - File not found, {path}"


def read_outline_tree(path):

    def read_outline_lines(path):
        return [line for line in text_lines(open(path).read()) if line.strip()]

    tree, lines_remaining = outline_tree(read_outline_lines(path))
    # print(tree)
    assert not lines_remaining
    return tree


def suboutline(text, line=1):
    lines = text_lines(text)[line-1:]
    indent = ' ' * (len(lines[0]) - len(lines[0].lstrip()))
    output = ['%s' % lines[0].strip()]
    for x in lines[1:]:
        if x.startswith(indent + '    '):
            output.append(x[len(indent):])
        else:
            if x.lstrip():
                break
    return text_join(output)



# def create_slide_markdown(path, settings):
#     outline_file = f'{path}.outline'
#     markdown_file = f'{path}.md'
#     tree = read_outline_tree(outline_file)
#     text = outline_as_slides(tree, settings)
#     write_file(markdown_file, text)
#

# def outline_as_slides(tree, settings):
#     output = ''
#     for node in tree:
#         for n2 in node[2:]:
#
#             output += f'\n\n## {n2[0]}\n\n'
#
#             if settings['intro']:
#                 for n3 in n2[1:]:
#                     output += f'* {n3[0]}\n'
#
#             for n3 in n2[1:]:
#                 output += f'\n\n### {n3[0]}\n\n'
#
#                 for n4 in n3[1:]:
#                     output += f'* {n4[0]}\n'
#
#                     for n5 in n4[1:]:
#                         output += f'    * {n5[0]}\n'
#     return output

