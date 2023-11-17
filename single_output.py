from openai import OpenAI
from dotenv import load_dotenv
import random
import os
import csv

# Load environment variables from .env file
load_dotenv()

client = OpenAI()

# Function to create a directory if it doesn't exist
def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
        
# Writing a short hook title
def hook_title(string):
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a highly-skilled TikTok and Instagram Reels video creator who is a pro in creating short video titles that hook."},
        {"role": "user", "content": f"Write a very short hook title without quotation marks (no longer than 5 words) about this topic: '{string}'."}
    ]
    )

    return(completion.choices[0].message.content)

# Writing voiceover text
def random_cta():
    cta = ['follow the account', 'like this video', 'leave a comment', 'share this video']
    random_cta = random.choice(cta)
    return random_cta

def voiceover_text(string):
    cta = random_cta()
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a highly-skilled TikTok and Instagram Reels video creator who is a pro in creating texts for video voiceovers."},
        {"role": "user", "content": f"Write a voiceover text that will include 3 parts: hook, main information, and a call to action. DO NOT use emojis in your output; don't do it!!! Do not specify which paragraph is which. Don't use quotation marks. The hook should be no longer than one sentence. The main information should be around 5 sentences and about this fact: '{string}'. The call to action should be one sentence and should prompt people to {cta}."}
    ]
    )

    return(completion.choices[0].message.content)

# Writing Instagram caption
def instagram_caption(string):
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a highly-skilled Instagram Reels video creator who is a pro in creating short engaging captions."},
        {"role": "user", "content": f"Write a short straight to the point caption related to this fact: '{string}'. Don't use quotation marks!!! Don't say 'caption' in front of the output. Also, add a few hashtags (both general and specific)."}
    ]
    )

    return(completion.choices[0].message.content)

# Writing TikTok description

def select_random_hashtag():
    tiktok_hashtags = ['#tiktok', '#tiktokviral', '#tiktokers', '#love', '#like', '#follow', '#followme', '#fyp', '#foryourpage', '#viral', '#viralpost', '#justforfun']
    random_hashtag = random.choice(tiktok_hashtags)
    return random_hashtag

def tiktok_caption(string):
    random_hashtag = select_random_hashtag()
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a highly-skilled TikTok video creator who is a pro in creating short engaging captions."},
        {"role": "user", "content": f"Write a caption related to this fact: '{string}'. Don't use quotation marks!!! Don't say 'caption' in front of the output. Add 1 or 2 hashtags. Keep length under 1000 characters."}
    ]
    )

    return(f"{completion.choices[0].message.content} {random_hashtag}")

def single_output(string, file_title):
    output_dir = os.getenv('OUTPUT_FOLDER')
    title = hook_title(string)
    voiceover = voiceover_text(string)
    insta_caption = instagram_caption(string)
    tt_caption = tiktok_caption(string)
    
    create_directory(output_dir)
    
    # Create a file with the keyword as the filename
    filename = f"{output_dir}/{file_title}.csv"
    
    # Check if the file already exists
    file_exists = os.path.isfile(filename)
    
    # Define the header for the TSV file (tab-delimited)
    header = ['video_title', 'voiceover_text', 'instagram_caption', 'tiktok_caption']
    
    # Open the CSV file in append mode with tab as delimiter
    with open(filename, 'a', newline='', encoding='utf-8') as file:
        # Use '\t' as the delimiter for the TSV file
        writer = csv.writer(file, delimiter='\t')
        
        # Write the header only if the file doesn't exist
        if not file_exists:
            writer.writerow(header)
        
        # Write the data as a new row
        writer.writerow([title, voiceover, insta_caption, tt_caption])