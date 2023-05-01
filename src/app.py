from flask import Flask, render_template, request, abort, jsonify
import json
from utils import load_data, refactor_url_for_key, compare_json_md5_hash, json_md5_hash

app = Flask(__name__)

DATA_PATH = "./wiki-data/data.json"
wiki_data = load_data(DATA_PATH)


@app.route('/')
def index():
    return render_template("index.html")


@app.route("/updateData", methods=["POST"])
def update_data():
    global wiki_data
    if request.is_json:
        data = request.get_json(silent=True)
        print(data)
        if data:
            if not compare_json_md5_hash(data, DATA_PATH):
                with open(DATA_PATH, "w") as file:
                    json.dump(data, file)
                wiki_data = load_data(DATA_PATH)
    return jsonify({"status": 200})


@app.route("/version", methods=["GET"])
def version():
    json_hash = json_md5_hash(wiki_data)
    return jsonify({"hash": json_hash}), 200


@app.route("/<classname>_<equipment>", methods=["GET"])
def class_equipments(classname, equipment):
    allowed_classes = ["warrior", "archer", "wizard", "cowboy"]
    allowed_equipments = ["weapons", "helmets", "armor", "pants", "shoes"]
    if classname.lower() not in allowed_classes:
        return abort(404)
    if equipment.lower() not in allowed_equipments:
        return abort(404)
    # title is the same as the key for the JSON wiki data
    title = refactor_url_for_key(request.url.split("/")[-1])
    try:
        return render_template("equipment.html", items=wiki_data[title][1:], title=title, headers=wiki_data[title][0])
    except KeyError:
        return abort(500)


if __name__ == '__main__':
    app.run()
