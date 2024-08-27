# Workout Generator
### Streamlit [Workout Generator](https://appworkoutgenerator.streamlit.app)
The Workout Generator is a Streamlit-based web application that generates personalized workout plans based on user preferences. It uses the ExerciseDB API to fetch exercises and create workout plans for different body parts. The app allows users to select workout types and duration to receive a customized workout routine.
![workout_gen](https://github.com/user-attachments/assets/01f84c40-691a-4a36-99b3-707476b5a3fd)



## Features
+ Custom Workout Plans: Select workout types and duration to generate a tailored workout plan.
+ Exercise Information: Includes details about each exercise such as target muscle, body part, equipment needed, and GIF demonstrations.
+ Download Option: Save the generated workout plan as a text file.

## Installation
1. Clone the repository
2. Install the required packages:
```
pip install streamlit requests
```
3. Add your RapidAPI key:
+ Replace API_KEY in main.py with your RapidAPI key from ExerciseDB API.
4. Run the Streamlit app:
```
streamlit run main.py
```
## Usage
1. Open the app in your web browser 
2. Select a workout type from the dropdown menu.
3. Set the duration of the workout using the slider.
4. Click "Generate Workout Plan" to fetch exercises and create your workout plan.
5. View the workout plan on the screen, complete with exercise details and GIFs.
6. Download the workout plan as a text file using the "Save Workout Plan" button.


