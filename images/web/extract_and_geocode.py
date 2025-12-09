#!/usr/bin/env python3
"""
Extract universities from MGP everything.json and geocode them.
Handles the specific format: "schools": ["University Name, Country"]
"""

import json
import time
import requests
from collections import defaultdict
import sys

def load_data(json_file):
    """Load the everything.json file."""
    print(f"Loading {json_file}...")
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    print(f"✓ Loaded {len(data)} records")
    return data

def extract_universities(data):
    """Extract unique universities from schools array."""
    universities = set()
    university_counts = defaultdict(int)
    
    for person in data:
        # Handle schools array: ["University Name, Country"]
        schools = person.get('schools', [])
        if schools and isinstance(schools, list):
            for school in schools:
                if school and school.lower() not in ['unknown', '', 'none']:
                    universities.add(school)
                    university_counts[school] += 1
        
        # Also check 'school' field as fallback
        school = person.get('school')
        if school and school.lower() not in ['unknown', '', 'none']:
            universities.add(school)
            university_counts[school] += 1
    
    # Sort by frequency
    sorted_unis = sorted(universities, key=lambda x: university_counts[x], reverse=True)
    
    print(f"\n✓ Found {len(sorted_unis)} unique universities")
    print(f"\nTop 20 most common:")
    for i, uni in enumerate(sorted_unis[:20], 1):
        print(f"  {i:2}. {uni}: {university_counts[uni]} people")
    
    return sorted_unis, university_counts

def geocode_university(name):
    """Geocode a single university."""
    url = "https://nominatim.openstreetmap.org/search"
    params = {
        'q': name,
        'format': 'json',
        'limit': 1
    }
    headers = {
        'User-Agent': 'MathGenealogyProject/1.0'
    }
    
    try:
        response = requests.get(url, params=params, headers=headers, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        if data and len(data) > 0:
            return {
                'lat': float(data[0]['lat']),
                'lon': float(data[0]['lon'])
            }
        return None
    except Exception as e:
        print(f"    Error: {e}")
        return None

def geocode_all(universities, max_count=None):
    """Geocode universities with rate limiting."""
    results = {}
    
    count = min(len(universities), max_count) if max_count else len(universities)
    
    print(f"\n🌍 Geocoding {count} universities...")
    print(f"⏱️  This will take ~{count * 1.1 / 60:.1f} minutes (1.1s per request)")
    print()
    
    for i, uni in enumerate(universities[:count], 1):
        print(f"[{i:3}/{count}] {uni[:60]}...", end=' ')
        
        result = geocode_university(uni)
        
        if result:
            results[uni] = [result['lat'], result['lon']]
            print(f"✓ [{result['lat']:.4f}, {result['lon']:.4f}]")
        else:
            print("✗ Not found")
        
        # Rate limiting
        if i < count:
            time.sleep(1.1)
    
    print(f"\n✓ Successfully geocoded {len(results)}/{count} universities")
    return results

def save_to_js(results, output_file='university_coordinates.js'):
    """Save as JavaScript ES6 module."""
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("// University coordinates for Mathematics Genealogy Project\n")
        f.write("// Auto-generated from MGP dataset\n")
        f.write(f"// Contains {len(results)} universities\n\n")
        f.write("const UNIVERSITY_COORDS = {\n")
        
        for name, coords in sorted(results.items()):
            # Escape single quotes in names
            safe_name = name.replace("'", "\\'")
            f.write(f"  '{safe_name}': [{coords[0]}, {coords[1]}],\n")
        
        f.write("};\n\n")
        f.write("export default UNIVERSITY_COORDS;\n")
    
    print(f"\n✓ Saved to {output_file}")
    print(f"\nNext steps:")
    print(f"1. Copy {output_file} to src/components/")
    print(f"2. You're done! The map will show all {len(results)} universities.")

def main():
    if len(sys.argv) < 2:
        print("Usage: python extract_and_geocode.py <path_to_everything.json>")
        print("\nExample:")
        print("  python extract_and_geocode.py public/sample-data/everything.json")
        print("\nOptions:")
        print("  Add a number to limit geocoding:")
        print("  python extract_and_geocode.py public/sample-data/everything.json 50")
        return
    
    json_file = sys.argv[1]
    
    # Load data
    data = load_data(json_file)
    
    # Extract universities
    universities, counts = extract_universities(data)
    
    # Ask how many to geocode
    if len(sys.argv) > 2:
        max_count = int(sys.argv[2])
        print(f"\n→ Will geocode top {max_count} universities")
    else:
        print(f"\nOptions:")
        print(f"  1. Geocode all {len(universities)} universities (~{len(universities) * 1.1 / 60:.0f} minutes)")
        print(f"  2. Geocode top 100 (~2 minutes)")
        print(f"  3. Geocode top 50 (~1 minute)")
        print(f"  4. Enter custom number")
        print(f"  5. Just save the list (no geocoding)")
        
        choice = input("\nYour choice (1-5): ").strip()
        
        if choice == '1':
            max_count = None
        elif choice == '2':
            max_count = 100
        elif choice == '3':
            max_count = 50
        elif choice == '4':
            max_count = int(input("Enter number: ").strip())
        elif choice == '5':
            # Save list only
            with open('universities_list.txt', 'w', encoding='utf-8') as f:
                for uni in universities:
                    f.write(f"{uni}\n")
            print("✓ Saved to universities_list.txt")
            return
        else:
            print("Invalid choice")
            return
    
    # Geocode
    results = geocode_all(universities, max_count)
    
    # Save
    save_to_js(results)
    
    print("\n🎉 Done!")

if __name__ == '__main__':
    main()
