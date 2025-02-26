# place.py
import streamlit as st
import time
import random

def place_order():
    st.markdown("### Placing Order...")
    time.sleep(1)

    # Simulate asking for credit card number
    card_number = st.text_input("Please share your credit card number:")

    if card_number: # Only proceed if input is given.
        st.markdown("### Order Details")
        for key, value in st.session_state.order_details.items():
            st.write(f"{key}: {value}")

        # Simulate generating a fake card number (no real storage)
        fake_card_number = "XXXX-XXXX-XXXX-" + str(random.randint(1000, 9999))
        st.write(f"Fake Card Number Processed: {fake_card_number}")

        st.success("Order Placed Successfully!")
        return "quality_check"
    else:
        st.warning("Please enter your credit card number to proceed.")
        return "place_order" # Stay on the same page until input is given.