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
            "selling_price": "1",
            "description": "A plain stick for hitting things.",
            "merchant": "Sales Man (Training Grounds)",
            "mob_drops": "Green Bouncer, Purple Bouncer, Green Walker, Mushroom Ball",
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
            "mob_drops": "Mushroom Squish, Crab",
            "two_handed": "No"
        },
        {
            "name": "Blue Plastic Sword",
            "power": "5",
            "level": "4",
            "buying_price": "230",
            "selling_price": "57 (103)",
            "description": "Still a piece of junk, but at least it's better than a red plastic sword.",
            "merchant": "Sales Man (Training Grounds)",
            "mob_drops": "None",
            "two_handed": "No"
        },
        {
            "name": "Plastic Saber",
            "power": "7",
            "level": "6",
            "buying_price": "551",
            "selling_price": "137 (248)",
            "description": "An extenable fighting toy for little kids.",
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
