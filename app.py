from flask import abort, Flask, request, Response

SECRET = 'fictional-spoon-crispy-waffle'

app = Flask(__name__)


@app.route('/hook', methods=['OPTIONS'])
def subscribe():
    secret = request.args.get('secret')
    if not secret:
        abort(401)

    if secret != SECRET:
        abort(403)

    headers = {
        'allow': 'OPTIONS, POST',
        'WebHook-Allowed-Origin': '*',
        'WebHook-Allowed-Rate': 100,
    }

    return Response(headers=headers)


@app.route('/hook', methods=['POST'])
def process():
    secret = request.args.get('secret')
    if not secret:
        abort(401)

    if secret != SECRET:
        abort(403)

    full_request = (
        f'{request.method} {request.url}\n'
        f'{request.headers}\n'
        f'{request.data}'
    )

    print('---------------------------')
    print(full_request)
    print('---------------------------')

    return Response()
