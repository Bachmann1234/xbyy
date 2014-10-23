import builtins
from main import (_get_words,
                  NOUN,
                  ADJECTIVE,
                  VERB,
                  BASEVERB)


def test_get_words_ing():
    assert all(
        w.endswith('ing')
        for w in _get_words(
            VERB,
            num_to_grab=100,
            ends_with='ing'
        )
    )


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
    monkeypatch.setattr(
        builtins,
        'open',
        make_file_assertion(BASEVERB, original_open)
    )
    _get_words(BASEVERB)


def test_landing_page(app):
    assert app.get('/').status == '200 OK'
