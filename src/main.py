from static_to_public import clear_destination, static_to_public
from generate_pages_recursive import generate_pages_recursive
clear_destination("public")
static_to_public("static", "public")
generate_pages_recursive("content", "template.html", "public")
