"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""


TESTS = {
    "Basics": [
        {"input": "18", "answer": 10},
        {"input": "1010101011", "answer": 2},
        {"input": "222", "answer": 3},
        {"input": "A23B", "answer": 14},
        {"input": "123F", "answer": 22},
        {"input": "IDDQD", "answer": 0},
        {"input": "ZZZ", "answer": 36},
        {"input": "XYZ", "answer": 0}
    ],
    "Extra": [
        {"input": "T", "answer": 30},
        {"input": "BTA1MCNQL", "answer": 32},
        {"input": "M3", "answer": 26},
        {"input": "29", "answer": 12},
        {"input": "HEEL", "answer": 23},
        {"input": "33112", "answer": 6},
        {"input": "707776957", "answer": 12},
        {"input": "2648", "answer": 11},
        {"input": "94308", "answer": 13},
    ]
}
