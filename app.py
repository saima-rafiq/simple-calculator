import streamlit as st

# Title of the app
st.title("Simple Calculator")

# Input fields for the two numbers
num1 = st.number_input("Enter the first number:", value=0.0)
num2 = st.number_input("Enter the second number:", value=0.0)

# Dropdown for selecting the operation
operation = st.selectbox("Select operation:", ["Add", "Subtract", "Multiply", "Divide"])

# Button to calculate the result
if st.button("Calculate"):
    if operation == "Add":
        result = num1 + num2
    elif operation == "Subtract":
        result = num1 - num2
    elif operation == "Multiply":
        result = num1 * num2
    elif operation == "Divide":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Cannot divide by zero!"
    
    # Display the result
    st.write(f"Result: {result}")

# Footer
st.write("Made with Streamlit")

