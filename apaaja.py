from flask import Flask, redirect, render_template, request, url_for
from DB_OP import add_contact, get_pesan, update_pesan, delete_pesan, get_last_pesan, get_all_pesan

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('PertanianMain.html')

@app.route('/konten')
def konten():
    return render_template('content.html')

@app.route('/kontak')
def kontak():
    last_pesan = get_last_pesan()
    pesan_list = get_all_pesan()
    print(pesan_list)
    return render_template('kontak.html', last_pesan = last_pesan, pesan_list = pesan_list)

@app.route('/TentangKami')
def tentang():
    return render_template('TentangKami.html')

@app.route('/add_text', methods=["POST","GET"])
def addtext():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["pesan"]
        add_contact(name, email, message)
        return redirect(url_for('kontak'))
    return render_template('kontak.html')

@app.route('/update_pesan', methods=["POST", "GET"])
def update_pesan_route():
    if request.method == "POST":
        id = request.form["id"]
        name = request.form["name"]
        email = request.form["email"]
        pesan = request.form["pesan"]
        update_pesan(id, name, email, pesan)
        return redirect(url_for('kontak'))
    id_value = request.args.get('id')
    pesan = get_pesan(id_value)
    return render_template('update_pesan.html', pesan=pesan)

@app.route('/delete_pesan', methods=["POST"])
def delete_pesan_route():
    id = request.form["id"]
    delete_pesan(id)
    return redirect(url_for('kontak'))

if __name__ == '__main__':
    app.run(debug=True)