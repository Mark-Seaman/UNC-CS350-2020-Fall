from os import listdir
from os.path import exists

from tool.files import read_file, write_file
from tool.text import text_join


def import_existing_book(book, old_book):
    print(f'Importing {book} from {old_book}')
    # table_of_contents(read_book_data(book), old_book)
    chapters = [(1, 'Journey'),
                (9, 'Prayer')]
    import_old_content(book, old_book, chapters)


def import_old_content(book, old_book, chapters):
    print(f'Importing content to {book} from {old_book}')
    for c in chapters:
        print(f'Importing content to {old_book}/{c[1]} --> {book}/{c[0]:02}.md')
        old = f'{old_book}/{c[1]}'
        new = f'Documents/book/{book}/{c[0]:02}.md'
        import_chapter(old, new)


def import_chapter(old, new):
    text = read_file(old)
    # text = text.replace('\n##', '\n#')
    if not exists(new):
        write_file(new, text)


def table_of_contents(book_data, old_book):
    print(f'{book_data["book"]}')
    print(f'{book_data["path"]}')
    parts = parts_list(book_data["parts"])
    chapters = chapter_list(book_data["chapters"])
    print_old_book(book_data["book"], parts, chapters, old_book)


def chapter_list(chapters):
    return "\nChapters\n\n" + text_join([f'    Chapter {i+1} - {c[0]}' for i, c in enumerate(chapters[1:])])


def parts_list(parts):
    return "\nParts\n\n" + text_join([f'    Part {i+1} - {c}' for i, c in enumerate(parts)])


def print_old_book(book, parts, chapters, old_book):
    path = f'Documents/book/{book}/chap_list'
    text = parts + chapters + text_join(sorted(listdir(old_book)))
    write_file(path, text)


# from course.book import read_book_data

# def copy_leverage_docs():
#     print('Copy Leverage Book')
#     copy_chapter('Leverage', 1)
#     copy_chapter('Debt', 2)
#     copy_chapter('Practices', 3)
#
#     copy_chapter('Technology', 4)
#     copy_chapter('Design', 5)
#     copy_chapter('Code', 6)
#     copy_chapter('Test', 7)
#
#     copy_chapter('Release', 8)
#     copy_chapter('Services', 9)
#     copy_chapter('Deployment', 10)
#     copy_chapter('Monitoring', 11)
#
#     copy_chapter('Knowledge', 12)
#     copy_chapter('Teamwork', 13)
#     copy_chapter('Learning', 14)
#     copy_chapter('Planning', 15)
#
#     copy_extra('Part1', 'Part1.md')
#     copy_extra('Part2', 'Part2.md')
#     copy_extra('Part3', 'Part3.md')
#     copy_extra('Part4', 'Part4.md')
#
#
# def copy_chapter(chapter, num):
#     text = read_file(f'Documents/book/Leverage/{chapter}')
#     text = text.replace('\n##', '\n#')
#     path = f'Documents/book/Leverage/{num:02}.md'
#     if not exists(path):
#         write_file(path, text)
#
#
# def copy_extra(chapter, extra):
#     text = read_file(f'Documents/book/Leverage/{chapter}')
#     text = text.replace('\n##', '\n#')
#     path = f'Documents/book/Leverage/{extra}'
#     if not exists(path):
#         write_file(path, text)
#
