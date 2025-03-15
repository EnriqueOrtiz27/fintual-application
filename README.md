* pending how to run
* pending requirements!
* review annualized return formula + create unit tests
    * format with Black

# Introduction

These are the instructions provided by Fintual to apply for
the [Sr. Backend Engineer](https://jobs.lever.co/fintual/26c5379b-4dbc-4ed9-a58e-a1bed26869b0) role:


> Construct a simple Portfolio class that has a collection of Stocks and a "Profit" method that receives 2 dates
> and returns the profit of the Portfolio between those dates. Assume each Stock has a "Price" method that receives a
> date
> and returns its price.
>
> Bonus Track: make the Profit method return the "annualized return" of the portfolio between the given dates.

## How it Works

We have 3 main entities: `Portfolios`, `Allocations`, and `Stocks`.

![image](images/entities.png)

For simplicity, there are only two stocks, `AAPL` (Apple) and `FNTL` (Fintual - too soon?).

I built a simple API with a single endpoint that allows you to compute the profits
of a portfolio comprised of a combination of these two stocks (for example, 70% AAPL and 30% FNTL, or a 100% FNTL
#Believe)
between Jan 1st, 2025, and Dec 31st, 2025 (yes, I can predict the future).

![image](images/how_it_works.png)

Prices are read from a csv called `stock_prices.csv`. They're fake, but they look kind of real.

![image](images/stock_prices.png)

## How to test it in 10 seconds

## How to test it in more than 10 seconds but less than 10 years

## Further Improvements

* Don't hardcode the price - look for it in the DB.
* Add more unit tests
* add cool price image
* Add pydantic validators to ensure allocations sum 100

### Note to Self

* add loom - make it turbo clear

## Bonus Track - How devs are expected to do QA at Palenca

You guys included a Bonus track, I want to include one too. 

