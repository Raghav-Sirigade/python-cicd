from nlplogic.corenlp import search_wikipedia, summarize_wikipedia, get_phrase


def test_get_phrase():
    assert 'leopardus' in get_phrase('ocelot')


def test_search_wikipedia():
    assert 'Ocelot' in search_wikipedia('ocelot')


def test_summarize_wikipedia():
    assert 'ocelot' in summarize_wikipedia('ocelot')
