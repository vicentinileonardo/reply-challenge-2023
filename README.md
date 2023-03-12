# Reply Challenge 2023

A (very) **greedy** implementation of a valid solution for the **Reply Code Challenge 2023** (Standard Edition).

The solution is not optimized at all. It is just a greedy (and **trivial**) implementation of a valid solution.

The main purpose of this repository is only to show that even this trivial solution can be used to get a relatively good score (useful for the University League leaderboard) and do not want to provide a smart solution.

## Idea

The idea is to just place snakes horizontally, on rows that do not contain wormholes, starting from 0 position. 

Therefore the rows are covered from left to right for the length of snakes.

If the number of rows is not enough, remaining snakes to be placed are simply not used (blank line in output file).

## Score

Leveraging only the first 5 input files, the final score that can be obtained is 5,515,411 that would have achieved the 148th position out of 3990 teams on the leaderboard.

The 6th input file is not considered because, if used, the score would be lowered.

## Repository structure
+ `greedy.py` contains the solution.
+ `input_files` contains the input files.
+ `output_files` contains the output files already generated.
+ `points.txt` contains the points obtained for each input file.

## How to run
The solution can be run using the following command:
```
python3 greedy.py --input N
```
where `N` is the number of the input file to be used (0 to 6).
Input and output files are hardcoded and can be changed in the source code.

