import markdown

def render_markdown(md_text):
    """
    Renders the given markdown as HTML.
    
    NOTE: Always use this instead of directly interacting with the markdown module.
    """
    return markdown.markdown(md_text, ['codehilite'])
