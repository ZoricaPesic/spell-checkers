# Requirements
1. **Python 3.x** : Ensure Python 3 is installed on your system.
2. **Dependencies** : Install the required libraries by running:
`pip install -r requirements.txt`

# Run
1. To clone the repository execute:
`git clone https://github.com/ZoricaPesic/spell-checkers/`
2. To run the code execute:
`python main.py`

# Dataset
I downloaded a [Spelling Corrector dataset](https://www.kaggle.com/datasets/bittlingmayer/spelling?resource=download) from kaggle. And used [wikipedia.txt file](https://github.com/ZoricaPesic/spell-checkers/blob/main/wikipedia.txt) that has 1922 lines and each line contains correct spelling of a word followed by : and incorrect spelling of the word to evaluate different spell checking libraries and models.
# Spell checkers 
I used the following libraries and models for text correction:
* [spellchecker library](https://pypi.org/project/pyspellchecker/)
* [autocorrect library](https://github.com/filyp/autocorrect)
* [enchant library](https://pyenchant.github.io/pyenchant/)
* [brillmoore model](https://docs.deeppavlov.ai/en/master/features/models/spelling_correction.html)

# Evaluation
I used metrics: Lexical Recall, Error Recall, Lexical Precision, Error Precision to evaluate each of the libraries and models and got these results:

**spellchecker** :
* Execution time: 0.101 
* Lexical Recall: 0.485
* Error Recall: 0.924
* Lexical Precision: 0.926
* Error Precision: 0.480

**autocorrect** :
* Execution time: 80.169
* Lexical Recall: 0.476
* Error Recall: 0.928
* Lexical Precision: 0.927
* Error Precision: 0.481

**enchant** :
* Execution time: 0.447 
* Lexical Recall: 0.484
* Error Recall: 0.977
* Lexical Precision: 0.976
* Error Precision: 0.494

**brillmoore**
* Execution time: 461.62
* Lexical Recall: 0.480
* Error Recall: 1.0
* Lexical Precision: 1.0
* Error Precision: 0.500

All of the models and libraries show great results. Out of the 4 compared solutions billmoore model had the best results but the slowest execution time, other libraries had much better execution time with little degradation of performances. In conclusion all solutions showed great results, autocorrect library and brillmoore model would be great solution for non real time spell checking, while spellchecker and enchant would be much better for real time spell checking because they have much better execution time.


# Process
I collected correctly and incorrectly spelled words from kaggle in order to calculate number of true positives, true negatives, false positives and false negatives so that i can calculate Lexical Recall, Error Recall, Lexical Precision, Error Precision. Then i used correctly spelled words to calculate number of true positives and false negatives and uncorrectly spelled words to calculate the number of true negatives and false positives.
