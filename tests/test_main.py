import builtins
from main import (_get_words,
                  NOUN,
                  ADJECTIVE,
                  VERB,
                  make_ing,
                  make_base_verb)


def test_make_ing():
    assert make_ing(u'dog') == 'doging'


def test_make_base_verb():
    assert make_base_verb(u'dogging') == 'dogg'
    assert make_base_verb(u'dogged') == 'dogg'
    assert make_base_verb(u'doggeded') == 'dogged'


def test_get_words():
    assert len(_get_words(NOUN)) == 1


def test_get_multiple_words():
    assert len(_get_words(NOUN, num_to_grab=10)) == 10


def test_get_word_opens_correct_file(monkeypatch):
    """
    Im not sure this is actually a good way of testing anything
    but it became a thing and I wanted to see if I could do it.
    :param monkeypatch:
    """
    original_open = builtins.open

    def make_file_assertion(type, original_open):
        def assert_filename(f, read_mode):
            # Probably should check path...
            # but im happy enough with filename
            assert '{}.txt'.format(type) in f
            return original_open(f, read_mode)
        return assert_filename

    monkeypatch.setattr(
        builtins,
        'open',
        make_file_assertion(NOUN, original_open)
    )
    _get_words(NOUN)
    monkeypatch.setattr(
        builtins,
        'open',
        make_file_assertion(ADJECTIVE, original_open)
    )
    _get_words(ADJECTIVE)
    monkeypatch.setattr(
        builtins,
        'open',
        make_file_assertion(VERB, original_open)
    )
    _get_words(VERB)


def test_landing_page(app):
    assert app.get('/').status == '200 OK'
