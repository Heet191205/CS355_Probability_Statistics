# Simulation: Journey of Airline
# Heet Shah - Hshah2

import numpy as np
from datetime import datetime, timedelta

#value within mu ± 3σ
def clamp(val, mu, sigma):
    min_val = mu - 3 * sigma
    max_val = mu + 3 * sigma
    return max(min(val, max_val), min_val)

# convert float hours to timedelta (h2d)
def h2d(hrs):
    # Convert hours to minutes
    minutes = int(hrs * 60)
    return timedelta(minutes=minutes)


# convert string to datetime object (time only)
def to_time(hhmm): # hours and minutes 
    return datetime.strptime(hhmm, "%H:%M") # how to read the time string

# simulate airline using numpy for random sampling
def sim_airline(trials, name):
    on_time = 0
    ttl_time = timedelta() # total time
    success = 0
    stranded = 0

    for _ in range(trials):
        t = to_time("08:00") # t - time

        if name == "One":
            ab = clamp(np.random.normal(4.0, 0.4), 4.0, 0.4)
            t += h2d(ab)

            if t <= to_time("12:29"):
                t = to_time("12:30")
            elif t <= to_time("12:59"):
                t = to_time("13:00")
            else:
                stranded += 1
                continue

            bc = clamp(np.random.normal(4.0, 0.4), 4.0, 0.4)
            t += h2d(bc)

            if t <= to_time("16:59"):
                t = to_time("17:00")
            elif t <= to_time("17:29"):
                t = to_time("17:30")
            elif t <= to_time("17:59"):
                t = to_time("18:00")
            else:
                stranded += 1
                continue

            cd = clamp(np.random.normal(3.5, 0.4), 3.5, 0.4)
            t += h2d(cd)

            if t <= to_time("21:00"):
                on_time += 1
        else:
            ae = clamp(np.random.normal(3.5, 0.8), 3.5, 0.8)
            t += h2d(ae)

            if t <= to_time("11:59"):
                t = to_time("12:00")
            elif t <= to_time("12:29"):
                t = to_time("12:30")
            else:
                stranded += 1
                continue

            ef = clamp(np.random.normal(4.0, 0.8), 4.0, 0.8)
            t += h2d(ef)

            if t <= to_time("16:29"):
                t = to_time("16:30")
            elif t <= to_time("16:59"):
                t = to_time("17:00")
            elif t <= to_time("17:29"):
                t = to_time("17:30")
            else:
                stranded += 1
                continue

            fd = clamp(np.random.normal(3.5, 0.8), 3.5, 0.8)
            t += h2d(fd)

            if t <= to_time("20:30"):
                on_time += 1
        success += 1
        ttl_time += (t - to_time("08:00"))

    avg = ttl_time / max(success, 1)  
    prob_on = on_time / max(success, 1)  
    prob_stranded = stranded / max(trials, 1)

    print(f"Airline {name} Results:")
    print(f"Average Arrival Time: {str(to_time('08:00') + avg)[11:16]}")
    print(f"On-time Probability: {round(prob_on, 4)}")
    print(f"Stranded Probability: {round(prob_stranded, 4)}\n")

def main():
    trials = 10000
    sim_airline(trials, "One")
    sim_airline(trials, "Two")

if __name__ == "__main__":
    main()