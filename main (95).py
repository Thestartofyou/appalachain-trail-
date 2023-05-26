import random

# Sample data representing trail sections and distances
trail_data = {
    'section1': {'start': 'Georgia', 'end': 'North Carolina', 'distance': 80},
    'section2': {'start': 'North Carolina', 'end': 'Tennessee', 'distance': 100},
    'section3': {'start': 'Tennessee', 'end': 'Virginia', 'distance': 150},
    'section4': {'start': 'Virginia', 'end': 'West Virginia', 'distance': 120},
    # ... Add more trail sections ...
}

def generate_route(preferences):
    # Filter trail sections based on user preferences
    filtered_sections = []

    for section, data in trail_data.items():
        # Example: filtering based on distance preference
        if preferences['max_distance'] >= data['distance']:
            filtered_sections.append(section)

    # Randomly select sections to form a route
    selected_sections = random.sample(filtered_sections, preferences['num_sections'])

    # Generate the route based on selected sections
    route = []

    for section in selected_sections:
        route.append(trail_data[section])

    return route

def display_route(route):
    print("Generated Route:")
    for i, section in enumerate(route, start=1):
        print(f"Section {i}: From {section['start']} to {section['end']}, Distance: {section['distance']} miles")
    print("End of Route.")

# Example usage
preferences = {
    'max_distance': 120,
    'num_sections': 3
}

route = generate_route(preferences)
display_route(route)
