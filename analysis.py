import os
import pandas as pd

def count_files_in_folder(folder_path):
    file_count = 0
    file_names = []
    for filename in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, filename)):
            file_count += 1
            file_names.append(filename)
    return file_count, file_names

if __name__ == "__main__":
    folder_path = "path/to/your/folder"
    file_count, file_names = count_files_in_folder(folder_path)

    # Create a pandas DataFrame
    df = pd.DataFrame({"File Name": file_names})

    # Add a new column for file count
    df["File Count"] = file_count

    # Display the DataFrame
    print(df)
    
    # Save the DataFrame to a CSV file
    df.to_csv("file_counts.csv", index=False)
