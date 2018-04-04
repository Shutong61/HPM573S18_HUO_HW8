import Parameters as P
import HW6 as Cls
import SupportSteadyState as Support


cohortONE = Cls.SetOfGames(id=1, n_games=P.SIM_POP_SIZE, prob_head=0.5)

Outcome1 = cohortONE.simulation()


cohortTWO = Cls.SetOfGames(id=2, n_games=P.SIM_POP_SIZE, prob_head=0.45)

Outcome2 = cohortTWO.simulation()

# print outcomes of each cohort
Support.print_outcomes(Outcome1, 'Fair coin:')
Support.print_outcomes(Outcome2, 'Unfair coin for which the probability of head is 45%:')


# print comparative outcomes
Support.print_comparative_outcomes(Outcome1, Outcome2)

