from bs4 import BeautifulSoup

with open('weather.html', 'r') as html_content:
    html_content = html_content.read()

html_content = BeautifulSoup(html_content, 'html.parser')

content = html_content.find('tbody').find_all('tr')

weather = []

for day in content:
    cols = day.find_all('td')
    day = cols[0].text
    temperature = int(cols[1].text.strip().replace('Â°C', ''))
    condition = cols[2].text

    print(f'{day}: {temperature} {condition}')
    weather.append({'day': day, 'temperature': temperature, 'condition': condition})

max_temp = max(entry['temperature'] for entry in weather)
temp_days = [entry['day'] for entry in weather if entry['temperature'] == max_temp]

sunny_days = [entry['day'] for entry in weather if entry['condition'] == 'Sunny']

print(f'Hottest days: {max_temp}°C on {", ".join(temp_days)}')
print((f'Sunny days: {", ".join(sunny_days)}'))

avg = sum(entry['temperature'] for entry in weather) / len(weather)
print('Average temperature: {:.2f}'.format(avg))