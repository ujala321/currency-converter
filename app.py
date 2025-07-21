from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Get all available currency symbols once at startup
def get_currency_list():
    try:
        url = "https://api.exchangerate.host/symbols"
        response = requests.get(url).json()
        if response and "symbols" in response:
            return sorted(response["symbols"].keys())
    except:
        pass
    return ['USD', 'INR', 'EUR', 'GBP', 'JPY']  # fallback

CURRENCIES = get_currency_list()

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    rate_info = None
    error = None

    # Default selections
    from_currency = "USD"
    to_currency = "INR"

    if request.method == "POST":
        try:
            from_currency = request.form["from"]
            to_currency = request.form["to"]
            amount = float(request.form["amount"])

            # Conversion result
            convert_url = f"https://api.exchangerate.host/convert?from={from_currency}&to={to_currency}&amount={amount}"
            convert_data = requests.get(convert_url).json()

            if convert_data and "result" in convert_data:
                result = round(convert_data["result"], 2)
            else:
                error = "Currency conversion failed."

        except Exception as e:
            error = f"Error: {str(e)}"

    # Always show live exchange rate
    try:
        rate_url = f"https://api.exchangerate.host/convert?from={from_currency}&to={to_currency}&amount=1"
        rate_data = requests.get(rate_url).json()
        if rate_data and "result" in rate_data:
            rate_info = f"1 {from_currency} = {round(rate_data['result'], 4)} {to_currency}"
    except:
        rate_info = None

    return render_template("index.html",
                           currencies=CURRENCIES,
                           result=result,
                           error=error,
                           rate_info=rate_info,
                           from_currency=from_currency,
                           to_currency=to_currency)

if __name__ == "__main__":
    app.run(debug=True)




