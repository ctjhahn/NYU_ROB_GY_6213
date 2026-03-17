# Option 1: generic pickle
import pickle
from pathlib import Path

data_dir = Path(__file__).resolve().parent / "data_straight" 
requested_name = "robot_data_100_5_17_03_26_16_18_53.pkl"
pkl_path = data_dir / requested_name

if not pkl_path.exists():
    pkl_candidates = sorted(data_dir.glob("*.pkl"), key=lambda path: path.stat().st_mtime, reverse=True)
    if not pkl_candidates:
        raise FileNotFoundError(f"No .pkl files found in {data_dir}")
    pkl_path = pkl_candidates[0]

with open(pkl_path, "rb") as f:
    obj = pickle.load(f)

print(f"Loaded file: {pkl_path.name}")
print(type(obj))
print(obj)