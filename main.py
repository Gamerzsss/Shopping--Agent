# main.py
import streamlit as st
from agents import quality_inspection_agent, shipping_agent, after_sales_agent
from order_now import order_now
from compare_products import compare_products
from get_product_details import get_product_details
from place import place_order

def run_agent(agent, query):
    try:
        result = agent.run(query)
        return result
    except Exception as e:
        st.error(f"Agent error: {e}")
        return f"An agent error occurred: {e}"

st.title("MBZ Virtual Shopper")

# Session State Initialization
if "shopping_list" not in st.session_state:
    st.session_state.shopping_list = []
if "user_preferences" not in st.session_state:
    st.session_state.user_preferences = {}
if "stage" not in st.session_state:
    st.session_state.stage = "input"
if "research_result" not in st.session_state:
    st.session_state.research_result = None
if "comparison_result" not in st.session_state:
    st.session_state.comparison_result = None
if "order_details" not in st.session_state:
    st.session_state.order_details = {}
if "relevant_products" not in st.session_state:
    st.session_state.relevant_products = []
if "selected_product" not in st.session_state:
    st.session_state.selected_product = None
if "product_images" not in st.session_state:
    st.session_state.product_images = {}

# Stage-based Logic
if st.session_state.stage == "input":
    st.markdown("### Enter Your Shopping Request")
    user_input = st.text_input("What are you looking for?")
    if st.button("Search"):
        if user_input:
            st.session_state.stage = "intent_prompt"
            st.session_state.user_input = user_input
        else:
            st.warning("Please enter a shopping request.")

elif st.session_state.stage == "intent_prompt":
    st.markdown("### What would you like to do?")
    if st.button("Get Details"):
        st.session_state.stage = "details"
    elif st.button("Compare Products"):
        st.session_state.stage = "compare_products"
    elif st.button("Order Now"):
        st.session_state.stage = "order_now"

elif st.session_state.stage == "order_now":
    order_now(st.session_state.user_input) # no need to check return.

elif st.session_state.stage == "compare_products":
    new_stage = compare_products()
    if new_stage:
        st.session_state.stage = new_stage

elif st.session_state.stage == "details":
    new_stage = get_product_details(st.session_state.user_input)
    if new_stage:
        st.session_state.stage = new_stage

elif st.session_state.stage == "place_order":
    new_stage = place_order()
    if new_stage:
        st.session_state.stage = new_stage

elif st.session_state.stage == "quality_check":
    st.markdown("### Quality Check")
    with st.spinner("Inspecting product..."):
        result = run_agent(quality_inspection_agent, st.session_state.selected_product if st.session_state.selected_product else st.session_state.user_input)
        if result:
            st.success(f"Quality Inspection: {result}")
            st.session_state.stage = "shipping"

elif st.session_state.stage == "shipping":
    st.markdown("### Shipping")
    with st.spinner("Arranging shipping..."):
        result = run_agent(shipping_agent, st.session_state.selected_product if st.session_state.selected_product else st.session_state.user_input)
        if result:
            st.success(f"Shipping Arrangement: {result}")
            st.session_state.stage = "after_sales"

elif st.session_state.stage == "after_sales":
    st.markdown("### After-Sales Service")
    st.success("After-sales service completed.")
    st.session_state.stage = "input"
    st.session_state.user_preferences = {}
    st.session_state.shopping_list = []
    st.session_state.relevant_products = []
    st.session_state.selected_product = None
    st.session_state.product_images = {}
    st.session_state.research_result = None
    st.session_state.comparison_result = None
    st.session_state.order_details = {}