import os
import random
import itertools
from flask import Flask, render_template

app = Flask(__name__)

NOUN = 'noun'
VERB = 'verb'
ADJECTIVE = 'adjective'


def _get_words(type, num_to_grab=1):
    with open(
            os.path.join(
                os.path.dirname(__file__),
                '{}.txt'.format(type)
            ),
            'r'
    ) as word_bag_file:
        word_list = list(word_bag_file.readlines())
        return [random.choice(word_list).strip().title()
                for _ in itertools.repeat(None, num_to_grab)]


def make_base_verb(verb):
    if verb[-3:] == 'ing':
        verb = verb[:-3]
    elif verb[-2:] == 'ed':
        verb = verb[:-2]
    return verb


def make_ing(verb):
    return "{}{}".format(
        make_base_verb(verb),
        'ing'
    )


@app.route('/')
def landing_page():
    nouns = _get_words(NOUN, 7)
    verbs = _get_words(VERB, 5)
    adjectives = _get_words(ADJECTIVE, 1)
    company, product = nouns[0:2]
    nouns = nouns[2:]
    title_one = "Revolutionize {}".format(
        verbs.pop()
    )
    title_two = "Stop trying to {} the {}".format(
        verbs.pop().lower(), nouns.pop().lower()
    )
    title_three = "Industry Tested, Community Approved"

    desc_one = "{} was always {} until now!".format(
        make_base_verb(verbs.pop()), adjectives.pop().lower()
    )
    desc_two = "Never again will {} be so easy".format(
        make_ing(verbs.pop()).lower()
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
        nouns.pop().lower(), make_base_verb(verbs.pop().lower())
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
