# API Created for SBA Loan Risk Analyis

##Information
This API was created as part of our project [here]{https://github.com/MatthewHolsten/sba-loan-risk-analysis}.

##Instructions
"https://matthewholsten.pythonanywhere.com/query/models/country/&loan_amt=X\
&sba_loan_amt=X&sba_prop=X&term=X&jobs=X&ind_code=X&state=X&admin=X&density=X&recession=X"

### Inputs
>model:          neural-net model to use, state abbreviation or "country" (string) NOTE: currently just "country" is available.\
loan_amt:       the total requested loan amount in USD (positive integer)\
sba_loan_amt:   the total guaranty from the SBA in USD (positive integer)\
sba_prop:       proportion of the loan_amt that the sba guarantees, values need not match (float)\
term:           loan payback length in months (positive integer)\
jobs:           total jobs retained from loan (positive integer)\
ind_code:       first two digits of NAICS industry code (9 < positve integer < 100)\
admin:          political party of US president in office ('d' or 'r')\
density:        population density ('urban', 'rural', or 'undefined')\
recession:      whether or not loan is during recession ('true' or 'false')\

### Outputs
>A nicely formatted JSON string will be returned with...\
• The URL recieved.\
• The values of all of the above inputs in "fields".\
• A list of field names which had invalid input in "invalid_fields." These must be
    corrected in order to run the neural network on the input.\
• The ouput of the neural network with the above inputs in "output" where 0 indicates
    a "high risk loan" and 1 indicates a "low risk loan" and -1 indicates an error processing
    the request.\
• The output as a string phrase in "output_phrase".\

