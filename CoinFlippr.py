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
        print(f"\033[92mCoin Flip Result: {result}\033[0m")
        if result == last_result:
            current_streak += 1
        else:
            current_streak = 1
        last_result = result
    end_time = time.time()  # End timing
    elapsed_time = end_time - start_time
    print(f"\033[92mAchieved {target_count} {last_result} in a row!\033[0m")
    print(f"\033[92mTime taken: {elapsed_time:.2f} seconds\033[0m")

def calculate_rarity(streak_length):
    probability = 1 / (2 ** streak_length)
    percentage = probability * 100
    print(f"The probability of getting {streak_length} heads or tails in a row is: {percentage:.10f}%")

def run_flips(count):
    for i in range(count):
        result = flip_coin(in_run=True)
        print(f"\033[38;5;250mFlip {i+1}/{count}: {result}\033[0m")
    print(f"\033[38;5;250mCompleted {count} flips.\033[0m")

def calculate_luck():
    total_flips = history['heads'] + history['tails']
    sim_flips = history['sim_heads'] + history['sim_tails']
    
    if total_flips > 0:
        heads_ratio = (history['heads'] / total_flips) * 100
        print(f"\033[96mOverall Luck:\033[0m")
        print(f"  Heads: \033[94m{heads_ratio:.1f}%\033[0m | Tails: \033[91m{100 - heads_ratio:.1f}%\033[0m")
    else:
        print(f"\033[96mOverall Luck:\033[0m No flips yet!")
    
    if sim_flips > 0:
        sim_heads_ratio = (history['sim_heads'] / sim_flips) * 100
        print(f"\033[92mSim Luck:\033[0m")
        print(f"  Heads: \033[92m{sim_heads_ratio:.1f}%\033[0m | Tails: \033[92m{100 - sim_heads_ratio:.1f}%\033[0m")
    else:
        print(f"\033[92mSim Luck:\033[0m No sim flips yet!")
    
    run_total = history['run_heads'] + history['run_tails']
    if run_total > 0:
        run_heads_ratio = (history['run_heads'] / run_total) * 100
        print(f"\033[38;5;250mRun Luck:\033[0m")
        print(f"  Heads: \033[38;5;250m{run_heads_ratio:.1f}%\033[0m | Tails: \033[38;5;250m{100 - run_heads_ratio:.1f}%\033[0m")
    else:
        print(f"\033[38;5;250mRun Luck:\033[0m No run flips yet!")

if __name__ == "__main__":
    while True:
        user_input = input("Press Enter to flip and type 'exit' to leave. See more commands by typing 'help': ").strip().lower()
        if user_input == "exit":
            print(f"\033[93mExiting the coin flipper. Goodbye!\033[0m")
            break
        elif user_input.startswith("sim"):
            try:
                target_count = int(user_input.split()[1])
                if target_count <= 0:
                    print("Please enter a positive number for the streak.")
                else:
                    print(f"\033[92mStarting sim...\033[0m")
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
            print(f"\033[93mScreen cleared. All previous output and history have been reset.\033[0m")
        elif user_input == "history":
            print(f"\033[96mFlip history since start:\033[0m")
            print(f"  Total heads: \033[94m{history['heads']}\033[0m")
            print(f"  Total tails: \033[91m{history['tails']}\033[0m")
            print(f"\033[92mSim-specific flips:\033[0m")
            print(f"  Heads in sim runs: \033[92m{history['sim_heads']}\033[0m")
            print(f"  Tails in sim runs: \033[92m{history['sim_tails']}\033[0m")
            print(f"  Total sim runs: \033[92m{history['sim_runs']}\033[0m")
            print(f"\033[94mRun-specific flips:\033[0m")
            print(f"  Heads in run commands: \033[38;5;250m{history['run_heads']}\033[0m")
            print(f"  Tails in run commands: \033[38;5;250m{history['run_tails']}\033[0m")
            print(f"  Total run commands: \033[38;5;250m{history['run_runs']}\033[0m")
        elif user_input == "luck":
            calculate_luck()
        elif user_input == "help":
            print(f"\033[96mAvailable commands:\033[0m")
            print("  Press Enter to flip the coin.")
            print(f"  Type \033[92m'sim <number>'\033[0m to flip until you get that many heads or tails in a row.")
            print(f"  Type \033[38;5;250m'run <number>'\033[0m to run that many flips without a goal.")
            print(f"  Type \033[94m'calc <number>'\033[0m to calculate the probability of getting that many heads or tails in a row.")
            print(f"  Type \033[96m'history'\033[0m to show total heads/tails and sim-specific counts.")
            print(f"  Type \033[95m'luck'\033[0m to see how lucky you've been with flips.")
            print(f"  Type \033[93m'reset'\033[0m to clear the screen and reset output.")
            print(f"  Type \033[91m'exit'\033[0m to leave.")
        elif user_input == "":
            result = flip_coin()
            print(f"Coin Flip Result: \033[94m{result}\033[0m" if result == 'Heads' else f"Coin Flip Result: \033[91m{result}\033[0m")
        else:
            print("Invalid command. Type 'help' to see available commands.")