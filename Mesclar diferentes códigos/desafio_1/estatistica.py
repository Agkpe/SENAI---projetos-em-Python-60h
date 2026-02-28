import statistics


# MÉDIA

def media(n):
    median = statistics.mean(n)
    return median

# MODA

def moda(n):
    modan = statistics.mode(n)
    return modan

# DESVIO
def desvio(n):
    desvion = statistics.stdev(n)
    return desvion