import requests
from bs4 import BeautifulSoup
from csv import writer

#Billboard Hot 100
 
response = requests.get('https://www.billboard.com/charts/hot-100')
 
soup = BeautifulSoup(response.text, 'html.parser')
 
posts = soup.find_all(class_='chart-element__information')
 
with open('billboard_Chart.csv', 'w', newline='') as csv_file:
	csv_writer = writer(csv_file)
	headers = ['TITLE','ARTIST']
	csv_writer.writerow(headers)
    
	for post in posts:
		title = post.find(class_='chart-element__information__song text--truncate color--primary').get_text().replace('\n', '').strip()
		artist = post.find(class_='chart-element__information__artist text--truncate color--secondary').get_text().replace('\n', '').replace('Featuring', 'Feat.').strip()
		csv_writer.writerow([title, artist])

# -------------------------------------------------------------------------------------------------------------
 
#Billboard Latin
     
response = requests.get('https://www.billboard.com/charts/latin-songs')
 
soup = BeautifulSoup(response.text, 'html.parser')
 
posts = soup.find_all(class_='chart-list-item__text-wrapper')
# posts1 = soup.find_all(class_='chart-number-one__info')
 
with open('Chart - Hot Latin Songs.csv', 'w', newline='') as csv_file:
    csv_writer = writer(csv_file)
    headers = ['TITLE','ARTIST']
    csv_writer.writerow(headers)
   
    
    for post in posts:
        title = post.find(class_='chart-list-item__title-text').get_text().replace('\n', '').strip()
        artist = post.find(class_='chart-list-item__artist').get_text().replace('\n', '').replace('Featuring', 'Feat.').strip()
        csv_writer.writerow([title, artist])