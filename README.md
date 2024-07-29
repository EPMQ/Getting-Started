# Artificial Intelligence Project

A financial institution hired you, a Data Analyst, to help them analyze their data and create a report. One of their business consists of issuing credit to customers, e.g. to buy a house. In this context, they gathered a database of 1.000 customers and the credit granted from a german bank. Each database entry refers to one credit grant and contains the following information:

- Status of existing checking account
- Duration (in months)
- Credit history
- Purpose
- Credit amount
- Savings account/bonds
- Present employment since
- Installment rate in percentage of disposable income
- Personal status and sex
- Other debtors / guarantors
- Present residence since
- Property
- Age (in years)
- Other installment plans
- Housing
- Number of existing credits at this bank
- Job
- Number of people being liable to provide maintenance for
- Telephone
- Foreign worker
- Risk (1 = good, 2 = bad)

More information is available at [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/144/statlog+german+credit+data). The goal is to first predict the client's risk based on the other atributes and then predict the amount of credit requested based on the other atributes, except "risk".

To evaluate the results of the risk prediction and build the report, consider the following profit and cost matrix:

| actual / predicted  |    1 |    2 |
| :-----------------: |  :-- |  :-- |
|   1                 |   0  | -200 |
|   2                 | -200 |  100 |

To evaluate the results of the amount of credit requested prediction, consider the folling profit function:

f = 100 * ( |Y - P| / Y < 0.3 )

where Y is the desired and P is the predicted amount of credit requested. The function assigns 100$ for a correct prediction with a margin of 30% to the value of Y.

Finally, to enrich the report, apply explainable AI techniques to the model to illustrate the importance of each atribute to the institution.
