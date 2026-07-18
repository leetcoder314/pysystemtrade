import sys
from systems.provided.futures_chapter15.basesystem import futures_system

def main():
    system = futures_system()
    port = system.accounts.portfolio()

    with open("yearly_returns.txt", "w") as f:
        f.write("Yearly Returns:\n")
        f.write(str(port.percent.annual) + "\n")
        f.write("\nAnnualised Sharpe Ratio: " + str(port.percent.sharpe()) + "\n")

        explanation = """
Explanation for crazy drawdowns:
These drawdowns (1987, 1994, 2006, 2020) are associated with major market crash events:
- 1987: Black Monday (Oct 19, 1987) where stock markets globally crashed. The trend following (ewmac) and carry strategies likely suffered from sudden, massive reversals and volatility spikes.
- 1994: The 1994 bond market crash (or Great Bond Massacre). A sudden drop in bond prices due to unexpected Fed interest rate hikes. This would heavily impact the fixed income/rates instruments (e.g. US10, SOFR/EDOLLAR) configured in this portfolio.
- 2006: Likely pre-crisis turbulence or specific commodities/emerging markets corrections affecting MXP or CORN, or early signs of the subprime mortgage crisis affecting liquidity.
- 2020: The COVID-19 pandemic crash in March 2020. This caused a massive, sudden global equity sell-off, spiking V2X (volatility) and crashing EUROSTX (equities), causing severe losses for trend-following systems caught on the wrong side of the sudden reversal.

A common underlying factor for these is sudden, systemic volatility shocks or "black swan" events causing sharp trend reversals which trend-following strategies (like ewmac) are inherently vulnerable to, as they are positioned for trend continuation and get caught out before they can adjust.

How to mitigate these drawdowns:
1. Faster Trend Signals: Incorporating faster moving averages can help the system react to sudden reversals more quickly, though this can increase trading costs (whipsawing).
2. Volatility Scaling and Capping: Dynamically scaling down position sizes as soon as volatility spikes, or capping the maximum position size / forecast size allowed.
3. Diversifying with Non-Trend Strategies: Adding mean-reversion, carry, or long volatility/options overlays that thrive in high-volatility environments can offset the losses from trend-following components during black swans.
4. Stop Losses: Implementing strict portfolio-level or instrument-level stop losses to exit trades when a significant crash event begins.
"""
        f.write("\n" + explanation + "\n")
    print("Done generating output stats.")

if __name__ == "__main__":
    main()
