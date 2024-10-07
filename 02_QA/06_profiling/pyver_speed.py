import os
import subprocess, functools
import pandas as pd

_PATH = os.path.abspath(os.path.dirname(__file__))
_CACHE_PATH = os.path.join(_PATH, "_pyver_speed.csv")


def _real_run():
    run = functools.partial(subprocess.run, shell=True, capture_output=True, text=True)
    
    pythons = [f"python3.{pyver}" for pyver in [8,9,10,11,12]]
    rows = []
    for py in pythons:
        minver = run(f"{py} --version").stdout
        cmd = run(f"time -p {py} {_PATH}/cProfile/confidence.py")
        values, times = cmd.stdout, cmd.stderr
        mean, p1std, m1std, its = map(
            float, (
                values.splitlines()[-1].replace("(", "").replace(")", "").replace(",", "").split()
            )
        )
        row = {
            "Python": minver.strip().split()[-1], 
            "Its.": its,
            "Mean": mean, 
            "+1 std": p1std, 
            "-1 std": m1std, 
        }
        for l in times.splitlines():
            tname, tvalue = l.strip().split()
            row[tname] = float(tvalue)
        rows.append(row)
        
    df = pd.DataFrame(rows)
    return df

def run():
    try:
        return pd.read_csv(_CACHE_PATH)
    except:
        df = _real_run()
        df.to_csv(_CACHE_PATH, index=False)
        return df