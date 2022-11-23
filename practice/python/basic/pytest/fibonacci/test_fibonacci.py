import pytest

from my_fibonacci import fibonacci


def test_fibonacci(capsys):
    fibonacci(5)

    out, _ = capsys.readouterr()

    assert out == (
        '1\n'
        '1\n'
        '2\n'
        '3\n'
        '5\n'
    )
