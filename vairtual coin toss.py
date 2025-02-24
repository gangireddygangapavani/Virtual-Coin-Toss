import random

def coin_toss():
    return random.choice(["Heads", "Tails"])

def simulate_tosses():
    while True:
        try:
            num_tosses = int(input("Enter the number of times to flip the coin: "))
            if num_tosses <= 0:
                print("Please enter a positive integer.\n")
                continue
        except ValueError:
            print("Invalid input. Please enter a number.\n")
            continue
        
        results = {"Heads": 0, "Tails": 0}
        
        for _ in range(num_tosses):
            result = coin_toss()
            results[result] += 1
            print(f"Result: {result}")
        
        total = num_tosses
        heads_percentage = (results["Heads"] / total) * 100
        tails_percentage = (results["Tails"] / total) * 100
        
        print("\n--- Toss Summary ---")
        print(f"Heads: {results['Heads']} ({heads_percentage:.2f}%)")
        print(f"Tails: {results['Tails']} ({tails_percentage:.2f}%)\n")
        
        restart = input("Do you want to flip again? (yes/no): ").strip().lower()
        if restart != "yes":
            print("Thank you for using the Virtual Coin Toss! Goodbye.")
            break

if __name__ == "__main__":
    simulate_tosses()



