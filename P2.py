import Parameters as P
import HW6 as Cls
import SupportTransientState as Support

# create multiple cohorts for when the coin is head
multiCohort1 = Cls.MultipleGameSets(
    ids=range(1000),   # [0, 1, 2 ..., NUM_SIM_COHORTS-1]
    n_games_in_a_set=[P.REAL_POP_SIZE] * P.NUM_SIM_COHORTS,  # [REAL_POP_SIZE, REAL_POP_SIZE, ..., REAL_POP_SIZE]
    prob_head=[P.HEAD_PROB]*P.NUM_SIM_COHORTS # [p, p, ...]
)
# simulate all cohorts
multiCohort1.simulation()

# create multiple cohorts for when the coin is tail
multiCohort2 = Cls.MultipleGameSets(
    ids=range(1000,2000),   # [NUM_SIM_COHORTS, NUM_SIM_COHORTS+1, NUM_SIM_COHORTS+2, ...]
    n_games_in_a_set=[P.REAL_POP_SIZE] * P.NUM_SIM_COHORTS,  # [REAL_POP_SIZE, REAL_POP_SIZE, ..., REAL_POP_SIZE]
    prob_head=[P.HEAD_PROBTWO]*P.NUM_SIM_COHORTS
)
# simulate all cohorts
multiCohort2.simulation()

# print outcomes of each cohort
Support.print_outcomes(multiCohort1, 'Fair coin:')
Support.print_outcomes(multiCohort2, 'Unfair coin for which the probability of head is 45%:')


# print comparative outcomes
Support.print_comparative_outcomes(multiCohort1, multiCohort2)
