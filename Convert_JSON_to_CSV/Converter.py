import json

if __name__ == "__main__":
    try:
        with open("input.json",'r') as f:
            data = json.load(f)
        
        output = ','.join([*data[0]])
        for obj in data:
            output += f'\n{obj["id"]},{obj["name"]},{obj["age"]}'

        with open("output.csv",'w') as f:
            f.write(output)
    except Exception as e:
        print(f"An error occurred: {str(e)}")