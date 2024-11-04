from spellchecker import SpellChecker
import os
from sklearn.metrics import accuracy_score,precision_score, recall_score, f1_score
from autocorrect import Speller
import enchant
from deeppavlov import build_model, configs
import time

def load_dataset():
    correct=[]
    misspelled=[]

    with open(os.path.join("wikipedia.txt"),'r') as file:
        for line in file:
            line=line.strip()
            if line:
                correct_word, misspelled_word=line.split(":")
                correct.append(correct_word.lower())
                misspelled.append(misspelled_word.lower())
    return correct,misspelled


def evaluate_py_spell_checker_predictions():
    spell = SpellChecker()

    flagged_valid_words=spell.unknown(correct)
    tp=len(correct)-len(flagged_valid_words)
    fn=len(misspelled)

    flagged_invalid_words=spell.unknown(misspelled)
    tn=len(flagged_invalid_words)
    fp=len(misspelled)-tn
    return tp,tn,fp,fn


def evaluate_autocorrect_speller_predictions():
    spell = Speller(lang='en')
    flagged_valid_words=[]
    flagged_invalid_words = []

    for word in correct:
        corrected_word = spell(word)
        if corrected_word != word:
            flagged_valid_words.append(word)

    tp = len(correct) - len(flagged_valid_words)
    fn = len(misspelled)

    for word in misspelled:
        corrected_word = spell(word)
        if corrected_word != word:
            flagged_invalid_words.append(word)

    tn = len(flagged_invalid_words)
    fp = len(misspelled) - tn
    return tp, tn, fp, fn


def evaluate_enchant_predictions():
    predictions = []
    dict = enchant.Dict("en_US")

    flagged_valid_words = [word for word in correct if not dict.check(word)]
    tp = len(correct) - len(flagged_valid_words)
    fn = len(misspelled)

    flagged_invalid_words = [word for word in misspelled if not dict.check(word)]
    tn = len(flagged_invalid_words)
    fp = len(misspelled) - tn
    return tp, tn, fp, fn


def evaluate_brillmoore_predictions():
    model = build_model('brillmoore_wikitypos_en', download=True)
    corrected_valid_words=model(correct)
    flagged_valid_words = [(word, correction) for word, correction in zip(correct, corrected_valid_words) if word != correction]
    tp = len(correct) - len(flagged_valid_words)
    fn = len(misspelled)

    corrected_invalid_words=model(misspelled)
    flagged_invalid_words = [(word, correction) for word, correction in zip(misspelled, corrected_invalid_words) if word != correction]
    tn = len(flagged_invalid_words)
    fp = len(misspelled) - tn

    return tp, tn, fp, fn


if __name__ == '__main__':

    correct,misspelled=load_dataset()

    start_time=time.time()
    tp,tn,fp,fn=evaluate_brillmoore_predictions()
    lr=lexical_recall=tp/(tp+fn)
    er=error_recall=tn/(tn+fp)
    lp=lexical_precision =tp/(tp+fp)
    ep=error_precision =tn/(tn+fn)
    end_time=time.time()

    print(end_time-start_time)
    print(lr)
    print(er)
    print(lp)
    print(ep)
