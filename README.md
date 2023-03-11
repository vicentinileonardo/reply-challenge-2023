# Reply Challenge 2023

A (very) **greedy** implementation of a valid solution for the **Reply Challenge 2023** (Standard Edition).

The solution is not optimized at all. It is just a greedy (and trivial) implementation of a valid solution.
The main purpose of this repository is to show that even this trivial solution can be used to get a relatively good score.
Leveraging only the first 5 input files, the final score that can be obtained is 5,515,411 that would have achieved the 148th position out of 3990 teams on the leaderboard.
The 6th input file is not included in this repository because, if used, the score would be lowered.

## How to run
The solution can be run using the following command:
```
python3 greedy.py --input N
```
where N is the number of the input file to be used (0 to 6).
Input and output files are hardcoded and can be changed in the source code.

`points.txt` contains the points obtained for each input file.