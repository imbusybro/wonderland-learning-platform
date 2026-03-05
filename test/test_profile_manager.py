import os
import pprint
import importlib.util
import pandas as pd

# Path to the alice file (has a space in the filename)
alice_path = r"c:\Users\Akshada\OneDrive\Desktop\Collage\current\IPP\New folder\alice 7.py"

spec = importlib.util.spec_from_file_location('alice7_module', alice_path)
alice7 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(alice7)

# Instantiate ProfileManager
pm = alice7.ProfileManager()

username = "__test_user__"
# Clean up if it exists
if username in pm.profiles:
    pm.delete_profile(username)

print('Creating profile:', username)
success, msg = pm.create_profile(username)
print('create_profile ->', success, msg)

# Record a realm play
print('Recording realm play: python easy 80')
pm.record_realm_play(username, 'python', 'easy', new_score=80, old_score=None)

# Print profile data
print('\nProfile data (from JSON):')
pprint.pprint(pm.profiles.get(username))

# Print CSV snippets
print('\nplayer_data.csv exists?', os.path.exists(pm.player_csv))
if os.path.exists(pm.player_csv):
    print('\n-- player_data.csv head --')
    try:
        print(pd.read_csv(pm.player_csv).head().to_string(index=False))
    except Exception as e:
        print('Error reading player_data.csv:', e)

print('\ngame_stats.csv exists?', os.path.exists(pm.game_stats_csv))
if os.path.exists(pm.game_stats_csv):
    print('\n-- game_stats.csv head --')
    try:
        print(pd.read_csv(pm.game_stats_csv).head().to_string(index=False))
    except Exception as e:
        print('Error reading game_stats.csv:', e)

print('\nTest done.')

# Cleanup test user
try:
    if username in pm.profiles:
        pm.delete_profile(username)
        print('Cleaned up test profile:', username)
except Exception as e:
    print('Cleanup failed:', e)

