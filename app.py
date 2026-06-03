from flask import Flask, request, jsonify, render_template
import json
import os

app = Flask(__name__)
pastaDiretorio = "arquivos"
bibliotecaArq = "biblioteca.json"
caminhoArquivo = os.path.join(pastaDiretorio, bibliotecaArq)

def inicializar_diretorio():
    if not os.path.exists(pastaDiretorio):
        os.makedirs(pastaDiretorio)

def carregar_biblioteca():
    with open(caminhoArquivo, "r", encoding="utf-8") as f:
        return json.load(f)

def salvar_biblioteca(dados):
    with open(caminhoArquivo, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)

@app.route("/")
def home():
    return jsonify({"mensagem": "API da Biblioteca funcionando!"})


@app.route("/biblioteca", methods=["GET", "POST"])
@app.route("/biblioteca/<isbn>", methods=["GET", "PUT", "DELETE"])
def manipular_livros(isbn=None):
    livros = carregar_biblioteca()

    match request.method:

        case "GET":
            if isbn:
                for livro in livros:
                    if livro["isbn"] == isbn:
                        return jsonify(livro)

                return jsonify({"mensagem": "livro não localizado"}), 404

            return render_template("biblioteca.html", livros=livros)

        case "POST":
            novo_livro = request.get_json()

            if not novo_livro:
                return jsonify({"mensagem": "dados inválidos"}), 400

            for livro in livros:
                if livro["isbn"] == novo_livro["isbn"]:
                    return jsonify({"mensagem": "erro: isbn já existe"}), 400

            livros.append(novo_livro)
            salvar_biblioteca(livros)

            return jsonify({"mensagem": "livro criado com sucesso"}), 201

        case "DELETE":
            for livro in livros:
                if livro["isbn"] == isbn:
                    livros.remove(livro)
                    salvar_biblioteca(livros)

                    return jsonify(
                        {"mensagem": "livro deletado com sucesso"}
                    ), 200

            return jsonify({"mensagem": "livro não localizado"}), 404

        case "PUT":
            livro_atualizado = request.get_json()

            if not livro_atualizado:
                return jsonify({"mensagem": "dados inválidos"}), 400

            for livro in livros:
                if livro["isbn"] == isbn:
                    livro.update(livro_atualizado)

                    salvar_biblioteca(livros)

                    return jsonify(
                        {"mensagem": "livro atualizado com sucesso"}
                    ), 200

            return jsonify({"mensagem": "livro não localizado"}), 404


# ==================================================================================================== 

if __name__ == "__main__":
    inicializar_diretorio()
    app.run(debug=True)

