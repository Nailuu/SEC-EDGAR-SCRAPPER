import requests

# Form URL = https://www.sec.gov/Archives/edgar/data/ _source.ciks[0].trim('0') / _source.adsh.trim('-') / _source.xsl / _id.find(':')
# https://www.sec.gov/Archives/edgar/data/1612571/000141588923003904/xslF345X03/form4-03032023_120329.xml
# 
# DATA EXAMPLE
# {
#         "_index": "edgar_file",
#         "_id": "0001415889-22-003603:form4-04012022_020405.xml",
#         "_score": 13.123604,
#         "_source": {
#           "ciks": [
#             "0001612571",
#             "0000001800"
#           ],
#           "period_ending": "2022-03-25",
#           "file_num": [
#             "001-02189"
#           ],
#           "display_names": [
#             "Ford Robert B  (CIK 0001612571)",
#             "ABBOTT LABORATORIES  (ABT)  (CIK 0000001800)"
#           ],
#           "xsl": "xslF345X03",
#           "schema_version": "X0306",
#           "sequence": 1,
#           "root_forms": [
#             "4"
#           ],
#           "file_date": "2022-04-01",
#           "biz_states": [
#             "IL"
#           ],
#           "sics": [
#             "2834"
#           ],
#           "form": "4",
#           "adsh": "0001415889-22-003603",
#           "film_num": [
#             "22799573"
#           ],
#           "biz_locations": [
#             "",
#             "Abbott Park, IL"
#           ],
#           "file_type": "4",
#           "file_description": null,
#           "inc_states": [
#             "",
#             "IL"
#           ],
#           "items": []
#         }
#       }
def extract_form_url(json):
    xsl = json["_source"]["xsl"]
    if (xsl is None):
        return None

    ciks = json["_source"]["ciks"][0].lstrip('0')
    adsh = json["_source"]["adsh"].replace('-', '')
    id = json["_id"].split(':')[1]

    url = "https://www.sec.gov/Archives/edgar/data/" + str(ciks) + "/" + str(adsh) + "/" + str(xsl) + "/" + str(id)

    return url

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:136.0) Gecko/20100101 Firefox/136.0',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Connection': 'keep-alive',
    'Origin': 'https://www.sec.gov'
}

entities = ["Robert Ford"]

for entity in entities:
    forms_links = []

    while True:
        # TO-DO - Implement multi page scrap
        url = f"https://efts.sec.gov/LATEST/search-index?q={entity}&dateRange=all&filter_forms=4&startdt=2001-01-01&enddt=2025-03-19"
        # &page=2
        response = requests.get(url, headers=headers)

        if (response.status_code == 200):
            data = response.json()
            files = data["hits"]["hits"]
            for file in files:
                url = extract_form_url(file)
                print(url)
