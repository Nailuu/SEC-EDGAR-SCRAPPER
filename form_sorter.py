import requests, json, os

path = "raw_data.json"

if not os.path.exists(path):
    print(f"You must run form_links_scrapper.py ({path} does not exist)")

def contains_g_code(form):
    form = form.decode("utf-8")
    if """<span class="SmallFormData">G</span>""" in form:
        return True
    else:
        return False


def sort():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:136.0) Gecko/20100101 Firefox/136.0',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Connection': 'keep-alive',
        'Origin': 'https://www.sec.gov'
    }
    
    with open(path, "r") as file:
        data = json.load(file)
        for entity in data:
            for url in entity["forms"][:]:
                response = requests.get(url, headers=headers)

                if (response.status_code == 200):
                    if contains_g_code(response.content):
                        print(f"\033[32m[G] {entity['name']}\033[0m {url}")
                        entity["total_g_forms"] += 1
                    else:
                        print(f"\033[31m[NO G] {entity['name']}\033[0m {url}")
                        entity["forms"].remove(url)
                        
                        with open("backup.json", "w") as backup:
                            json.dump(data, backup)
                else:
                    print(f"\033[31m[ERROR {response.status_code}] {entity['name']}:\033[0m {url}")
            try:
                entity["g_form_rate"] = entity["total_g_forms"] / entity["total_extracted_forms"] * 100
            except ZeroDivisionError:
                entity["g_form_rate"] = 0

            with open("backup.json", "w") as backup:
                json.dump(data, backup)
        print("\n\033[34m---------------------FINISHED-----------------------\033[0m\n")
        total = 0
        for entity in data:
            print(f"\033[34m{entity['name']}\033[0m - {entity['total_g_forms']} ({entity['g_form_rate']:.2f}%)")
            total += entity["total_g_forms"]
    
    print(f"\n\033[32mTotal:\033[0m {total}")

sort()