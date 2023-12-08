import streamlit as st
import os
import asyncio
import time
import pandas as pd
from streamlit_gsheets import GSheetsConnection


st.divider()

# def main():
#     st.title('Audio Comparison Survey')

#     # Folder containing paired audio files
#     audio_folder = 'jp_dataset/basic5000/wav'  # Update this path to your audio folder
#     audio_files = os.listdir(audio_folder)

#     # Filter audio files (assuming pairs are named consistently)
#     pairs = {}
#     for filename in audio_files:
#         name, ext = os.path.splitext(filename)
#         if ext == '.wav':
#             pair_name = name.split('_')[0]  # Assuming pairs are named similarly (e.g., audio1_1.wav, audio1_2.wav)
#             if pair_name not in pairs:
#                 pairs[pair_name] = [filename]
#             else:
#                 pairs[pair_name].append(filename)


#     for pair_name, audio_pair in pairs.items():
#         st.subheader(f'Pair: {pair_name}')

#         audio_1_path = os.path.join(audio_folder, audio_pair[0])
#         audio_2_path = os.path.join(audio_folder, audio_pair[1])

#         st.audio(audio_1_path, format='audio/wav')
#         st.audio(audio_2_path, format='audio/wav')

#         st.write('Which audio sounds better?')
#         user_choice = st.radio(f'Choose preferred audio for Pair {pair_name}', ['Audio 1', 'Audio 2'])

#         st.write(f'You selected for Pair {pair_name}: {user_choice}')

def collect_ratings_comprehend(audio_samples):
    ratings = {}
    rating_choices = {
        1: "Very difficult to understand",
        2: "Difficult to understand",
        3: "Moderately understandable",
        4: "Easy to understand",
        5: "Very easy to understand"
    }
    count = 0
    for sample in audio_samples:
        st.write(f"Listening to audio {count}:")
        st.audio(sample, format='audio/wav')
        # Play audio (simulated)
        # Implement code to play the audio sample here (this depends on your audio playback method)

        # Ask the user for their rating by presenting a multiple-choice interface
        rating = st.radio(f"How will you rate the comprehensibility of the audio ?", list(rating_choices.values()), index=2)
        selected_rating = [key for key, value in rating_choices.items() if value == rating][0]
        ratings[sample] = selected_rating
        count += 1
    return ratings

def collect_natural(audio_samples):
    ratings = {}
    rating_choices = {
        1: "Completely unnatural",
        2: "Mostly unnatural",
        3: "Neutral",
        4: "Mostly natural",
        5: "Completely natural"
    }
    count = 0
    for sample in audio_samples:
        # st.write(f"Listening to audio {count}:")
        # st.audio(sample, format='audio/wav')
        # Play audio (simulated)
        # Implement code to play the audio sample here (this depends on your audio playback method)

        # Ask the user for their rating by presenting a multiple-choice interface
        rating = st.radio(f"How will you rate the naturalness of the audio ?", list(rating_choices.values()), index=2)
        selected_rating = [key for key, value in rating_choices.items() if value == rating][0]
        ratings[sample] = selected_rating
        count += 1
    return ratings

# Main function for Streamlit app
# def main():
#     # Title and instructions for the survey
#     st.title("Audio Comparison Survey")
#     #st.write("Listen to each audio sample and select how easy it is to understand.")

#     # Define the audio samples
#     audio_samples = ["jp_dataset/basic5000/wav/BASIC5000_0001.wav"]  # Add your audio file names or descriptions

#     # Collect ratings
#     survey_ratings_comprehend = collect_ratings_comprehend(audio_samples)
#     survey_ratings_naturalness = collect_natural(audio_samples)

#     # Display collected ratings
#     for sample, rating in survey_ratings_comprehend.items():
#         rating_choices = {
#             1: "Very difficult to understand",
#             2: "Difficult to understand",
#             3: "Moderately understandable",
#             4: "Easy to understand",
#             5: "Very easy to understand"
#         }

#     for sample, rating in survey_ratings_naturalness.items():
#         rating_choices = {
#             1: "Very difficult to understand",
#             2: "Difficult to understand",
#             3: "Moderately understandable",
#             4: "Easy to understand",
#             5: "Very easy to understand"
#         }
#         #st.write(f"{sample}: {rating} - {rating_choices[rating]}")
conn = st.experimental_connection("gsheets", type=GSheetsConnection)


def collect_transcriptions(audio_samples):
    

    transcriptions = {}
    total_samples = len(audio_samples)
    df = conn.read(worksheet="IntelligibilityEvaluation")

    for count, audio_sample in enumerate(audio_samples):
        st.write(f"Listening to audio {count + 1}")
        st.audio(audio_sample, format='audio/wav')

        transcription = st.text_area(f"What do you hear in audio {count + 1}?", key=f"transcription_{count}")
        transcriptions[f"Audio_{count + 1}"] = [str(transcription)]
    
    
    
    #print(transcriptions)
    if st.button('Submit All Transcriptions'):
        

        additional_df = pd.DataFrame(transcriptions)

        updated_orders = pd.concat([df, additional_df], ignore_index=True)
        conn.update(worksheet="IntelligibilityEvaluation", data=updated_orders)
        st.write("All transcriptions submitted successfully 🤓!")
        #st.cache_resource.clear()
    return transcriptions   


# # Main function for Streamlit app
# def main():
#     # Title and instructions for the transcription survey
#     st.title("Transcription Survey")
#     st.write("Listen to each audio sample and transcribe what you hear.")

#     # Define the audio samples
#     audio_samples = ["jp_dataset/basic5000/wav/BASIC5000_0001.wav"]  # Add your audio file names or descriptions

#     # Collect transcriptions
#     survey_transcriptions = collect_transcriptions(audio_samples)

#     # Display collected transcriptions
#     #st.write("Collected Transcriptions:")
#     #for sample, transcription in survey_transcriptions.items():
#         #st.write(f"{sample}: {transcription}")

def list_files_with_full_path(directory):
    try:
        files_with_path = []  # List to store full paths of files
        for file_name in os.listdir(directory):
            file_path = os.path.join(directory, file_name)
            if os.path.isfile(file_path):  # Check if it's a file (not a directory)
                files_with_path.append(file_path)
        return files_with_path
    except Exception as e:
        return f"Error: {e}"

# Replace 'path/to/your/folder' with your directory path
folder_path = 'jp_dataset/basic5000/wav'


def page_home():
    st.title('Intelligibility Evaluation')
    st.write("You are given a set of audio files (possibly hear many times), then you will have to write down all the text you hear!")

    audio_samples = list_files_with_full_path(folder_path)
    survey_transcriptions = collect_transcriptions(audio_samples)


def page_audio_comparison():
    st.title('Naturalness Evaluation')
    st.write("You are given a set of audio files (possibly hear many times), then you will have to decide whether the voice is understandable and natural")
    audio_samples = ["jp_dataset/basic5000/wav/BASIC5000_0001.wav"]  # Add your audio file names or descriptions

    # Collect ratings
    survey_ratings_comprehend = collect_ratings_comprehend(audio_samples)
    survey_ratings_naturalness = collect_natural(audio_samples)

    # Display collected ratings
    for sample, rating in survey_ratings_comprehend.items():
        rating_choices = {
            1: "Very difficult to understand",
            2: "Difficult to understand",
            3: "Moderately understandable",
            4: "Easy to understand",
            5: "Very easy to understand"
        }

    for sample, rating in survey_ratings_naturalness.items():
        rating_choices = {
            1: "Very difficult to understand",
            2: "Difficult to understand",
            3: "Moderately understandable",
            4: "Easy to understand",
            5: "Very easy to understand"
        }

def page_feedback():
    st.title('Audio Comparison')
    st.write("Differentiate between model synthesis and groundtruth")
    audio_folder = 'jp_dataset/basic5000/wav'  # Update this path to your audio folder
    audio_files = os.listdir(audio_folder)

    # Filter audio files (assuming pairs are named consistently)
    pairs = {}
    count = 0
    for filename in audio_files:
        name, ext = os.path.splitext(filename)
        if ext == '.wav':
            pair_name = name.split('_')[0]  # Assuming pairs are named similarly (e.g., audio1_1.wav, audio1_2.wav)
            if pair_name not in pairs:
                pairs[pair_name] = [filename]
            else:
                pairs[pair_name].append(filename)
  

    for pair_name, audio_pair in pairs.items():
        st.subheader(f'Pair: {count}')
        count += 1
        audio_1_path = os.path.join(audio_folder, audio_pair[0])
        audio_2_path = os.path.join(audio_folder, audio_pair[1])

        st.audio(audio_1_path, format='audio/wav')
        st.audio(audio_2_path, format='audio/wav')

        user_choice = st.radio(f'Which audio is ground truth ?', ['Audio 1', 'Audio 2'])

def main():
    pages = {
        "Intelligibility Evaluation": page_home,
        "Naturalness Evaluation": page_audio_comparison,
        "Audio Comparison": page_feedback
    }

    st.sidebar.title('Navigation')
    selected_page = st.sidebar.radio('Go to', list(pages.keys()))

    # Run the selected page function
    pages[selected_page]()

if __name__ == "__main__":
    main()
