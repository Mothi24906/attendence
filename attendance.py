import streamlit as st

# Set page configuration
st.set_page_config(page_title="Attendance Calculator", layout="centered")

# Apply custom CSS for white background
st.markdown(
    """
    <style>
        body {
            background-color: white !important;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Title
st.title("🎓 Attendance Calculator")

# Inputs
percentage_required = st.number_input("Enter the percentage required:", min_value=0, max_value=100, value=75)
attended = st.number_input("Enter the number of classes present:", min_value=0, value=0)
total_classes = st.number_input("Enter the total number of classes:", min_value=0, value=0)

# Calculate Attendance
if total_classes > 0:
    attendance_percentage = (attended / total_classes) * 100
else:
    attendance_percentage = 0  # Avoid division by zero

# Display Results
st.write(f"📊 **Current Attendance:** {attended}/{total_classes} → **{attendance_percentage:.2f}%**")

if percentage_required > 0 and total_classes > 0:
    required_classes = attended / (percentage_required / 100)
    bunkable_classes = max(0, round(required_classes - total_classes))  # Rounded to nearest integer
    st.write(f"💡 **You can bunk:** {bunkable_classes} more classes")
else:
    st.write("⚠️ Enter valid values.")

