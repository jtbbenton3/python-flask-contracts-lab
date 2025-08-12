from flask import Flask

app = Flask(__name__)

# --- fake data for the lab ---
contracts = {
    1: "This contract is for John and building a shed",
    # add more if you want; only id=1 is required by the provided tests
}
customers = {"bob"}  # set → fast membership checks

# /contract/<id>: 200 with text if found, else 404
@app.route("/contract/<int:id>", methods=["GET"])
def get_contract(id: int):
    if id in contracts:
        return contracts[id], 200
    return "", 404

# /customer/<customer_name>: 204 no body if found, else 404
@app.route("/customer/<string:customer_name>", methods=["GET"])
def check_customer(customer_name: str):
    if customer_name in customers:
        return "", 204
    return "", 404

if __name__ == "__main__":
    
    app.run(debug=True, port=5555)