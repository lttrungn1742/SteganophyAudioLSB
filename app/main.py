from flask import Flask, render_template, request, send_from_directory, redirect
import os
import stegano 

app = Flask(__name__)

@app.route('/static/<path:path>')
def send_report(path):
    return send_from_directory('static', path)

@app.route('/')
def index():
    return render_template('index.html',result_encrypt=None, result_decrypt=None)

@app.route('/encrypt', methods=['POST', 'GET'])
def encrypt():
    if request.method == 'GET':
        return redirect('/')
    file = request.files['file'] or None
    message = request.form['message'] or None

    if file == None:
        return render_template('index.html', result_decrypt=None,result_encrypt="Miss file")
    elif message == None:
        return render_template('index.html', result_decrypt=None,result_encrypt='Miss message')


    file_in_dir = f"./static/in/{os.urandom(10).hex()}{file.filename}"
    file.save(file_in_dir)
    outfile = "./static/out/%s"%(file.filename)

    result = stegano.encrypt(file_in_dir,outfile,message)
    if result == "Success":
        return render_template('index.html', result_decrypt=None,result_encrypt=result, fileDownload=outfile)

    return render_template('index.html', result_decrypt=None,result_encrypt=result)

@app.route('/decrypt', methods=['POST', 'GET'])
def decrypt():
    if request.method == 'GET':
        return redirect('/')
    file = request.files['file'] or None

    if file == None:
        return render_template('index.html', result_decrypt="Miss file")

    file_in_dir = f"./static/in/{os.urandom(10).hex()}{file.filename}"
    file.save(file_in_dir)

    result = stegano.decrypt(file_in_dir)
    
    return render_template('index.html', result_decrypt=result)

if __name__=="__main__":
    app.run('0.0.0.0',8080, True)