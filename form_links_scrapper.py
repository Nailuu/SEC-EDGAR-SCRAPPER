import requests, json

entities = [
    "Tim Spence", "Robert Ford", "Julie Sweet", "Evan Greenberg", "Bobby Kotick",
    "Shantanu Narayen", "Doctor Lisa Su", "Doctor Andrés Gluski Weilert", "Dan Amos",
    "Mike McMullen", "Seifi Ghasemi", "Doctor Tom Leighton", "Ben Minicucci",
    "Jerry Masters Jr", "John Plant", "Joe Hogan", "Sarah London", "Dave Lesar",
    "Kate Johnson", "Stephanie Ferris", "Dave Bozeman", "Jim Foster", "Mike Wirth",
    "Matthew Farrell", "David Cordani", "Steve Johnston", "Todd Schneider",
    "Chuck Robbins", "Jane Fraser", "Linda Rendle", "Garrick Rochow", "Todd Kahn",
    "James Quincey", "Ravi Singisetti", "Noel Wallace", "Brian Roberts",
    "Curtis Farmer", "Jeff Miller", "Rodney Sacks", "Hilton Schlosberg",
    "Chris Kubasik", "Chris Swift", "Chris Cocks", "Shankh Mitra", "Dave Foss",
    "Stan Bergman", "Michele Buck", "Enrique Lores", "Steve MacMillan",
    "Ted Decker", "Vimal Kapur", "Jim Snee", "Jim Risoleo", "Bruce Broussard",
    "John Roberts III", "Steve Steinour", "Eric Ashleman", "Jonathan Mazelsky",
    "H Bolton Jr", "Mike Roman", "Jeff Lorberbaum", "Rob Fauber", "James Gorman",
    "Greg Brown", "George Kurian", "R Feight", "Mark Kowlzan", "Jim Heppelmann",
    "Thomas Williams", "John Gibson Jr", "John Stauch", "Ramon Laguarta",
    "Doctor Albert Bourla", "Patti Poppe", "Billy Gifford Jr", "Ryan Lance",
    "Jeff Guldner", "Scott Sheffield", "William Demchak", "Patrice Louvet",
    "George Oliver", "H Moore Jr", "Donnie King", "J Kirby", "Lance Fritz",
    "Larry Fink", "Dave Calhoun", "Frederic Lissalde", "Owen Thomas",
    "Mike Mahoney", "Giovanni Caforio", "J Brown", "Lawson Whiting", "Tom Jorden",
    "Doctor Anirudh Devgan", "Ric Campo", "Mark Clouse", "Rich Fairbank",
    "Jason Hollar", "Josh Weinstein", "Jim Umpleby III", "Bob Sulentic", "Bob Bakish", 
    "Lal Karsanbhai", "Drew Marsh", "Ezra Yacob", "Mark Begor", "Charles Meyers", 
    "Toby Rice", "Mark Parrell", "Angela Kleiman", "Fabrizio Freda", "Calvin Butler Jr", 
    "Jeff Musser", "Darren Woods", "Francois Locoh-Donou", "Phil Snow", "Dan Florness", 
    "Don Wood", "Raj Subramaniam", "Brian Tierney", "Mark Douglas", "Joaquin Duato", 
    "Jamie Dimon", "Rami Rahim", "Steve Cahillane", "Chris Gorman", "Mike Hsu", 
    "Conor Flynn", "Rick Wallace", "Doctor Dirk van de Put", "William McMullen", 
    "Adam Schechter", "Tim Archer", "Stuart Miller", "Jon Jaffe", "Dave Ricks", 
    "Gina Boswell", "Ellen Cooper", "Jim Taiclet Jr", "Jim Tisch", "Tim Knavish", 
    "Vince Sorgi", "Rob Sharps", "Glenn Fogel", "Dan Houston", "Jon Moeller", 
    "Tricia Griffith", "Charlie Lowrey Jr", "Ralph LaRossa", "Joe Russell Jr", 
    "Ryan Marshall", "Cristiano Amon", "Duke Austin Jr", "Jim Davis", "Paul Reilly", 
    "Sumit Roy", "Lisa Palmer", "Doctor Len Schleifer", "Jon Vander Ark", "Mick Farrell", 
    "Vincent Pilette", "Doctor Aart De Geus", "Kevin Hourican", "Strauss Zelnick", 
    "Brian Cornell", "Chuck Kummeth", "Professor Doctor Robert Mehrabian", "Liam Kelly", 
    "Greg Smith", "Haviv Ilan", "Scott Donnelly", "Marc Casper", "Ernie Herrman", 
    "Frank Svoboda", "Matt Darden", "Hal Lawton III", "Rob Painter", "David Gibbs", 
    "Marc Miller", "Andy Cecere", "Bernard Kim", "Lee Tillman", "Tom Toomey", 
    "Sir Andrew Witty", "Carol Tomé", "Matt Flannery", "Greg Hayes", "R Riggs", 
    "Debra Cafaro", "John Larsen", "Tom Wilson II", "Liam Griffin", "Andy Jassy", 
    "Hamid Moghadam", "Ron Delia", "Nicholas Akins", "Steve Squeri", "Peter Zaffino",
    "Tom Bartlett", "M Hardwick", "John Hess", "Marty Lyons Jr", "David Zapico",
    "Bob Bradway", "Richard Norwitt", "Andrew Schlossberg", "Vincent Roche",
    "Doctor Ajei Gopal", "Gail Boudreaux", "Greg Case", "John Christmann IV",
    "Tim Cook", "Gary Dickerson", "Marc Grandisson", "Juan Luciano",
    "Michael Salvino", "Sean Connolly", "Tim Cawley", "Bill Newlands Jr",
    "Al White III", "Gavin Hattersley", "Jeffrey Liaw", "Wendell Weeks",
    "Andy Florance", "W Jelinek", "Jay Brown", "Joe Hinrichs",
    "Jennifer Rumsey", "Karen Lynch", "Rainer Blair", "Rick Cardenas",
    "Javier Rodriguez", "John May", "Ed Bastian", "Ernest Santi",
    "Francis deSouza", "Hervé Hoppenot", "Dave Regnery", "Doctor Pat Gelsinger",
    "Philippe Krakowsky", "Doctor Arvind Krishna", "Frank Clyburn Jr",
    "Mark Sutton", "Sasan Goodarzi", "Doctor Gary Guthart", "Bill Meaney",
    "Bob Pragada", "Chris Peterson", "Tom Palmer", "John Donahoe II",
    "Lloyd Yates", "Naga Nagarajan", "Alan Shaw", "Mike O'Grady",
    "Kathy Warden", "Doctor Larry Coben", "Joe Nolan Jr", "Leon Topalian",
    "Jensen Huang", "Vicki Hollub", "Kevin Freeman", "John Wren III",
    "Hassane El-Khoury", "Pierce Norton II", "Safra Catz", "Kevin Wheeler",
    "Mark Smucker", "Nick Pinchuk", "Chris Womack", "Bob Jordan",
    "Don Allan Jr", "Laxman Narasimhan", "Ron O'Hanley III", "Mark Millett",
    "Dan Carestio", "Kevin Lobo", "Adena Friedman", "Lori Ryerkerk",
    "Marc Benioff", "Jean-Louis Servranckx", "Brian Niccol", "Bill Nash",
    "Sundar Pichai", "The Hon. Terry Duffy", "Jim Bidzos", "Hans Vestberg",
    "Doctor Reshma Kewalramani", "Bracken Darrell", "Alan Schnitzer",
    "John Akers", "Carlos Rodriguez", "Doctor Andrew Anagnost",
    "Bill Rhodes III", "Benjamin Schall", "Mitchell Butier",
    "Lorenzo Simonelli", "Dan Fisher", "Joe Almeida",
    "Bill Rogers Jr", "Tom Polen", "Rob Berkley Jr", "Warren Buffett",
    "Corie Barry", "Norman Schwartz", "Brian Moynihan", "Simon Campion",
    "Rick Muncrief", "Rick Dreiling", "Bob Blue", "Rich Tobin", "David Auld",
    "Jerry Norcia", "Mark Costa", "Craig Arnold", "Jamie Iannone", "W Carlson",
    "Christophe Beck", "Pedro Pizarro", "Bernard Zovighian", "Andrew Wilson",
    "Jim Farley Jr", "John Ketchum", "Jenny Johnson", "Richard Adkerson",
    "Pat Gallagher Jr", "Cliff Pemble", "Gene Hall", "Phebe Novakovic",
    "Larry Culp Jr", "Jeff Harmening", "Paul Donahue", "Daniel O'Day",
    "Cameron Bready", "David Solomon", "DG Macpherson", "Marvin Ellison",
    "René Jones", "Tony Capuano Jr", "John Doyle", "Ward Nye", "Keith Allman",
    "Lawrence Kurzius", "Chris Kempczinski", "Doug Peterson", "Doctor Brian Tyler",
    "Geoff Martha", "Michel Khalaf", "Bill Hornbuckle IV", "Ganesh Moorthy",
    "Sanjay Mehrotra", "Satya Nadella", "Michael Waddell", "Blake Moret",
    "Jerry Gahlhoff Jr", "Laurence Hunn", "Barbara Rentler", "Jason Liberty",
    "Jeff Stoops", "John Stankey", "Rob Davis", "Olivier Le Peuch",
    "Walt Bettinger II", "Pete Arvan", "Doctor Dave Mosley", "Ted Doheny II",
    "Jeff Martin", "John Morikis", "David Simon", "Steve Roth", "Tom Hill",
    "Rafael Santana", "Rosalind Brewer", "Doug McMillon", "Bob Iger",
    "Jim Fish Jr", "Doctor Udit Batra", "Charlie Scharf", "Eric Green",
    "David Goeckeler", "Devin Stockfish", "Doctor Marc Bitzer", "Alan Armstrong",
    "Carl Hess", "Scott Lauber", "Bob Frenzel", "Bill Burns", "Ivan Tornos",
    "Harris Simmons", "Chris Viehbacher", "Dave Kimbell", "Michael Hsing",
    "Rob Goldstein", "Tom Bell", "Joe DePaolo", "Hock Tan", "Doctor Kevin Stein",
    "Terrence Curtin", "Ryan McInerney", "Ken Xie", "Kurt Sievers", "Mary Barra", "Kim Dang", "Kevin Clark",
    "Badri Kothandaraman", "Bill McDermott", "Harry Sommer", "Robert Thomson",
    "John Stone", "Alessandro Maselli", "Brian Doubles", "Zvi Lando",
    "Daniel Schulman", "Tom Werner", "Ed Breen", "Stéphane Bancel",
    "Lachlan Murdoch", "John Turner Jr", "Keith Demmings", "Joc O'Rourke",
    "Chris Concannon", "Jim Cracchiolo", "Peter Kern", "Lynn Good",
    "Mike Sievert", "Tim Gokey", "Henry Fernandez", "Aaron Jagdfeld",
    "Chris Winfrey", "Ron Clarke", "Christopher Kastner", "Bob Espey",
    "Mark Lashier", "Travis Stice", "Kristin Peck", "Chris Leahy",
    "Robert Isom Jr", "Chris Nassetta", "Tom Reeg", "Josh Silverman",
    "Antonio Neri", "Ed Pitoniak", "Jim Fitterling", "Scott Smith",
    "Joseph Zubretsky", "Joe Margolis", "Tony Will", "Robin Vince",
    "David Zaslav", "Lee Shavel", "Edward Tilly", "Peter Vanacker",
    "Sam Hazen", "Arkadiy Dobkin", "Mark Zuckerberg", "Ari Bousbib",
    "Jayshree Ullal", "Satish Dhanasekaran", "Jim Lico", "Vicente Reynal",
    "David Campbell", "Chuck Magro", "Greg Davis", "Kevin Ali",
    "Roger Hochschild", "Russell Weiner", "Ted Sarandos Jr", "Greg Peters",
    "Thomas Greco", "Craig Billings", "Kevin Sayer", "Nick Zarcone",
    "Michael Miebach", "Andy Power", "Michael Rapino", "Jeff Sprecher",
    "Mark Widmar", "Bob Gamgort Jr", "Jacek Olczak", "Jeffery Owen",
    "Elon Musk", "Matt Meloy", "Mike Hennigan", "Patrick Decker",
    "Rick Gonzalez", "Chad Richison", "Bruce van Saun", "Bob Bruggeworth",
    "Miguel Patricio", "David Sewell", "Dallas Tanner", "Sanjiv Lamba",
    "Dave Gitlin", "Judy Marks", "Joe Dominguez", "Patrick Kaltenbach",
    "Gregory Johson", "Eugene Bredow"
]

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

    result = []

    for entity in entities:
        sub_result = {
            "name": entity,
            "total_results": 0,
            "total_extracted_forms": 0,
            "success_rate": 0,
            "total_g_forms": 0,
            "g_form_rate": 0,
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
                    sub_result["total_results"] += 1
                    url = extract_form_url(file)
                    if url is not None:
                        sub_result["total_extracted_forms"] += 1
                        sub_result["forms"].append(url)
                if len(files) < 100:
                    break
            else:
                print(f"\033[31m[ERROR {response.status_code}] {entity}:\033[0m {url}")
                break
        try:
            sub_result["success_rate"] = sub_result["total_extracted_forms"] / sub_result["total_results"] * 100
        except ZeroDivisionError:
            sub_result["success_rate"] = 0
        result.append(sub_result)

    with open("raw_data.json", "w") as file:
        json.dump(result, file)

    print("\n\033[34m---------------------FINISHED-----------------------\033[0m\n")
    total = 0
    for entity in result:
        print(f"\033[34m{entity['name']}\033[0m - {entity['total_extracted_forms']} ({entity['success_rate']:.2f}%)")
        total += len(entity["forms"])
    
    print(f"\n\033[32mTotal:\033[0m {total}")

scrap()