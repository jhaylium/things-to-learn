get_price = """
Task:
Go to the specified website and retrieve the current price of the given item.

Navigate to:
{url}

Search the page for the product titled: {item}

Locate and extract the price displayed for this item (including the currency symbol).

Return the result in the following JSON format:

{{
  "item_name": "{item}"
  "price": "string",
  "currency": "string",
  "source_url": "{url}",
  "timestamp": "ISO8601 datetime"
}}

If the price is not found, return: 
{{
  "error": "Price not found",
  "source_url": "{url}",
}}

Requirements:

Retrieve only publicly visible data.

Do not log in, submit forms, or add the item to cart.

Use the visible price on the page as it appears to an average user.

"""