from flask import Flask, request
# from flask_sqlalchemy import SQLAlchemy
import nn_model as nn

app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
# db = SQLAlchemy(app)


''' QUERIES '''
@app.route('/')
def index():
    return 'Hello!'

@app.route('/query/models/<model>/')
def parse_url_full(model):

    fields = request.args.to_dict()
    fields['model'] = model
    return handle_query(fields)

@app.route('/query/models/<model>/random')
def parse_url_full_random(model):
    fields = get_random_sample_fields(model)
    return handle_query(fields)



''' FUNCTIONS '''
def handle_query(fields):
    invalid_fields = validate_fields(fields)

    for _, v in invalid_fields.items():
        if v != 0:
            return response_obj(fields=fields, invalid_fields=invalid_fields)

    sample = format_fields(fields)
    output = query_model(fields, sample, 'country')
    return {'output': output}
    # return response_obj(fields=fields, output=output)

def query_model(fields, sample, model):
    return nn.query_nn(sample, model)

def validate_fields(fields):

    invalid_fields = {k: 0 for k in fields}
    print("init invalid_fields")

    error_msg = {
        'model': '      model error message',
        'loan_amt':     'loan_amt error message',
        'sba_loan_amt': 'sba_loan_amt error message',
        'sba_prop':     'sba_prop error message',
        'term':         'term error message',
        'jobs':         'jobs error message',
        'state':        'state error message',
        'urban':        'urban error message',
        'admin':        'admin error message',
        'recession':    'recession error message'
    }

    # invalid_fields['term'] = error_msg['term']

    #loan_amt
    # if isinstance(fields['loan_amt'], int):
    #     if fields['loan_amt'] < 0:
    #         invalid_fields['loan_amt'] = error_msg['loan_amt']
    # else:
    #     invalid_fields['loan_amt'] = error_msg['loan_amt']
    #
    # #sba_loan_amt
    # if isinstance(fields['sba_loan_amt'], int):
    #     if fields['sba_loan_amt'] < 0:
    #         invalid_fields['sba_loan_amt'] = error_msg['sba_loan_amt']
    # else:
    #     invalid_fields['sba_loan_amt'] = error_msg['sba_loan_amt']
    #
    # #sba_prop
    # if isinstance(fields['sba_prop'], float):
    #     if fields['sba_prop'] < 0 or fields['sba_prop'] > 0:
    #         invalid_fields['sba_prop'] = error_msg['sba_prop']
    # else:
    #     invalid_fields['sba_prop'] = error_msg['sba_prop']



    return invalid_fields

def format_fields(fields):

    states = {
        'AK': 1, 'AL': 2, 'AR': 3, 'AZ': 4,
        'CA': 5, 'CO': 6, 'CT': 7, 'DC': 8,
        'DE': 9, 'FL': 10, 'GA': 11, 'HI': 12,
        'IA': 13, 'ID': 14, 'IL': 15, 'IN': 16,
        'KS': 17, 'KY': 18, 'LA': 19, 'MA': 20,
        'MD': 21, 'ME': 22, 'MI': 23, 'MN': 24,
        'MO': 25, 'MS': 26, 'MT': 27, 'NC': 28,
        'ND': 29, 'NE': 30, 'NH': 31, 'NJ': 32,
        'NM': 33, 'NV': 34, 'NY': 35, 'OH': 36,
        'OK': 37, 'OR': 38, 'PA': 39, 'RI': 40,
        'SC': 41, 'SD': 42, 'TN': 43, 'TX': 44,
        'UT': 45, 'VA': 46, 'VT': 47, 'WA': 48,
        'WI': 49, 'WV': 50, 'WY': 51
    }

    re_backed = int(int(fields['term']) >= 240)
    admin = {'D': 0, 'R': 1}[fields['admin']] #TODO check which is whick for admin

    sample = [
        fields['ind_code'],
        fields['loan_amt'],
        re_backed,
        fields['recession'],
        fields['sba_loan_amt'],
        admin,
        fields['sba_prop'],
        fields['urban'],
        fields['jobs'],
        fields['term'],
        states[fields['state']]
    ]

    return sample

def response_obj(fields = {}, invalid_fields = [], output = -1):
    return {
        'fields': fields,
        'invalid_fields': invalid_fields,
        'output': output
    }

#TODO retrieve actual sample
def get_random_sample_fields(model):
        fields = {
            'model':        model,
            'loan_amt':     1000000,
            'sba_loan_amt': 500000,
            'sba_prop':     0.6,
            'term':         250,
            'jobs':         500,
            'ind_code':     44,
            'state':        'VA',
            'urban':        1,
            'admin':        'R',
            'recession':    1,
        }
        return fields

def test_query(id):
    sample_0 = [44, 100000000000, 1, 1, 0, 1, 0.0001, 1, 200, 120, 36]
    sample_1 = [ 44, 100000, 10000, 1, 0, 1, 0.9, 1, 200, 120, 36]

    sample = sample_1 if id == 1 else sample_0
    output = 1
    output = nn.query_nn(sample)

    return {'result': output}

if __name__ == '__main__':
    app.run()
