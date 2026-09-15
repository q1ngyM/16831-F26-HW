
import pickle
from pathlib import Path
import numpy as np

for file in sorted(Path("rob831/expert_data").glob("*.pkl")):
    with file.open("rb") as f:
        paths = pickle.load(f)

    returns = [path["reward"].sum() for path in paths]

    print(file.stem)
    print(f"  each trajectory return: {returns}")
    print(f"  Mean: {np.mean(returns):.2f}")
    print(f"  Std:  {np.std(returns):.2f}")
