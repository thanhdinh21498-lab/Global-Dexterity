from pathlib import Path

import pandas as pd
import streamlit as st
import csv
from datetime import datetime


# ---------- PATHS ----------
BASE_DIR = Path(__file__).resolve().parent
CSV_PATH = BASE_DIR / "survey_data.csv"      # rename your file to this
IMG_DIR = BASE_DIR / "images"


# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="Global Dexterity – A Way of Disagreeing and Giving Feedback Across Cultures",
    layout="wide",
)


# ---------- SIDEBAR ----------
with st.sidebar:
    st.title("About this project")
    st.write(
        "BUS 222F – Global Dexterity\n\n"
        "Situation:\n"
        "Disagreeing and giving critical feedback across cultures\n"
        "(Vietnamese, American, International)."
    )

    st.subheader("My Mentor")
    mentor_path = IMG_DIR / "mentor_linh.jpg"
    if mentor_path.exists():
        st.image(
            mentor_path,
            caption="Coach Le Ba Nam Linh (HNBA & Zeit Media)",
            use_container_width=True,
        )
    else:
        st.info("Add images/mentor_linh.jpg to show a mentor photo here.")


# ---------- TITLE ----------
st.header("For folks having situation with small talk")
with st.expander("Some examples to encourage you guys!                ------                press here to see more"):
    st.write("Try to step out and talk to high profile people but make sure you know what to talk about")
    Tatum_path = IMG_DIR / "Tatum.jpg"
    if Tatum_path.exists():
        st.image(
            Tatum_path,
            caption="Jayson Tatum with a big smile",
            use_container_width=True,
        )
    else:
        st.info("Add images/Tatum.jpg to show Tatum photo here.")
    
    Rob_path = IMG_DIR / "Rob.jpg"
    if Rob_path.exists():
        st.image(
            Rob_path,
            caption="Robert Hale Jr - Co-owner of the Boston Celtics",
            use_container_width=True,
        )
    else:
        st.info("Add images/Rob.jpg to show Tatum photo here.")
    

st.title("Disagreeing or Giving Critical Feedback Across Cultures")

st.markdown(
    """
This Streamlit site is my final interactive project for **BUS 222F – Global Dexterity**.  
I worked on a situation where I often feel uncomfortable: **disagreeing or giving critical feedback**.
"""
)


# ---------- SECTION 1: MY SITUATION ----------
st.header("1. My Situation")

st.write(
    """
I grew up in Vietnam, where people usually avoid open disagreement to keep peace and respect.  
Because of this, I often find it hard to give feedback directly in group work or class.  
In the U.S., I noticed that people expect clearer and more honest feedback and see it as teamwork,
not rudeness. This cultural gap is what I worked on in this project.
"""
)


# ---------- SECTION 2: LOAD AND SHOW SURVEY DATA ----------
st.header("2. Cultural Expectations Survey")
# ----- PIE CHART IMAGE (optional visual summary) -----
pie_chart_path = BASE_DIR / "chart" / "Backgroup.jpg"

if pie_chart_path.exists():
    st.subheader("Where did survey participants grow up?")
    st.image(pie_chart_path, use_container_width=True)
    st.write(
        """
        This chart shows the distribution of survey participants by where they grew up.
        Having respondents from Vietnam, the U.S., India, Brazil, and Albania adds 
        cultural diversity to the feedback patterns we observe later.
        """
    )
else:
    st.info("Add chart/backgroup.jpg to show the pie chart here.")


if CSV_PATH.exists():
    df = pd.read_csv(CSV_PATH)

    st.write(
        """
I created a short survey for Vietnamese, American, and International participants about how they
prefer to give and receive feedback. Here is the raw data from the Google Form:
        """
    )

    st.dataframe(df, use_container_width=True)

    # Column names from your CSV
    COL_COUNTRY = "Where did you grow up?"
    COL_COMFORT = "How comfortable are you with direct disagreement during group work?"
    COL_DIRECTNESS = "How direct do you think feedback should be?"
    COL_SAVING_FACE = "How important is “saving face” (not embarrassing someone) when giving feedback?"
    COL_ACCEPT_HIGHER = "In your culture, how acceptable is it to disagree with someone older or higher status?"

    # ---- Summary by country (for the 4 main questions) ----
    metrics = [COL_COMFORT, COL_DIRECTNESS, COL_SAVING_FACE, COL_ACCEPT_HIGHER]

    summary = (
        df.groupby(COL_COUNTRY)[metrics]
        .mean()
        .reset_index()
    )

    st.subheader("Average Scores by Country (from 1 to 5)")
    st.dataframe(summary, use_container_width=True)

    st.subheader("Line Chart – Cultural Differences")
    st.markdown(
        """
The chart below shows how people from different countries answered key questions about feedback.
Each line represents one question, and the x-axis shows where respondents grew up.
        """
    )

    # Set country as index so Streamlit uses it on x-axis
    st.line_chart(summary.set_index(COL_COUNTRY))

else:
    st.error(
        "Could not find 'survey_data.csv'. "
        "Place your exported Google Form file in the same folder as app.py and rename it to 'survey_data.csv'."
    )


# ---------- SECTION 3: INTERPRETING THE DATA ----------
st.header("3. What the Data Suggests")

st.write(
    """
From the survey, I noticed some patterns:

- **Comfort with disagreement** and **directness** tend to be higher for American and Brazilian.  
- **Saving face** is more important on average for people from Vietnam and India.  
- Acceptability of disagreeing with someone older or higher status also varies by culture but can easily see that Asian feel more uncomfortable on this.

These patterns match my own experience: my Vietnamese background makes me more cautious,
especially about embarrassing others or challenging someone with higher status.
"""
)


# ---------- SECTION 4: MY PRACTICE ATTEMPTS ----------
st.header("4. My Practice Attempts (Diary Highlights)")

st.write(
    """
I practiced giving feedback at least three times in real situations (group projects and discussions).
Here are short summaries from my diary.
"""
)

with st.expander("Attempt 1 – Very nervous, softened my message                ------                press here to see more"):
    st.write(
        """
- I disagreed with a teammate but used very soft language and spoke quietly.  
- I worried a lot about hurting their feelings.  
- They understood my point, but my message was not very clear.  
- I realized I was still holding back because of my fear of conflict.
        """
    )

with st.expander("Attempt 2 – Used a simple feedback phrase                ------                press here to see more"):
    st.write(
        """
- I used a phrase like: *“I see your point, but maybe we can try…”*  
- I was more direct, but still respectful.  
- My teammate actually appreciated the suggestion and we improved the slide.  
- This made me see that clear feedback can be seen as helpful, not rude.
        """
    )

with st.expander("Attempt 3 – More confident and better timing                ------                press here to see more"):
    st.write(
        """
- I chose a good moment after the meeting to share my feedback one-on-one.  
- I kept it short and focused on the work, not the person.  
- The conversation felt more like collaboration than conflict.  
- I felt more authentic and a bit more confident than before.
        """
    )


# ---------- SECTION 5: BEFORE VS AFTER ----------
st.header("5. Before vs. After")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Before the Project")
    st.write(
        """
- Stayed quiet when I disagreed.  
- Very indirect language.  
- Focused mainly on not upsetting anyone.  
- Often felt frustrated afterwards for not speaking up.
        """
    )

with col2:
    st.subheader("After the Project")
    st.write(
        """
- Speak up more often in group work.  
- Use simple and clear feedback phrases.  
- Still keep tone and respect in mind (especially saving face).  
- Feel more balanced between honesty and harmony.
        """
    )


# ---------- SECTION 6: FINAL REFLECTION ----------
st.header("6. What I Learned About Global Dexterity")

st.write(
    """
Working on this situation showed me how strongly culture shapes our comfort with disagreement
and feedback. Through reading *Global Dexterity* (most of it), talking with my mentor
Coach Le Ba Nam Linh and my Brandeis cohort, collecting survey data, and practicing in real life, I learned that:

- It is possible to be more direct **and** still be myself.  
- Customizing my language (for example, using gentle openers) helps bridge Vietnamese and U.S. expectations.  
- Understanding the “cultural code” makes adaptation feel less scary and more logical.  

This project helped me build a small but important new skill: I can now disagree and give feedback
in a clearer way while keeping respect and relationships in mind.
"""
)

# ---------- SECTION 7: FEEDBACK FORM ----------
st.header("7. Now Is Your Turn To Give Feedback!!!!!!")

st.write("I would love to hear any comments or suggestions about this project. Don't force yourself to hard, take it easy on me ^^")

with st.form("feedback_form"):
    name = st.text_input("Name (optional)")
    role = st.selectbox(
        "Who are you?",
        ["Professor", "Classmate", "Friend", "Other"],
        index=1,
    )
    rating = st.slider("How clear was this project?", 1, 5, 4)
    rating = st.slider("How good was this project?", 1, 5, 4)
    comments = st.text_area("Any feedback or suggestions?")

    submitted = st.form_submit_button("Submit feedback")

if submitted:
    feedback_file = BASE_DIR / "feedback.csv"
    new_row = [
        datetime.now().isoformat(timespec="seconds"),
        name,
        role,
        rating,
        comments,
    ]
    file_exists = feedback_file.exists()

    with feedback_file.open("a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["timestamp", "name", "role", "rating", "comments"])
        writer.writerow(new_row)

    st.success("Thank you for your feedback! 🙏")


st.success("Thank you for viewing my Global Dexterity project!")
















