
import pandas as pd
import json

def lambda_handler(event, context):
    d={'col1':[1,2],'col2':[3,4]}

    df=pd.DataFrame(data=d)
    print(df)

    print('Done X.1')
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
