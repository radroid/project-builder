"""The goal of this module is to automate the process of creating directories
and files for a new project."""


import pathlib
from pathlib import Path


def get_names():
    """Take input from user for the project name and author name. Print out
    the information provided.

    Returns (Tuple):
        proj_name (str): name of project entered by the user.
        author_name (str): name of the author entered by the user.
    """
    print('\n> What would you like to name your project?')
    proj_name = input()
    print('\n> Who is the author of the project? '
          '(Enter full name of the author)')
    author_name = input()

    print('\n### Project Details ###')
    print(f'Project name: {proj_name}')
    print(f'Author\'s name: {author_name}\n')
    return proj_name, author_name


def create_dir(path: str or pathlib.PosixPath, dir_name: str):
    """The function creates a directory at the path specified and with the
    name input.

    Args:
        path (pathlib.PosixPath or str): path to directory creation location.
        dir_name (str): Name of the directory to be created.

    Raises:
        FileNotFoundError: if the path provided does not exist.
        TypeError: if the path provided is not valid or not a directory.

    Returns:
        pathlib.Posix object: This is the path to the directory created.
    """
    if type(path) == str:
        path = Path(path)

    if not path.exists():
        raise FileNotFoundError('The path provided, does not exist.')
    if not path.is_dir():
        raise TypeError('Please input a path to a directory.')

    new_dir = path / dir_name
    new_dir.mkdir()
    return new_dir


def create_readme(path: str or pathlib.PosixPath):
    """The function creates a README.md file at the path specified.

    Args:
        path (strorpathlib.PosixPath): This is the path to the project folder
                                       or directory where the readme file is
                                       to be created.

    Raises:
        FileNotFoundError: if the path provided does not exist.
        TypeError: if the path provided is not valid or not a directory.

    Returns:
        pathlib.Posix object: This is the path to the README.md file created.
    """
    if type(path) == str:
        path = Path(path)

    if not path.exists():
        raise FileNotFoundError('The path provided, does not exist.')
    if not path.is_dir():
        raise TypeError('Please input a path to a directory.')

    readme = path / 'README.md'
    readme.touch()

    with readme.open('w') as write:
        write.write('Hello World!\n')

    return readme


def add_to_readme(path: str or pathlib.PosixPath, proj_name: str, author: str):
    if type(path) == str:
        path = Path(path)

    if not path.exists():
        raise FileNotFoundError('The path provided, does not exist.')
    if not (path.is_file() or path.name == 'README.md'):
        raise TypeError('Please input a path to a README.md file.')

    text_to_write = f"""# {proj_name}
    Welcome to {proj_name}!



    Created by {author}.
    """

    with path.open('w') as readme:
        readme.write(text_to_write)


if __name__ == '__main__':
    proj_name, author_name = get_names()
    new_dir = create_dir(Path.cwd(), proj_name)
