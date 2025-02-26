# tasks.py
from crewai import Task
from agents import product_researcher, price_comparator, shopping_list_manager, order_placement_agent, user_interface_agent

research_product_task = Task(
    description="Search for products based on the user's request, providing detailed information, prices, and reviews. Use the Tavily API.",
    agent=product_researcher
)

compare_prices_task = Task(
    description="Compare prices from different retailers to identify the best deals and discounts for the selected product.",
    agent=price_comparator
)

update_shopping_list_task = Task(
    description="Update the user's shopping list by adding, removing, or modifying items as requested.",
    agent=shopping_list_manager
)

summarize_shopping_list_task = Task(
    description="Provide a summary of the current items in the user's shopping list.",
    agent=shopping_list_manager
)

place_order_task = Task(
    description="Place the order for the selected product, using the user's stored payment and shipping information.",
    agent=order_placement_agent
)

get_user_request_task = Task(
    description="Get the user's shopping request and translate it into a format that the other agents can understand.",
    agent=user_interface_agent
)

present_results_task = Task(
    description="Present the results of the product search and price comparison to the user in a clear and concise manner.",
    agent=user_interface_agent
)

get_user_feedback_task = Task(
    description="Get the user's feedback on the presented results and any additional requests or modifications.",
    agent=user_interface_agent
)

present_order_confirmation_task = Task(
    description="Present the order confirmation to the user and provide order tracking information.",
    agent=user_interface_agent
)
