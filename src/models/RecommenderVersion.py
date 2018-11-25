import enum


# Version | Question  | Answers
# 1       | random    | random
# 2       | nerandom  | random
# 3       | random    | nerandom
# 4       | nerandom  | nerandom

class RecommenderVersion(enum.Enum):
    RR = 1
    NR = 2
    RN = 3
    NN = 4
