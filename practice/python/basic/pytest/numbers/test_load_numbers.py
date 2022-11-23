import pytest

from my_numbers import load_numbers_sorted


@pytest.fixture
def txt(tmpdir) -> str:
    tmpfile = tmpdir.join('numbers.txt')
    
    # 前処理
    with open(tmpfile, 'w') as f:
        for n in [2, 5, 4, 3, 1]:
            f.write('{}\n'.format(n))

    yield str(tmpfile)
    
    # 後処理
    tmpfile.remove()

def test_load_numbers_sorted(txt):
    assert load_numbers_sorted(txt) == [1, 2, 3, 4, 5]
