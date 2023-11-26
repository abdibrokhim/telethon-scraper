import csv
import os

# Set the directory path containing CSV files
directory_path = 'csv4/'

def read_and_write_csv():
    try:
        # Open output file for writing
        with open('data/output.csv', 'a', newline='') as output_file:
            writer = csv.writer(output_file)

            # Write header row to output file
            # writer.writerow(['Username', 'User ID'])

            # Loop through files in directory
            for filename in os.listdir(directory_path):
                if filename.endswith('.csv'):
                    file_path = os.path.join(directory_path, filename)
                    try:
                        # Open current file for reading
                        with open(file_path, 'r') as input_file:
                            reader = csv.reader(input_file)

                            # Loop through rows in current file and extract username and user ID
                            for row in reader:
                                username = row[0]
                                user_id = row[1]
                                access_hash = row[2]

                                # Write filename, username, and user ID to output file
                                writer.writerow([username, user_id, access_hash])
                                # writer.writerow([user_id])
                    except Exception as e:
                        print(e)
                print('done')
        print("Output file saved successfully!")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    read_and_write_csv()
