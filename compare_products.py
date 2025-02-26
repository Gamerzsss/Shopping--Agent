# compare_products.py
import streamlit as st
from agents import user_interface_agent

def compare_products():
    st.markdown("### Compare Products")
    product1 = st.text_input("Enter the name of the first product to compare:")
    product2 = st.text_input("Enter the name of the second product to compare:")

    if st.button("Compare"):
        if product1 and product2:
            st.markdown("### Comparison Results:")
            with st.spinner("Comparing products..."):
                comparison_result = user_interface_agent.run(f"Compare {product1} with {product2}")
                st.write(comparison_result)
            return "intent_prompt"  # Go back to the main menu
        else:
            st.warning("Please enter both product names.")
            return "compare_products" # stay on compare page.
    else:
        return "compare_products" # stay on compare page.