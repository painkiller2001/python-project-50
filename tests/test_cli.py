from gen_diff.cli import welcome_user


def test_cli_file():
    excepted = 'Compares two configuration files and shows a difference.'
    assert excepted == welcome_user()