import os

FRAME_PATH = "data/extracted_frames"

print("\nFRAME DISTRIBUTION\n")

total = 0

for folder in os.listdir(FRAME_PATH):

    folder_path = os.path.join(FRAME_PATH, folder)

    if os.path.isdir(folder_path):

        count = len([
            f for f in os.listdir(folder_path)
            if f.endswith(".jpg")
        ])

        total += count

        print(f"{folder:<40} {count}")

print("\nTOTAL FRAMES:", total)