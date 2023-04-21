from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route("/warrior_weapons")
def warrior_weapons():
    # TODO: load items via DB or xlsx file
    # TODO: give items their own class
    items = [
        {
            "name": "Stick",
            "power": "1",
            "level": "1",
            "buying_price": "N/A",
            "selling_price": "1 (?)",
            "description": "A plain stick for hitting things.",
            "merchant": "Sales Man (Training Grounds)",
            "mob_drops": "Green Squish",
            "two_handed": "No"
        },
        {
            "name": "Red Plastic Sword",
            "power": "4",
            "level": "2",
            "buying_price": "129",
            "selling_price": "31 (58)",
            "description": "Just a crappy toy with lifetime warranty of just two days.",
            "merchant": "Sales Man (Training Grounds)",
            "mob_drops": "None",
            "two_handed": "No"
        }
    ]
    return render_template("warrior_weapons.html", items=items)


@app.route("/archer_weapons")
def archer_weapons():
    return "Hello Archer World"


@app.route("/mage_weapons")
def mage_weapons():
    return "Hello Mage World"


@app.route("/cowboy_weapons")
def cowboy_weapons():
    return "Hello Cowboy World"


if __name__ == '__main__':
    app.run()
