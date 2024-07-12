import streamlit as st
from datetime import datetime


st.set_page_config(
    page_title="Meeting Summaries",
)


# Sample data for Google Meets
meetings = [
    {"title": "Project Sync-Up", "datetime": "2023-10-01 10:00:00", "summary": "Discussion on project progress."},
    {"title": "Team Retrospective", "datetime": "2023-10-02 15:00:00", "summary": "Review of the last sprint."},
    {"title": "Client Meeting", "datetime": "2023-10-03 11:00:00", "summary": "Presentation to the client."},
    {"title": "Marketing Strategy", "datetime": "2023-10-04 14:00:00", "summary": "Planning for next quarter."},
    {"title": "Design Review", "datetime": "2023-10-05 09:00:00", "summary": "Critique of the latest design."},
]

def format_datetime(dt_str):
    """Helper function to format datetime string."""
    return datetime.strptime(dt_str, "%Y-%m-%d %H:%M:%S").strftime("%A, %d %B %Y %I:%M %p")

# Title of the Streamlit app
st.title("Google Meets Summary")

# Display the list of meetings
st.header("Upcoming Meetings")
for meeting in meetings[:5]:
    with st.expander(f"{meeting['title']} - {format_datetime(meeting['datetime'])}"):
        if st.button(f"Get Summary for {meeting['title']}", key=meeting['title']):
            st.write(f"**Summary:** {meeting['summary']}")