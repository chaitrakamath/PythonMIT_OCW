#File Name: ps4.py
#Author: Chaitra Kothari
#Date: Oct 30th, 2015
#Description: This problem set will introduce you to using successive approximation, as well as data structures such as tuples and lists.


#==============================================Problem1=============================
def nestEggFixed(salary, save, growthRate, years):
    """
    - salary: the amount of money you make each year.
    - save: the percent of your salary to save in the investment account each
      year (an integer between 0 and 100).
    - growthRate: the annual percent increase in your investment account (an
      integer between 0 and 100).
    - years: the number of years to work.
    - return: a list whose values are the size of your retirement account at
      the end of each year.
    """
    retirementFund = []
    retirementFund.append(salary * save * 0.01)
    for numYear in range(1, years):
        curYearSavings = retirementFund[numYear - 1] * (1 + 0.01 * growthRate) + salary * save * 0.01
        retirementFund.append(curYearSavings)
    return retirementFund  



def testNestEggFixed():
    salary     = 10000
    save       = 10
    growthRate = 15
    years      = 5
    savingsRecord = nestEggFixed(salary, save, growthRate, years)
    print savingsRecord
    # Output should have values close to:
    # [1000.0, 2150.0, 3472.5, 4993.375, 6742.3812499999995]

    raw_input()

    salary     = 20000
    save       = 20
    growthRate = 7
    years      = 40
    savingsRecord = nestEggFixed(salary, save, growthRate, years)
    print savingsRecord
    
#==============================================Problem2=============================
def nestEggVariable(salary, save, growthRates):
    """
    - salary: the amount of money you make each year.
    - save: the percent of your salary to save in the investment account each
      year (an integer between 0 and 100).
    - growthRate: a list of the annual percent increases in your investment
      account (integers between 0 and 100).
    - return: a list of your retirement account value at the end of each year.
    """
    retirementFund = []
    retirementFund.append(salary * save * 0.01)
    for numYear in range(1, len(growthRates)):
        curYearSavings = retirementFund[numYear - 1] * (1 + 0.01 * growthRates[numYear]) + salary * save * 0.01
        retirementFund.append(curYearSavings)
    return retirementFund  

def testNestEggVariable():
    salary      = 10000
    save        = 10
    growthRates = [3, 4, 5, 0, 3]
    savingsRecord = nestEggVariable(salary, save, growthRates)
    print savingsRecord
    # Output should have values close to:
    # [1000.0, 2040.0, 3142.0, 4142.0, 5266.2600000000002]
    raw_input()
    salary = 20000
    save = 20
    growthRates = [6, 4, 3, 9, 2, 7, 8, 5, 1]
    savingsRecord = nestEggVariable(salary, save, growthRates)
    print savingsRecord
#==============================================Problem3=============================
def postRetirement(savings, growthRates, expenses):
    """
    - savings: the initial amount of money in your savings account.
    - growthRate: a list of the annual percent increases in your investment
      account (an integer between 0 and 100).
    - expenses: the amount of money you plan to spend each year during
      retirement.
    - return: a list of your retirement account value at the end of each year.
    """
    retirementFundVal = []
    retirementFundVal.append(savings * (1 + 0.01 * growthRates[0]) - expenses)
    for year in range(1, len(growthRates)):
        curYearValue = retirementFundVal[year - 1] * (1 + 0.01 * growthRates[year]) - expenses
        retirementFundVal.append(curYearValue)
    return retirementFundVal

def testPostRetirement():
    savings     = 100000
    growthRates = [10, 5, 0, 5, 1]
    expenses    = 30000
    savingsRecord = postRetirement(savings, growthRates, expenses)
    print savingsRecord
    # Output should have values close to:
    # [80000.000000000015, 54000.000000000015, 24000.000000000015,
    # -4799.9999999999854, -34847.999999999985]

    raw_input()

    savings = 10000000
    growthRates = [2, 3, 6, 8, 10, 1, 3, 4]
    expenses = 30000
    savingsRecord = postRetirement(savings, growthRates, expenses)
    print savingsRecord


#==============================================Problem4=============================
def findMaxExpenses(salary, save, preRetireGrowthRates, postRetireGrowthRates,
                    epsilon):
    """
    - salary: the amount of money you make each year.
    - save: the percent of your salary to save in the investment account each
      year (an integer between 0 and 100).
    - preRetireGrowthRates: a list of annual growth percentages on investments
      while you are still working.
    - postRetireGrowthRates: a list of annual growth percentages on investments
      while you are retired.
    - epsilon: an upper bound on the absolute value of the amount remaining in
      the investment fund at the end of retirement.
    """
    savings = nestEggVariable(salary, save, preRetireGrowthRates)[-1]
    print savings
    minExp = 0
    maxExp = savings
    monthlyExp = (minExp + maxExp) / 2.0

    yearlyValue = postRetirement(savings, postRetireGrowthRates, monthlyExp)
    while yearlyValue[-1] < 0 or yearlyValue[-1] > epsilon:
        if yearlyValue[-1] < 0: #too high monthly exp, alter maxExp
            maxExp = monthlyExp
        else:
            minExp = monthlyExp
        monthlyExp = (minExp + maxExp) / 2.0
        yearlyValue = postRetirement(savings, postRetireGrowthRates, monthlyExp)
        print 'new monthly expense guess:', monthlyExp
        print 'new yearly value:', yearlyValue 
        print      
    return monthlyExp



def testFindMaxExpenses():
    salary                = 10000
    save                  = 10
    preRetireGrowthRates  = [3, 4, 5, 0, 3]
    postRetireGrowthRates = [10, 5, 0, 5, 1]
    epsilon               = .01
    expenses = findMaxExpenses(salary, save, preRetireGrowthRates,
                               postRetireGrowthRates, epsilon)
    print expenses
    # Output should have a value close to:
    # 1229.95548986

    # TODO: Add more test cases here.
