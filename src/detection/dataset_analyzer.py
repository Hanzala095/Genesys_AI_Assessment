import os
import pandas as pd


TRAIN_PATH = r"data/raw/train"
TEST_PATH = r"data/raw/test"


def count_videos(folder_path):

    data = []

    for class_name in os.listdir(folder_path):

        class_path = os.path.join(folder_path, class_name)

        if os.path.isdir(class_path):

            video_count = len([
                file
                for file in os.listdir(class_path)
                if file.endswith(".mp4")
            ])

            data.append({
                "Class": class_name,
                "Videos": video_count
            })

    return pd.DataFrame(data)


if __name__ == "__main__":

    print("\nTRAIN DATASET\n")

    train_df = count_videos(TRAIN_PATH)

    print(train_df)

    print("\nTOTAL TRAIN VIDEOS:")
    print(train_df["Videos"].sum())

    print("\n" + "=" * 50)

    print("\nTEST DATASET\n")

    test_df = count_videos(TEST_PATH)

    print(test_df)

    print("\nTOTAL TEST VIDEOS:")
    print(test_df["Videos"].sum())