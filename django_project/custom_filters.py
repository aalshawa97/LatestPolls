# custom_filters.py

from django import template

register = template.Library()

@register.filter
def calculate_percentage(votes, total_votes):
    if total_votes == 0:
        return 0
    return votes * 100 / total_votes
