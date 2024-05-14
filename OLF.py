import requests
import math

API_KEY = 'AIzaSyDzxAXwHux_H6eu3WTLoXuEG7yqWZScW0s'

# Initialize an empty dictionary for aliases
alias_mapping = {}

def geocode_address(address):
    url = f'https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={API_KEY}'
    response = requests.get(url).json()
    if response['status'] == 'OK':
        location = response['results'][0]['geometry']['location']
        return location['lat'], location['lng']
    else:
        raise Exception('Error geocoding address')

def reverse_geocode(lat, lng):
    url = f'https://maps.googleapis.com/maps/api/geocode/json?latlng={lat},{lng}&key={API_KEY}'
    response = requests.get(url).json()
    if response['status'] == 'OK':
        return response['results'][0]['formatted_address']
    else:
        return 'No address found'

def calculate_midpoint(coords):
    x, y, z = 0, 0, 0
    for lat, lng in coords:
        lat, lng = map(math.radians, [lat, lng])
        x += math.cos(lat) * math.cos(lng)
        y += math.cos(lat) * math.sin(lng)
        z += math.sin(lat)
    total = len(coords)
    x /= total
    y /= total
    z /= total
    lon = math.atan2(y, x)
    hyp = math.sqrt(x * x + y * y)
    lat = math.atan2(z, hyp)
    return list(map(math.degrees, [lat, lon]))

def find_candidate_locations(lat, lng, keywords, radius=48280):
    places = []
    for keyword in keywords:
        url = f'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={lat},{lng}&radius={radius}&keyword={keyword}&key={API_KEY}'
        response = requests.get(url).json()
        if response['status'] == 'OK' and response['results']:
            places.extend([(place['name'], place['geometry']['location']['lat'], place['geometry']['location']['lng']) for place in response['results']])
    return places

def calculate_drive_time(origins, destinations):
    origins_str = '|'.join([f'{lat},{lng}' for lat, lng in origins])
    destinations_str = '|'.join([f'{lat},{lng}' for lat, lng in destinations])
    url = f'https://maps.googleapis.com/maps/api/distancematrix/json?origins={origins_str}&destinations={destinations_str}&key={API_KEY}'
    response = requests.get(url).json()
    if response['status'] == 'OK':
        drive_times = [[element['duration']['value'] for element in row['elements']] for row in response['rows']]
        return drive_times
    else:
        raise Exception('Error calculating drive time')

def main():
    input_type = input("Are you looking for a specific address or a place type (keyword)? Enter 'address' or 'keyword': ").strip().lower()
    place_input = input("Enter the address or place type (e.g., basketball court, park, restaurant, chain name): ").strip()

    addresses = []
    while True:
        address = input("Enter an address or alias (or type 'done' to finish): ").strip()
        if address.lower() == 'done':
            break
        # Check if the input is an alias
        if address.lower() in alias_mapping:
            address = alias_mapping[address.lower()]
        else:
            # Ask if the user wants to add an alias for this address
            add_alias = input(f"Do you want to add an alias for {address}? (yes/no): ").strip().lower()
            if add_alias == 'yes':
                alias = input("Enter the alias: ").strip().lower()
                alias_mapping[alias] = address
        addresses.append(address)
    
    if not addresses:
        print("No addresses provided.")
        return
    
    try:
        coords = [geocode_address(address) for address in addresses]
        
        if input_type == 'address':
            dest_coords = [geocode_address(place_input)]
            dest_names = [place_input]
        else:
            midpoint = calculate_midpoint(coords)
            candidate_locations = find_candidate_locations(midpoint[0], midpoint[1], [place_input])
            dest_coords = [(place[1], place[2]) for place in candidate_locations]
            dest_names = [place[0] for place in candidate_locations]
        
        drive_times = calculate_drive_time(coords, dest_coords)
        
        # Calculate total drive times for each destination
        total_drive_times = [sum(times) for times in zip(*drive_times)]
        
        # Combine names, addresses, and total drive times
        locations_with_drive_times = []
        for i, (name, (lat, lng), total_time) in enumerate(zip(dest_names, dest_coords, total_drive_times)):
            address = reverse_geocode(lat, lng)
            locations_with_drive_times.append((name, address, total_time))
        
        # Sort locations by drive time
        locations_with_drive_times.sort(key=lambda x: x[2])
        
        print(f"The nearest {place_input}s to all addresses are:")
        for i, place in enumerate(locations_with_drive_times):
            print(f"{i + 1}. {place[0]} located at {place[1]} with a total drive time of {place[2]} seconds.")
    
    except Exception as e:
        print(str(e))

if __name__ == '__main__':
    main()

