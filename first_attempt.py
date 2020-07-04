import spacy

from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest

article = "croatians voted sunday in three constituencies around the country in a mini-rerun of legislative elections held last week , electoral officials said .   the voting started in rijeka , on the adriatic coast , in pozega in eastern croatia and in dugo selo , a suburb of the capital zagreb .   polling was to end sunday evening .   the outcome of the voting -- held because of irregularities in the initial round last sunday -- will not affect the overall outcome of the legislative elections held last week and won by the rightwing ruling party of croatian president franjo tudjman .   final results of the elections will be published next week when the results of sunday 's rerun polls are in .   tudjman 's ruling croatian democratic union -lrb- hdz -rrb- party won an absolute majority in the poll , according to partial , unofficial results announced so far but fell short of its target of two thirds of the ###-member parliament .   in his first press conference here since the poll , tudjman on saturday named zlatko matesa as new prime minister , to replace nikica valentic who he said was retiring for health reasons .   matesa , economy minister in the outgoing government , is expected to announce the makeup of his government next week .   most portfolios are expected to remain unchanged with mate granic expected to stay as foreign minister and gojko susak as defense minister .   the new parliament is expected to meet for the first time between november ## and december # .   international observers pronounced polling in last week 's polls relatively fair but criticised the reduction in representation for the minority serbs , the vote given to the ultranationalist croat diaspora in bosnia and elsewhere , the ruling party 's domination of the state - run media and occasionally sloppy counting and checking procedures . ."
StopWords = list(STOP_WORDS)
NLP = spacy.load('en_core_web_sm')

doc = NLP(article)

tokens = [token.text for token in doc]
punctuation = punctuation + '\n'

word_frequencies = {}

for word in doc:
    if word.text.lower() not in StopWords:
        if word.text.lower() not in punctuation:
            if word.text not in word_frequencies.keys():
                word_frequencies[word.text] = 1
            else:
                word_frequencies[word.text] += 1

max_frequency = max(word_frequencies.values())

for word in word_frequencies.keys():
    word_frequencies[word] = word_frequencies[word]/max_frequency

sentence_tokens = [sent for sent in doc.sents]
sentence_scores = {}

for sent in sentence_tokens:
    for word in sent:
        if word.text.lower() in word_frequencies.keys():
            if sent not in sentence_scores.keys():
                sentence_scores[sent] = word_frequencies[word.text.lower()]
            else:
                sentence_scores[sent] += word_frequencies[word.text.lower()]

select_length = int(len(sentence_scores))

summary = nlargest(select_length, sentence_scores, key = sentence_scores.get)

final_summary = [word.text for word in summary]
summary = ' '.join(final_summary)

print(summary)