import http.client

conn = http.client.HTTPSConnection("sneaker-db-stockx-light-version.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "",
    'x-rapidapi-host': "sneaker-db-stockx-light-version.p.rapidapi.com"
}

def search_sneakers(query):
    conn.request("GET", f"/searchv3?s={query}", headers=headers)

    res = conn.getresponse()
    data = res.read()

    return data.decode("utf-8")

def get_sneaker_details(url_key):
    conn.request("GET", f"/productsDetail?urlKey={url_key}", headers=headers)

    res = conn.getresponse()
    data = res.read()

    return data.decode("utf-8")

queries = [
    "Air Jordan 1",
"Air Jordan 3",
"Air Jordan 4",
"Air Jordan 5",
"Air Jordan 6",
"Air Jordan 11",
"Air Jordan 13",
"Nike Dunk Low",
"Nike Dunk High",
"Nike SB Dunk",
"Nike Air Force 1",
"Nike Air Max 1",
"Nike Air Max 90",
"Nike Air Max 97",
"Nike Air Max 270",
"Nike Air Max Plus",
"Nike Blazer Mid",
"Nike Blazer Low",
"Nike Kobe 6",
"Nike Kobe 5",
"Yeezy Boost 350",
"Yeezy Boost 380",
"Yeezy Boost 700",
"Yeezy Slide",
"Yeezy Foam Runner",
"Adidas Ultraboost",
"Adidas NMD",
"Adidas Superstar",
"Adidas Stan Smith",
"Adidas Forum Low",
"New Balance 550",
"New Balance 990",
"New Balance 992",
"New Balance 2002R",
"New Balance 327",
"New Balance 574",
"New Balance 530",
"Asics Gel Lyte III",
"Asics Gel Kayano",
"Asics Gel Nimbus",
"Puma Suede Classic",
"Puma RS-X",
"Puma Clyde",
"Converse Chuck 70",
"Converse All Star",
"Converse Run Star Hike",
"Reebok Classic Leather",
"Reebok Club C",
"Reebok Question Mid",
"Vans Old Skool",
]

def main():
    # print(get_sneaker_details("Nike-Air-Force-1-Low-Protro-Kobe-Bryant-Mamba-Mentality"))
    for query in queries:
        # url escape query
        escaped_query = query.replace(" ", "%20").replace("-", "%2D").replace("(", "%28").replace(")", "%29")
        print(f"Searching for: {query}")
        result = search_sneakers(escaped_query)
        open(f"query_results/{query}.json", "w", encoding="utf-8").write(result)

if __name__ == "__main__":
    main()