import streamlit as st

# App Title
st.title("Simple Calculator")

# Input Numbers
num1 = st.number_input("Enter the first number", value=0.0)
num2 = st.number_input("Enter the second number", value=0.0)

# Operation Selection
operation = st.selectbox("Select an operation", ["Add", "Subtract", "Multiply", "Divide"])

# Perform Calculation
if st.button("Calculate"):
    if operation == "Add":
        result = num1 + num2
        st.success(f"The result is: {result}")

    elif operation == "Subtract":
        result = num1 - num2
        st.success(f"The result is: {result}")

    elif operation == "Multiply":
        result = num1 * num2
        st.success(f"The result is: {result}")

    elif operation == "Divide":
        if num2 != 0:
            result = num1 / num2
            st.success(f"The result is: {result}")
        else:
            st.error("Error: Division by zero is not allowed.")
