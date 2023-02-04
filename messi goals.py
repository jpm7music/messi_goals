import requests
from bs4 import BeautifulSoup

# Make the request to the website
response = requests.get("https://www.messivsronaldo.app/")

# Check the response status code
if response.status_code == 200:
    # Parse the HTML content of the response
    soup = BeautifulSoup(response.content, "html.parser")
    
    # Find the container that holds the number of goals
    goals_container = soup.find("span", class_="StatsBlock-module--statNum--1Tu-D StatsBlock-module--largeNum--1nl6o")
    
    # Extract the number of goals
    goals = int(goals_container.text)
    
    # Print the number of goals
    print("Lionel Messi ha marcado {} goles en su carrera".format(goals))

       # read the previous value from a file
    try:
       with open("previous_value.txt", "r") as f:
        contents = f.read().strip()
        if contents:
            previous_value = int(contents)
        else:
            previous_value = 0
    except FileNotFoundError:
        previous_value = 0

    difference = goals - previous_value

    print("Han sido {} goles desde la última vez que revisaste ".format(difference))

    # update the previous value
    with open("previous_value.txt", "w") as f:
        f.write(str(goals))
else:
    # Handle the error
    print("Failed to retrieve data from the website")