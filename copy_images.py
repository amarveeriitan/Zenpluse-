import glob
import shutil
import os

brain_dir = r"C:\Users\verma\.gemini\antigravity\brain\2f18430b-4b41-4afe-a513-94c0df667670"
dest_dir = r"C:\PAGE\assets"
os.makedirs(dest_dir, exist_ok=True)

files = [
    ("106_fat_caliper*.png", "fat-caliper.png"),
    ("107_jump_rope*.png", "jump-rope.png"),
    ("108_meal_prep*.png", "meal-prep.png"),
    ("109_green_tea*.png", "green-tea.png"),
    ("110_shaker_bottle*.png", "shaker-bottle.png"),
    ("206_creatine*.png", "creatine.png"),
    ("207_lifting_belt*.png", "lifting-belt.png"),
    ("208_protein_bars*.png", "protein-bars.png"),
    ("209_resistance_bands*.png", "resistance-bands.png"),
    ("210_liquid_chalk*.png", "liquid-chalk.png"),
    ("305_journal_set*.png", "journal-set.png"),
    ("306_tibetan_bells*.png", "tibetan-bells.png"),
    ("307_incense_sticks*.png", "incense-sticks.png"),
    ("308_meditation_timer*.png", "meditation-timer.png"),
    ("309_mala_beads*.png", "mala-beads.png"),
    ("310_eye_mask*.png", "eye-mask.png"),
]

for pattern, dest_name in files:
    matches = glob.glob(os.path.join(brain_dir, pattern))
    if matches:
        latest_file = max(matches, key=os.path.getctime)
        shutil.copy2(latest_file, os.path.join(dest_dir, dest_name))
        print(f"Copied to {dest_name}")
    else:
        print(f"Warning: No match found for {pattern}")
