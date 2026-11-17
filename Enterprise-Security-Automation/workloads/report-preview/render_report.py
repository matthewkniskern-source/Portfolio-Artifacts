"""Synthetic HTML preview for future governance dashboard; no network or credentials."""
from jinja2 import Environment, select_autoescape

def render(title, decision):
    env = Environment(autoescape=select_autoescape(default_for_string=True))
    template = env.from_string("<h1>{{ title }}</h1><p>{{ decision }}</p>")
    return template.render(title=title, decision=decision)

if __name__ == "__main__":
    print(render("Synthetic lab report", "REVIEW REQUIRED"))
