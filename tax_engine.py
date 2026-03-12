#courthouse, clarendon, virginia square, crystal city, pentagon city, ballston

#first focus on tax calculator definition function

def estimate_total_tax(income, state, county, filing_status = "single"):

  federal = federal_tax(income, filing_status)
  state_tax_amount = state_tax(income, state)
  local = local_tax(income, state, county)
  payroll = payroll_tax(income)

  sales = estimated_sales_tax(income, state, county)
  property_tax = estimated_property_tax(income, county)

  total = federal + state_tax_amount + local + payroll + sales + property_tax

  return {
      "federal": federal,
      "state": state_tax_amount,
      "local": local,
      "payroll": payroll,
      "sales": sales,
      "property": property_tax,
      "total": total,
      "effective rate": total/income,
      "leftover": income - total
  }

#federal tax function

def federal_tax(income, filing_status = "single"):
    brackets = [
        (11600, 0.1),
        (47150, 0.12),
        (100525, 0.22),
        (191950, 0.24),
        (243725, 0.32),
        (609350, 0.35),
        (float("inf"), 0.37)
      ]
#calculates progressive tax system
    tax = 0
    prev = 0

    for limit, rate in brackets:
      if income > limit:
          tax +=(limit - prev)*rate
          prev = limit
      else:
          tax += (income - prev)*rate
          break

    return tax

#payroll tax (ss and medicare tax)(FICA~ federal insurance contributions act)

def payroll_tax(income):
    ss_cap = 168600
    ss_tax = min(income, ss_cap)*0.062

    medicare = income*0.0145

    return ss_tax + medicare

#state tax

def state_tax(income, state):

  brackets = state_tax_brackets.get(state, [])

  if brackets == []:
    return 0

  tax = 0
  prev = 0

  for limit, rate in brackets:
    if income > limit:
      tax +=(limit - prev)*rate
      prev = limit

    else:
      tax += (income - prev)*rate
      break

  return tax


#state tax, progressive state tax system, later add csv instead of hard code

state_tax_brackets = {
    "VA": [
        (3000, 0.02),
        (5000, 0.03),
        (17000, 0.05),
        (float("inf"), 0.0575)
    ],

    "TX": []
}


#sales tax
sales_tax_rates = {
    "VA": 0.06, 
    "TX": 0.0625
}

def estimated_sales_tax(income, state, county):
    rate = sales_tax_rates.get(state, 0.05)

    #assuming 30% of income is spent on taxable goods
    taxable_spending = income*0.30

    return taxable_spending *rate 
  #define local tax 

local_tax_rates = {
    ("VA", "Arlington"): 0.00, 
    ("VA", "Fairfax"): 0.00,
    ("VA", "Loudoun"): 0.00, 
    ("VA", "Alexandria"): 0.00, 
    ("VA", "Prince William"), 0.00               
}

def local_tax(income, state, county):
    rate = local_tax_rates.get((state, county), 0)

    return income*rate
  #property tax 

#dictionary
property_tax_rates = {
    "Arlington": 0.0103, 
    "Fairfax": 0.0111, 
    "Loudoun": 0.00875, 
    "Prince William": 0.00966,
    "Alexandria": 0.0135
}


#function
def estimated_property_tax(income, county):
    rate = property_tax_rates.get(county, 0.01)

    #assuming home value ~ 4*income
    home_value = income*4

    return home_value *rate

#example estimate_total_tax(90000, "VA", "Fairfax", "Single)



