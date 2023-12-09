import csv
import os
from html2image import Html2Image

hti = Html2Image(size=(4000, 3091))

csv_filename = 'main.csv'
cert_html_filename = 'certificate.html'
output_folder = 'certificates'  # Specify the absolute path here

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Initialize the counter at 1
counter = 1

if os.path.exists(csv_filename):
    # Read data from CSV
    with open(csv_filename, 'r', newline='') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        data = list(csv_reader)

    # Generate certificates
    with open(cert_html_filename, 'r') as file:
        html_template = file.read()

        for item in data:
            full_name = item.get('full_name', '')
            if not full_name:
                print("Error: 'full_name' not found in CSV data for an item.")
                continue

            cert_id_format = "AWSCC-EC-02-{:03d}".format(counter)

            counter += 1

            # Replace placeholders directly in the HTML content
            htmlcontent = html_template.replace("{{ name }}", full_name)
            htmlcontent = htmlcontent.replace("{{ certID }}", cert_id_format)

            # Set the output_path attribute to the specified absolute folder path
            hti.output_path = output_folder

            # Save the certificate with a filename only (no path)
            certificate_filename = f"{full_name}.png"
            hti.screenshot(html_str=htmlcontent, save_as=certificate_filename)

else:
    print(f"Error: '{csv_filename}' not found.")
