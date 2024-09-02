import streamlit as st
import requests
import random
from io import StringIO

# API Key and types mapping
API_KEY =  st.secrets["API_KEY"] # Replace with your RapidAPI key

WORKOUT_TYPES = {
    "Cardio": "cardio",
    "Back": "back",
    "Chest": "chest",
    "Arms": "upper arms",
    "Shoulders": "shoulders",
    "Legs": "upper legs",
    "Abs": "waist",

}



# Function to fetch exercises based on workout type
def fetch_exercises(workout_type, api_key):
    url = "https://exercisedb.p.rapidapi.com/exercises/bodyPart/"

    headers = {
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": "exercisedb.p.rapidapi.com"
    }

    try:
        response = requests.get(f"{url}{workout_type}", headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return []


# Function to generate workout plan
def generate_workout_plan(exercises, duration):
    # Average time per exercise including rest
    time_per_exercise = 5  # minutes
    number_of_exercises = duration // time_per_exercise

    # Randomly choose exercises
    selected_exercises = random.sample(exercises, number_of_exercises)

    # Create the workout plan
    workout_plan = []
    for exercise in selected_exercises:
        workout_plan.append({
            "name": exercise["name"],
            "target": exercise.get("target", "Not specified"),
            "bodyPart": exercise.get("bodyPart", "Not specified"),
            "equipment": exercise.get("equipment", "None"),
            "gifUrl": exercise.get("gifUrl", "")
        })

    return workout_plan


# Function to create workout plan text
def create_workout_plan_text(workout_plan):
    plan_text = StringIO()
    for exercise in workout_plan:
        plan_text.write(f"Exercise: {exercise['name']}\n")
        plan_text.write(f"Body Part: {exercise['bodyPart']}\n")
        plan_text.write(f"Target Muscle: {exercise['target']}\n")
        plan_text.write(f"Equipment: {exercise['equipment']}\n\n")
    return plan_text.getvalue()


# Streamlit App
# Add image
st.image("workout_logo.png", width=100)
st.title("Workout Plan Generator")

# User Input
workout_type = st.selectbox("Select workout type:", list(WORKOUT_TYPES.keys()))
duration = st.slider("How many minutes do you want to workout?", 10, 60, 30)

# Fetch exercises and generate plan
if st.button("Generate Workout Plan"):
    exercises = fetch_exercises(WORKOUT_TYPES[workout_type], API_KEY)
    if exercises:
        workout_plan = generate_workout_plan(exercises, duration)

        st.subheader("Your Workout Plan:")
        for i, exercise in enumerate(workout_plan):
            st.markdown(f"### Exercise {i + 1}: {exercise['name']}")
            st.markdown(f"- **Body Part**: {exercise['bodyPart']}")
            st.markdown(f"- **Target Muscle**: {exercise['target']}")
            st.markdown(f"- **Equipment**: {exercise['equipment']}")
            if exercise["gifUrl"]:
                st.image(exercise["gifUrl"], width=300)

        # Prepare the workout plan text for saving
        workout_plan_text = create_workout_plan_text(workout_plan)

        # Saving the workout plan
        st.download_button(
            label="Save Workout Plan",
            data=workout_plan_text,
            file_name="workout_plan.txt",
            mime="text/plain"
        )
    else:
        st.error("Failed to fetch exercises. Please try again later.")
