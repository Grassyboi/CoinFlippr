import os
import random
import time

history = {
    "heads": 0,
    "tails": 0,
    "sim_heads": 0,
    "sim_tails": 0,
    "sim_runs": 0,
    "run_heads": 0,
    "run_tails": 0,
    "run_runs": 0,
}

def flip_coin(in_sim=False, in_run=False):
    result = "Heads" if random.choice([True, False]) else "Tails"
    if in_sim:
        history[f"sim_{result.lower()}"] += 1
    elif in_run:
        history[f"run_{result.lower()}"] += 1
    else:
        history["heads" if result == "Heads" else "tails"] += 1
    return result

def spam_until_in_a_row(target_count):
    current_streak = 0
    last_result = None
    start_time = time.time()  # Start timing
    while current_streak < target_count:
        result = flip_coin(in_sim=True)
        print(f"Coin Flip Result: {result}")
        if result == last_result:
            current_streak += 1
        else:
            current_streak = 1
        last_result = result
    end_time = time.time()  # End timing
    elapsed_time = end_time - start_time
    print(f"Achieved {target_count} {last_result} in a row!")
    print(f"Time taken: {elapsed_time:.2f} seconds")

def calculate_rarity(streak_length):
    probability = 1 / (2 ** streak_length)
    percentage = probability * 100
    print(f"The probability of getting {streak_length} heads or tails in a row is: {percentage:.10f}%")

def run_flips(count):
    for i in range(count):
        result = flip_coin(in_run=True)
        print(f"Flip {i+1}/{count}: {result}")
    print(f"Completed {count} flips.")

def calculate_luck():
    total_flips = history['heads'] + history['tails']
    sim_flips = history['sim_heads'] + history['sim_tails']
    
    if total_flips > 0:
        heads_ratio = (history['heads'] / total_flips) * 100
        print(f"Overall Luck:")
        print(f"  Heads: {heads_ratio:.1f}% | Tails: {100 - heads_ratio:.1f}%")
    else:
        print(f"Overall Luck: No flips yet!")
    
    if sim_flips > 0:
        sim_heads_ratio = (history['sim_heads'] / sim_flips) * 100
        print(f"Sim Luck:")
        print(f"  Heads: {sim_heads_ratio:.1f}% | Tails: {100 - sim_heads_ratio:.1f}%")
    else:
        print(f"Sim Luck: No sim flips yet!")
    
    run_total = history['run_heads'] + history['run_tails']
    if run_total > 0:
        run_heads_ratio = (history['run_heads'] / run_total) * 100
        print(f"Run Luck:")
        print(f"  Heads: {run_heads_ratio:.1f}% | Tails: {100 - run_heads_ratio:.1f}%")
    else:
        print(f"Run Luck: No run flips yet!")

if __name__ == "__main__":
    while True:
        user_input = input("Press Enter to flip and type 'exit' to leave. See more commands by typing 'help': ").strip().lower()
        if user_input == "exit":
            print(f"Exiting the coin flipper. Goodbye!")
            break
        elif user_input.startswith("sim"):
            try:
                target_count = int(user_input.split()[1])
                if target_count <= 0:
                    print("Please enter a positive number for the streak.")
                else:
                    print(f"Starting sim...")
                    history["sim_runs"] += 1
                    spam_until_in_a_row(target_count)
            except (IndexError, ValueError):
                print("Invalid command. Use 'sim <number>' where <number> is a positive integer.")
        elif user_input.startswith("run"):
            try:
                count = int(user_input.split()[1])
                if count <= 0:
                    print("Please enter a positive number for flips.")
                else:
                    history["run_runs"] += 1
                    run_flips(count)
            except (IndexError, ValueError):
                print("Invalid command. Use 'run <number>' where <number> is a positive integer.")
        elif user_input.startswith("calc"):
            try:
                streak_length = int(user_input.split()[1])
                if streak_length <= 0:
                    print("Please enter a positive number for the streak.")
                else:
                    calculate_rarity(streak_length)
            except (IndexError, ValueError):
                print("Invalid command. Use 'calc <number>' where <number> is a positive integer.")
        elif user_input == "reset":
            for key in history:
                history[key] = 0
            os.system("cls" if os.name == "nt" else "clear")
            print(f"Screen cleared. All previous output and history have been reset.")
        elif user_input == "history":
            print(f"Flip history since start:")
            print(f"  Total heads: {history['heads']}")
            print(f"  Total tails: {history['tails']}")
            print(f"Sim-specific flips:")
            print(f"  Heads in sim runs: {history['sim_heads']}")
            print(f"  Tails in sim runs: {history['sim_tails']}")
            print(f"  Total sim runs: {history['sim_runs']}")
            print(f"Run-specific flips:")
            print(f"  Heads in run commands: {history['run_heads']}")
            print(f"  Tails in run commands: {history['run_tails']}")
            print(f"  Total run commands: {history['run_runs']}")
        elif user_input == "luck":
            calculate_luck()
        elif user_input == "help":
            print(f"Available commands:")
            print("  Press Enter to flip the coin.")
            print(f"  Type 'sim <number>' to flip until you get that many heads or tails in a row.")
            print(f"  Type 'run <number>' to run that many flips without a goal.")
            print(f"  Type 'calc <number>' to calculate the probability of getting that many heads or tails in a row.")
            print(f"  Type 'history' to show total heads/tails and sim-specific counts.")
            print(f"  Type 'luck' to see how lucky you've been with flips.")
            print(f"  Type 'reset' to clear the screen and reset output.")
            print(f"  Type 'exit' to leave.")
        elif user_input == "":
            result = flip_coin()
            print(f"Coin Flip Result: {result}")
        else:
            print("Invalid command. Type 'help' to see available commands.")