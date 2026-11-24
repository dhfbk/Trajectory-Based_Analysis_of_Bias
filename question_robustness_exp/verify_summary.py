#!/usr/bin/env python3
"""Verify key reported counts using only Python's standard library."""
import csv
from pathlib import Path
root=Path(__file__).resolve().parent

def read(name):
    with (root/name).open(encoding='utf-8',newline='') as f:
        return list(csv.DictReader(f,delimiter='\t'))
checkpoints=read('checkpoint_comparison.tsv')
stories=read('story_comparison.tsv')
judgments=read('behavioral_question_judgments.tsv')
assert len(checkpoints)==1608 and len(stories)==120 and len(judgments)==4824
assert sum(r['majority_vote']!='' for r in checkpoints)==1605
assert sum(r['same_vote']=='True' and r['majority_vote']!='' for r in checkpoints)==1499
assert sum(r['both_committed']=='True' for r in checkpoints)==948
assert sum(r['same_direction']=='True' and r['both_committed']=='True' for r in checkpoints)==941
assert sum(r['first_direction_agrees']!='' for r in stories)==117
assert sum(r['first_direction_agrees']=='True' for r in stories)==115
assert sum(r['timing_difference']=='0.0' for r in stories)==96
assert sum(r['behavioral_first_label']=='unresolved' for r in stories)==3
assert sum(r['first_direction_agrees']=='False' for r in stories)==2
assert sum(r['final_same']=='True' for r in stories)==107
print('All question robustness release checks passed.')
