import os
import random
import itertools
from flask import Flask, render_template

app = Flask(__name__)

NOUN = 'noun'
VERB = 'verb'
ADJECTIVE = 'adjective'
BASEVERB = 'baseVerbs'


def _get_words(type, num_to_grab=1, ends_with=''):
    with open(
            os.path.join(
                os.path.dirname(__file__),
                '{}.txt'.format(type)
            ),
            'r'
    ) as word_bag_file:
        word_list = [word for word in word_bag_file.readlines()
                     if word.strip().endswith(ends_with)]
        return [random.choice(word_list).strip().title()
                for _ in itertools.repeat(None, num_to_grab)]


@app.route('/')
def landing_page():
    nouns = _get_words(NOUN, 7)
    verbs = _get_words(VERB, 2)
    base_verbs = _get_words(BASEVERB, 3)
    adjectives = _get_words(ADJECTIVE, 1)
    company, product = nouns[0:2]
    nouns = nouns[2:]
    title_one = "Revolutionize {}".format(
        verbs.pop()
    )
    title_two = "Stop trying to {} the {}".format(
        base_verbs.pop().lower(), nouns.pop().lower()
    )
    title_three = "Industry Tested, Community Approved"

    desc_one = "{} was always {} until now!".format(
        base_verbs.pop(), adjectives.pop().lower()
    )
    desc_two = "Never again will {} be so easy".format(
        _get_words(VERB, 1, ends_with='ing').pop().lower()
    )
    desc_three = (
        "Backed by {} Certification and "
        "winner of the {} award for {}"
    ).format(
        nouns.pop(),
        nouns.pop(),
        nouns.pop().lower()
    )

    phrase_one = "The {} that {}s".format(
        nouns.pop().lower(), base_verbs.pop().lower()
    )
    return render_template(
        'index.html',
        product=product,
        company=company,
        nouns=nouns,
        title_one=title_one,
        title_two=title_two,
        title_three=title_three,
        desc_one=desc_one,
        desc_two=desc_two,
        desc_three=desc_three,
        phrase_one=phrase_one
    )
