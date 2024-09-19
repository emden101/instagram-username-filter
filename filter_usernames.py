import openai
import time

# Set your OpenAI API key
openai.api_key = "YOUR_OPENAI_API_KEY"

# Function to check if a username belongs to a male individual from USA/Europe
def is_male_from_usa_europe(username):
    try:
        # Define the prompt
        prompt = f"Analyze the Instagram username '{username}'. Based on common usage, does this username likely belong to a male individual from the USA or Europe?"

        # Make the API call to OpenAI
        response = openai.Completion.create(
            engine="text-davinci-003",  # or the latest model you wish to use
            prompt=prompt,
            max_tokens=50
        )

        # Extract the response text
        result = response.choices[0].text.strip().lower()

        # Check if the result matches the required criteria
        if 'male' in result and ('usa' in result or 'europe' in result):
            return True
        else:
            return False
    except Exception as e:
        print(f"Error processing username '{username}': {e}")
        return False

# Function to process a batch of usernames
def process_usernames(file_path, output_path):
    # Open the input file and read the usernames
    with open(file_path, 'r') as file:
        usernames = file.readlines()

    # Prepare a list to hold the filtered usernames
    filtered_usernames = []

    # Process each username
    for i, username in enumerate(usernames):
        username = username.strip()

        # Check if the username matches the criteria
        if is_male_from_usa_europe(username):
            filtered_usernames.append(username)

        # Print progress every 100 usernames
        if i % 100 == 0:
            print(f"Processed {i} usernames...")

        # Sleep for a short duration to avoid hitting rate limits (if needed)
        time.sleep(0.2)  # Adjust sleep as needed based on API limits

    # Save the filtered usernames to a new output file
    with open(output_path, 'w') as output_file:
        for filtered_username in filtered_usernames:
            output_file.write(f"{filtered_username}\n")

    print(f"Finished processing. {len(filtered_usernames)} usernames saved to {output_path}")

# Main execution
if __name__ == "__main__":
    # Input file path (username list) and output file path (filtered list)
    input_file = "input_usernames.txt"
    output_file = "filtered_usernames.txt"

    # Process the usernames and filter based on criteria
    process_usernames(input_file, output_file)
