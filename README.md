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
of a portfolio comprised of a combination of these two stocks (for example, 70% AAPL and 30% FNTL)
between Jan 1st, 2025, and Dec 31st, 2025.

Prices are read from a csv called `stock_prices.csv`. They're simulated, but they look kind of real.

The csv can be
found [here](https://github.com/EnriqueOrtiz27/fintual-application/blob/main/infrastructure/stock_prices.csv).

![image](images/stock_prices.png)

## How to test it in 10 seconds

### JSON Body Guidelines

The JSON body of your request must fulfill the following criteria:

* `start_date` and `end_date` must be in `YYYY-MM-DD` format
* `start_date` and `end_date` must be between `2025-01-01` and `2025-12-31`
    * If `start_date` > `end_date`, we'll switch them up for you.
* `allocations` is an object that must fulfill the following criteria:
    * It must have at least one element
    * The keys must be either `AAPL` or `FNTL`
    * The weights must be integers (so that you can do QA more easily)
    * The weights must add to `100`

## How to test it in more than 10 seconds but less than 10 years

# Appendix

### How this API works

![image](images/how_it_works.png)

### Doing QA

I recorded a video of me doing some QA, you can watch
it [here](https://www.loom.com/share/4d8b430e053448f2977967d03f740614?sid=94e16037-8f0d-4cf2-a7cb-29206759cdbd).

### Final checklist

* reread instructions, make sure I follow all of them
* run new env dockerfile
* add unit tests
* API -> Deploy GCP

### First week's prices

In case it helps you do QA more easily. The entire list
is [here](https://github.com/EnriqueOrtiz27/fintual-application/blob/main/infrastructure/stock_prices.csv).

![image](/images/first_week.png)
