import enum


# Version | Question  | Answers
# 1       | random    | random
# 2       | trained   | random
# 3       | random    | trained
# 4       | trained   | trained

class RecommenderVersion(enum.Enum):
    RR = 1
    TR = 2
    RT = 3
    TT = 4
