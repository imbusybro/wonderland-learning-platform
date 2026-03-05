import importlib.util
import traceback
import os
import sys

module_path = r'c:\Users\Akshada\OneDrive\Desktop\Collage\current\IPP\New folder\alice 7.py'

spec = importlib.util.spec_from_file_location("alice7", module_path)
module = importlib.util.module_from_spec(spec)
try:
    spec.loader.exec_module(module)
except Exception as e:
    print("Error importing module:", e)
    traceback.print_exc()
    sys.exit(1)

try:
    pm = module.ProfileManager()
    print("ProfileManager instantiated")
    print("PANDAS_AVAILABLE in module:", getattr(module, 'PANDAS_AVAILABLE', False))
    print("pd available in module:", 'pd' in module.__dict__)
    print("player_csv:", pm.player_csv)
    print("game_stats_csv:", pm.game_stats_csv)
    print("player_csv exists:", os.path.exists(pm.player_csv))
    print("game_stats_csv exists:", os.path.exists(pm.game_stats_csv))
    print("profiles loaded:", list(pm.profiles.keys()))
except Exception as e:
    print("Error creating ProfileManager:", e)
    traceback.print_exc()
