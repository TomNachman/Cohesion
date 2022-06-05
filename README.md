
# The Cohesion Pipeline

Given a division, Cohesion pipeline should give a cohesion score and recommend a suitable name for each group
A suitable should suit each member of the group and be the tightest one (no entities in other groups suits the name), using inter and intra score


## Installation

```bash
pip install cohesion-pipeline
```

## Usage Example
The input to the cohesion_score functin must be a csv,txt,tsv file with a tab['\t'] seperator and must have 'label' and 'text' columns
```bash
from Cohesion import mainPipeline
bad_score, bad_topics = mainPipeline.cohesion_score('..\\resources\\tests\\bad_division.txt') # give full path to file
good_score, good_topics = mainPipeline.cohesion_score('..\\resources\\tests\\good_division.txt')
print('bad_score: ', bad_score)
print('bad_topics: ', bad_topics)

print('good_score: ', good_score)
print('good_topics: ', good_topics)
```
