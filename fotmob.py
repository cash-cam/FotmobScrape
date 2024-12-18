"""
 This script scrapes the squad information from a team's squad page on FotMob.
 The user is prompted to enter the URL of the team's squad page, and the script
 Will then scrape the team's squad information (player names and images) and print it.
 Additionally, it needs to add the use of adding players to the database and the team.
 The script will continue to prompt the user for URLs until the user types 'exit'.
Note: This script requires the 'requests' and 'beautifulsoup4' libraries, which can be installed using pip.
Note: The url is required in the following format: https://www.fotmob.com/teams/6230/squad/melbourne-victory
"""

import requests
from bs4 import BeautifulSoup


def get_squad(URL):
    response = requests.get(URL)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find the container that holds the squad information
        squad_container = soup.find_all('div', class_='css-cnpt1f-PlayerDetailsTileCSS evmusvs0')
        print("Number of players:", len(squad_container))
        print()
 
        
        # Extract player names and images
        players = []
        for player in squad_container:
            name_div = player.find('span', class_='css-10e7ss7-Name evmusvs1')
            img_tag = player.find('img', class_='Image PlayerImage ImageWithFallback')
            if name_div and img_tag:
                name = name_div.text
                image = img_tag['src']
                players.append({"name": name, "image": image})
        
        return players
    else:
        print("Failed to fetch squad:", response.status_code)
        return []

while True:
    # Prompt the user for the URL
    url = input("Enter the URL of the team squad page (or type 'exit' to quit): ")
    
    # Check if the user wants to exit
    if url.lower() == 'exit':
        break
    
    # Get the squad information
    squad = get_squad(url)
    
    # Print the squad information
    for player in squad:
        print(f"Name: {player['name']}, Image: {player['image']}")
	