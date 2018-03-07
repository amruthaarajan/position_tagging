import pandas as pd

def Viterbi(tokens, trans_prob, emission_prob,states):
    trans = list(trans_prob.keys())
    prob = 0
    #Initializing the matrix
    V = [[0 for x in range(len(tokens))] for y in range(len(states))]
    V[0][0]=1;
    for tokenIndex in range(1, len(tokens)):
        token = tokens[tokenIndex]
        previousColumnIndex = tokenIndex - 1
        for row_index, trans_value_1 in enumerate(trans):#enumerate generates both index and value. Index in posIndexFrom and the value in posFrom
            previousProbability = V[row_index][previousColumnIndex]
            for column_index, trans_value_2 in enumerate(trans):
                wordPosProbability = emission_prob.get(trans_value_2).get(token, 0)
                posTransitionProbability = trans_prob.get(trans_value_1).get(trans_value_2, 0)
                V[column_index][tokenIndex] = max(V[column_index][tokenIndex],previousProbability * wordPosProbability * posTransitionProbability)


    vDF = pd.DataFrame(V, index=trans, columns=tokens)
    print("Viterbi Matrix:\n", vDF)
    vDF.to_csv("Output_Viterbi.csv")
    #print("Viterbi Probability: \n",vDF.get_value(index= "<stop>", col = "<stop>", takeable=False))
    return vDF




states = ['<start>', 'V', 'N', 'Adj', '<stop>']
observations = ['<start>','learning', 'changes', 'thoroughly','<stop>']
transition_probability = {
    '<start>' : {'V': 0.3, 'N':0.2},
    'V' : {'V': 0.1, 'N': 0.4, 'Adv': 0.4},
    'N' : {'V': 0.3, 'N': 0.1, 'Adv': 0.1},
    'Adv':{'<stop>': 0.1},
    '<stop>': {}
}
emission_probability = {
    'V' : {'learning': 0.003, 'changes': 0.004, 'thoroughly': 0.0},
    'N' : {'learning': 0.001, 'changes': 0.003, 'thoroughly': 0.0},
    'Adv' : {'learning': 0.0, 'changes': 0.0, 'thoroughly': 0.002},
    "<start>": {"<start>": 1},
    "<stop>" : {"<stop>" : 1}
}

Viterbi(observations, trans_prob = transition_probability, emission_prob=emission_probability, states=states)


