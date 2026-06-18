import cv2
import os


INPUT_FOLDER = "data/raw/train"
OUTPUT_FOLDER = "data/extracted_frames"


FRAME_SKIP = 30


def extract_frames():

    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    total_saved = 0

    for class_name in os.listdir(INPUT_FOLDER):

        class_input = os.path.join(INPUT_FOLDER, class_name)

        if not os.path.isdir(class_input):
            continue

        class_output = os.path.join(
            OUTPUT_FOLDER,
            class_name
        )

        os.makedirs(class_output, exist_ok=True)

        for video_file in os.listdir(class_input):

            if not video_file.endswith(".mp4"):
                continue

            video_path = os.path.join(
                class_input,
                video_file
            )

            cap = cv2.VideoCapture(video_path)

            frame_count = 0
            saved_count = 0

            while True:

                ret, frame = cap.read()

                if not ret:
                    break

                if frame_count % FRAME_SKIP == 0:

                    frame_name = (
                        f"{video_file[:-4]}"
                        f"_frame_{saved_count}.jpg"
                    )

                    save_path = os.path.join(
                        class_output,
                        frame_name
                    )

                    cv2.imwrite(save_path, frame)

                    saved_count += 1
                    total_saved += 1

                frame_count += 1

            cap.release()

            print(
                f"Processed: {video_file}"
            )

    print("\nDone!")
    print(
        f"Total Frames Saved: {total_saved}"
    )


if __name__ == "__main__":
    extract_frames()