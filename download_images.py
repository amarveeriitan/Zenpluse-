import os
import requests
from duckduckgo_search import DDGS

products = [
    (101, 'L-Carnitine Liquid supplement bottle'),
    (102, 'Fiber Pro Plus supplement container'),
    (103, 'Premium Yoga Mat rolled'),
    (104, 'Body Weight Scale modern digital'),
    (105, 'Detox Tea Set box'),
    (106, 'Fat Caliper body measurement tool'),
    (107, 'Speed Jump Rope fitness'),
    (108, 'Meal Prep Containers stacked'),
    (109, 'Green Tea Extract capsules supplement'),
    (110, 'Protein Shaker Bottle'),
    
    (201, 'Mass Gainer 2kg supplement tub'),
    (202, 'Adjustable Dumbbells heavy gym'),
    (203, 'Wrist Wraps weightlifting pair'),
    (204, 'ZMA Recovery vitamins bottle'),
    (205, 'Pre-Workout Shot energy bottle'),
    (206, 'Creatine Monohydrate powder tub'),
    (207, 'Leather Lifting Belt gym'),
    (208, 'Protein Bars Box snack'),
    (209, 'Resistance Bands fitness set'),
    (210, 'Liquid Chalk gym bottle'),

    (301, 'Zafu Cushion meditation'),
    (302, 'Zen Diffuser aromatherapy'),
    (303, 'Essential Oil Pack small bottles'),
    (304, 'Crystal Singing Bowl sound therapy'),
    (305, 'Journal and Pen Set mindfulness'),
    (306, 'Tibetan Bells tingsha'),
    (307, 'Incense Sticks burning'),
    (308, 'Meditation Timer digital'),
    (309, 'Mala Beads 108 wooden'),
    (310, 'Silk Eye Mask sleep')
]

os.makedirs('assets', exist_ok=True)

with DDGS() as ddgs:
    for pid, query in products:
        filename = f"assets/prod_{pid}.jpg"
        if os.path.exists(filename):
            continue
            
        print(f"Searching for {query}...")
        try:
            results = list(ddgs.images(query, max_results=1))
            if results:
                img_url = results[0]['image']
                print(f"Downloading {img_url}")
                img_data = requests.get(img_url, timeout=10).content
                with open(filename, 'wb') as f:
                    f.write(img_data)
            else:
                print(f"No image found for {query}")
        except Exception as e:
            print(f"Failed for {query}: {e}")

print("Done downloading images.")
