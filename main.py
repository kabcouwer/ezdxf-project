import json
import os
from utils.dxf_writer import create_dxf_from_json

def main():
    file_name = "siteDetail0"
    file_folder = "example_b_PKVC6ADKF3AK-001-H"

    input_path = os.path.join("input", file_folder, f"{file_name}.json")
    output_folder = os.path.join("output", file_folder)
    os.makedirs(output_folder, exist_ok=True)
    output_file = os.path.join(output_folder, f"{file_name}.dxf")

    with open(input_path, "r") as file:
        data = json.load(file)

    doc = create_dxf_from_json(data)
    doc.saveas(output_file)
    print(f"DXF file saved to: {output_file}")

if __name__ == "__main__":
    main()
