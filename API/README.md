# API Created for SBA Loan Risk Analyis Project

## Information
This API was created as part of our project [here](https://github.com/MatthewHolsten/sba-loan-risk-analysis).

## Instructions

Replace the X's in the following URL with the associated inputs below:
>https://matthewholsten.pythonanywhere.com/api/sba-loan-risk-analysis/query/?loan_amt=X&sba_loan_amt=X&sba_prop=X&term=X&jobs=X&ind_code=X&state=X&model=X&admin=d&density=X&recession=X


### Inputs
\
**loan_amt**:       the total requested loan amount in USD (positive integer)\
**sba_loan_amt**:   the total guaranty from the SBA in USD (positive integer)\
**sba_prop**:       proportion of the loan_amt that the sba guarantees, values need not match (float)\
**term**:           loan payback length in months (positive integer)\
**jobs**:           total jobs retained from loan (positive integer)\
**ind_code**:       first two digits of NAICS industry code (9 < positve integer < 100)\
**state**:          2-Letter state abbreviation of loan location (string)\
**model**:          neural-net model to use, state abbreviation or "country" (string) NOTE: currently just "country" is available.\
**admin**:          political party of US president in office ('d' or 'r')\
**density**:        population density ('urban', 'rural', or 'undefined')\
**recession**:      whether or not loan is during recession ('true' or 'false')

##### Example input: 
> https://matthewholsten.pythonanywhere.com/api/sba-loan-risk-analysis/query/?loan_amt=845000&sba_loan_amt=169000&sba_prop=0.2&term=27&jobs=227&ind_code=37&state=RI&model=country&admin=d&density=undefined&recession=false

### Outputs
A nicely JSON string will be returned with the following fields...\
\
• The values of all of the above inputs in "**fields**".\
• A list of field names which had invalid input in "**invalid_fields**." These must be
    corrected in order to run the neural network on the input. Empty list implies no input errors.\
• The ouput of the neural network with the above inputs in "**output**", where 0 indicates
    a "high risk loan", 1 indicates a "low risk loan", and -1 indicates an error processing
    the request.\
• The output as described above written as a string phrase in "**output_phrase**".\

##### Example output (corresponding to above example input):
> {"fields":{"admin":"r","density":"rural","ind_code":"474","jobs":"176","loan_amt":"509000","model":"country","recession":"false","sba_loan_amt":"122160","sba_prop":"0.24","state":"SC","term":"99"},"invalid_fields":[],"output":"1"}
