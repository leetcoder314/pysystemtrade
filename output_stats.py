import sys
from systems.provided.futures_chapter15.basesystem import futures_system

def main():
    system = futures_system()
    port = system.accounts.portfolio()

    with open("yearly_returns.txt", "w") as f:
        f.write("Yearly Returns:\n")
        f.write(str(port.percent.annual) + "\n")
        f.write("\nAnnualised Sharpe Ratio: " + str(port.percent.sharpe()) + "\n")
    print("Done generating output stats.")

if __name__ == "__main__":
    main()
