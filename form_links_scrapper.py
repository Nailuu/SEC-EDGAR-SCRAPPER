import requests, json

# Form URL = https://www.sec.gov/Archives/edgar/data/ _source.ciks[0].trim('0') / _source.adsh.trim('-') / _source.xsl / _id.find(':')
# https://www.sec.gov/Archives/edgar/data/1612571/000141588923003904/xslF345X03/form4-03032023_120329.xml

def extract_form_url(json):
    xsl = json["_source"]["xsl"]
    if (xsl is None):
        return None

    ciks = json["_source"]["ciks"][0].lstrip('0')
    adsh = json["_source"]["adsh"].replace('-', '')
    id = json["_id"].split(':')[1]

    url = "https://www.sec.gov/Archives/edgar/data/" + str(ciks) + "/" + str(adsh) + "/" + str(xsl) + "/" + str(id)

    return url

def scrap():
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:136.0) Gecko/20100101 Firefox/136.0',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Connection': 'keep-alive',
    'Origin': 'https://www.sec.gov'
    }

    entities = ["Robert Ford", "Waren Buffett", "Lisa Su", "Jensen Huang"]
    result = []

    for entity in entities:
        sub_result = {
            "name": entity,
            "forms": []
        }

        page = 1
        count = 0
        while True:
            url = f"https://efts.sec.gov/LATEST/search-index?q={entity}&dateRange=all&filter_forms=4&startdt=2001-01-01&enddt=2025-03-19&page={page}&from={count}"
            response = requests.get(url, headers=headers)
            page += 1
            count += 100

            if (response.status_code == 200):
                data = response.json()
                files = data["hits"]["hits"]
                print(f"\033[32m[FETCHED] {entity}:\033[0m {len(files)} forms")
                for file in files:
                    url = extract_form_url(file)
                    if url is not None:
                        sub_result["forms"].append(url)
                if len(files) < 100:
                    break
            else:
                print(f"\033[31m[ERROR] {entity}:\033[0m {url}")
                break
        result.append(sub_result)

    print("\033[34m---------------------FINISHED-----------------------\033[0m\n")
    for entity in result:
        print(f"\033[34m{entity["name"]}\033[0m - {len(entity["forms"])} forms")

    with open("raw_forms.txt", "w") as file:
        json.dump(result, file)

scrap()