from flask import Flask, request

appFlask = Flask(__name__)

@appFlask.route('/notifications', methods=['POST'])
def json_example():
    request_data = request.get_json()
    content_type = request.headers.get('Content-Type')
    return '''

Data Send: {}'''.format(request_data, content_type)

if __name__ == '__main__':
    appFlask.run(debug = True)