import json
import inflect

p = inflect.engine()

def lambda_handler(event, context):
    # TODO implement
    word = "birds"
    word = p.singular_noun(word)
    return {
        'statusCode': 200,
        'body': json.dumps(word)
    }
