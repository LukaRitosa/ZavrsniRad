from pathlib import Path
import shutil


SOURCE = Path("data_hr")


DESTINATION = Path("ZavrsniShiny/data")


DESTINATION.mkdir(parents=True, exist_ok=True)

files = [
    "features_assessment2.csv",
    "features_classroom_management2.csv",
    "features_virtual_classroom2.csv"
]

for file in files:
    src = SOURCE / file
    dst = DESTINATION / file

    shutil.copy2(src, dst)

    print(f"Kopirano: {src} -> {dst}")

print("\nSvi CSV-ovi su kopirani u Shiny projekt.")