import numpy as np

N = 100000

# arrival time simulation uniformly between 7:10 and 7:30
arrival_t = np.random.uniform(0, 20, N)

# If arrival between 0 and 5 min (7:10 to 7:15), you wait until 7:15
# or then wait until 7:30, so waiting is 20 - arrival_t
waiting_t = np.where(arrival_t <= 5, 5 - arrival_t, 20 - arrival_t)
exp_waiting_t = np.mean(waiting_t)

print(f"Expected Waiting Time: {exp_waiting_t:.4f} minutes")
