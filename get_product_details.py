# get_product_details.py
import streamlit as st
from agents import user_interface_agent, product_researcher

def get_product_details(user_input):
    st.markdown("### Getting Product Details...")
    details_query = st.text_input("Enter your specific question about the product:")
    if st.button("Get Details"):
        if details_query:
            details_result = user_interface_agent.run(f"Provide details about {user_input} based on this question: {details_query}")
            st.success(details_result)

        # Add the "Order Now" button here
        if st.button("Order Now"):
            st.markdown("### Getting Product Information...")
            with st.spinner("Fetching product info..."):
                research_result = product_researcher.run(user_input)
                if research_result:
                    st.session_state.order_details = {
                        "product": user_input,
                        "price": "Simulated Price: $99.99",
                        "shipping_address": "Simulated Address",
                        "order_number": "Simulated Order #12345",
                        "product_details": research_result,
                    }
                    return "place_order"
                else:
                    st.error("Could not retrieve product information.")
                    return "intent_prompt"
        else:
            return "intent_prompt"

    return "details"