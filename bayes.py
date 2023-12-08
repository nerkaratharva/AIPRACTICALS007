def main():

    population = 1000000

    P_ill = 0.01
    P_positive_if_ill = 0.99 # sensitivity
    P_negative_if_healthy = 0.99 # specificity

    calculate_without_bayes(population, P_ill, P_positive_if_ill, P_negative_if_healthy)

    print()

    calculate_with_bayes(P_ill, P_positive_if_ill, P_negative_if_healthy)


def calculate_without_bayes(population, P_ill, P_positive_if_ill, P_negative_if_healthy):

    heading = "Calculate P(ill | positive) without Bayes' Theorem"
    print(heading)
    print("=" * len(heading) + "\n")

    percent_ill = P_ill * 100
    number_ill = population * P_ill
    number_healthy = population * (1 - P_ill)
    ill_positive = number_ill * P_positive_if_ill
    healthy_positive = number_healthy * (1 - P_negative_if_healthy)
    P_ill_if_positive = ill_positive / (ill_positive + healthy_positive)

    print(f"Population:                {population}")
    print(f"Percent ill:               {percent_ill}%")
    print(f"Number ill:                {number_ill:>.0f}")
    print(f"Number healthy:            {number_healthy:>.0f}")
    print(f"P(positive if ill):        {P_positive_if_ill}")
    print(f"P(negative if healthy):    {P_negative_if_healthy}")
    print(f"Ill and test positive:     {ill_positive:>.0f}")
    print(f"Healthy but test positive: {healthy_positive:>.0f}")
    print(f"P(ill | positive):        {P_ill_if_positive:>.2f}")


def calculate_with_bayes(P_ill, P_positive_if_ill, P_negative_if_healthy):


    P_healthy = 1 - P_ill
    P_positive_if_healthy = 1 - P_negative_if_healthy
    P_ill_if_positive = (P_positive_if_ill * P_ill) / ((P_healthy * P_positive_if_healthy) + (P_ill * P_positive_if_ill))

    heading = "Calculate P(ill | positive) with Bayes' Theorem"
    print(heading)
    print("=" * len(heading) + "\n")

    print(f"P(ill):                 {P_ill}")
    print(f"P(healthy):             {P_healthy}")
    print(f"P(positive if ill):     {P_positive_if_ill}")
    print(f"P(positive if healthy): {P_positive_if_healthy:>.2f}\n")

    print("                                        P(positive if ill) * P(ill)")
    print("P(ill | positive) = -------------------------------------------------------------------")
    print("                      P(healthy) * P(positive if healthy) + P(ill) * P(positive if ill)")

    print("\n")

    print(f"                                               {P_positive_if_ill} * {P_ill}")
    print("                   = -------------------------------------------------------------------")
    print(f"                                         {P_healthy} * {P_positive_if_healthy:>.2f} + {P_ill} * {P_positive_if_ill}")

    print("\n")

    print(f"                   = {P_ill_if_positive:>.2f}")


main()


