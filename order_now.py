# order_now.py
import streamlit as st
from agents import product_researcher

def order_now(user_input):
    st.markdown("### Researching Product Details...")
    with st.spinner("Fetching product info..."):
        research_result = product_researcher.run(user_input)
        if research_result:
            st.markdown("### Product Details:")
            st.write(research_result)

            if st.button("Place Order"):
                st.session_state.order_details = {
                    "product": user_input,
                    "price": "Simulated Price: $99.99",
                    "shipping_address": "Simulated Address",
                    "order_number": "Simulated Order #12345",
                    "product_details": research_result,
                }
                st.session_state.stage = "place_order"  # Directly set the stage
                st.rerun()  # Force rerun.
            else:
                return "intent_prompt"
        else:
            st.error("Could not retrieve product information.")
            return "intent_prompt"