````markdown
# Project README

## Project Overview

This project provides a Python script for geocoding addresses, reverse geocoding coordinates, calculating midpoints, finding candidate locations based on keywords, and calculating drive times between multiple points. It leverages the Google Maps API for all geocoding and distance calculations.

## Features

- **Geocode Address**: Converts a given address into latitude and longitude coordinates.
- **Reverse Geocode**: Converts latitude and longitude coordinates into a human-readable address.
- **Calculate Midpoint**: Finds the geographic midpoint of a list of coordinates.
- **Find Candidate Locations**: Searches for locations matching specific keywords within a given radius of specified coordinates.
- **Calculate Drive Time**: Determines the drive time between a list of origin points and destination points.

## Prerequisites

- Python 3.x
- `requests` library (`pip install requests`)
- A Google Maps API Key with Geocoding and Distance Matrix API enabled

## Getting Started

### Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/yourprojectname.git
   cd yourprojectname
   ```
````

2. **Install the required Python packages**:

   ```bash
   pip install requests
   ```

3. **Set up your Google Maps API Key**:

   Replace the placeholder `API_KEY` in the script with your actual Google Maps API Key.

### Usage

1. **Run the script**:

   ```bash
   python script.py
   ```

2. **Follow the prompts**:

   - Enter whether you are looking for a specific address or a place type (keyword).
   - Enter the address or place type you are looking for.
   - Enter the addresses or aliases of the starting points.

3. **Alias Mapping**:

   - If you enter an address that you want to map to an alias, you can add an alias for easier reference in the future.

### Example

Here is a step-by-step example of how the script works:

1. **Input the type of search**:

   ```
   Are you looking for a specific address or a place type (keyword)? Enter 'address' or 'keyword':
   ```

2. **Input the address or keyword**:

   ```
   Enter the address or place type (e.g., basketball court, park, restaurant, chain name):
   ```

3. **Input the addresses or aliases**:

   ```
   Enter an address or alias (or type 'done' to finish):
   ```

4. **Alias mapping (optional)**:

   ```
   Do you want to add an alias for [address]? (yes/no):
   Enter the alias:
   ```

5. **Output**:
   The script will display the nearest places matching the input criteria along with their addresses and total drive times from the provided starting points.

If you encounter any issues or have any questions, feel free to open an issue in the repository.

```

```
