import importlib.util
import os
import pandas as pd
import traceback

module_path = r'c:\Users\Akshada\OneDrive\Desktop\Collage\current\IPP\New folder\alice 7.py'
spec = importlib.util.spec_from_file_location('alice7', module_path)
mod = importlib.util.module_from_spec(spec)
try:
    spec.loader.exec_module(mod)
except Exception as e:
    print('Error importing alice 7.py:', e)
    traceback.print_exc()
    raise

pm = mod.ProfileManager()
print('Using files:')
print(' profiles:', pm.profiles_file)
print(' player csv:', pm.player_csv)
print(' game stats csv:', pm.game_stats_csv)

TEST_NAME = '__auto_test_user__'
# Clean if exists
if TEST_NAME in pm.profiles:
    pm.delete_profile(TEST_NAME)

# Create profile
ok, msg = pm.create_profile(TEST_NAME)
print('create_profile:', ok, msg)
# record a realm play
pm.record_realm_play(TEST_NAME, 'python', 'easy', new_score=42, old_score=None, attempts=3)
print('recorded realm play')

# Read CSVs and print last few rows
try:
    df_p = pd.read_csv(pm.player_csv)
    print('\nplayer_data.csv (tail):')
    print(df_p.tail(5).to_string(index=False))
except Exception as e:
    print('Error reading player csv:', e)

try:
    df_g = pd.read_csv(pm.game_stats_csv)
    print('\ngame_stats.csv (tail):')
    print(df_g.tail(5).to_string(index=False))
except Exception as e:
    print('Error reading game stats csv:', e)

# Cleanup
pm.delete_profile(TEST_NAME)
print('\nCleaned up test profile')

