from flask import Flask, request, json, make_response
import Connection as conn
import MedicamentosDAO as med

app = Flask(__name__)
@app.route('/', methods=['POST'])

def weebhook():
    req = request.get_json(silent=True, force=True)
    print('Request: ')
    print(json.dumps(req, indent=4))
    res = makeWebhookResult(req)
    res = json.dumps(res, indent=4)
    print (res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

def makeWebhookResult(req):
    if req.get('queryResult').get('action') != 'Dosagem':
        return {}
    result = req.get('queryResult')
    parameters = result.get('parameters')
    msg = result.get('fulfillmentMessages')
    if msg:
        verificaErro = "\n".join(map(lambda erros: ' '.join(erros.get('text').get('text')), msg))
    # else :
    #     verificaErro = ""
    nameMed = parameters.get('NomeMedicamento')
    nameDosagem = parameters.get('DosagemMedicamento')
    tipoDosagem = parameters.get('TipoDosagemMedicamento')
    # med.save(nameMed, nameDosagem, tipoDosagem, 1)
    if msg and verificaErro != "":
        speech = verificaErro
    else:
        speech = 'Aplicado ' + str(nameDosagem) + str(tipoDosagem) + ' de ' + str(nameMed.title())

    print ('Response: ')
    print(speech)
    return {
        'fulfillmentText' : speech,
        'source' : 'Dr.Farmer'
    }

if __name__ == '__main__':
    app.run(debug=True, port=80, threaded=True, host='0.0.0.0')