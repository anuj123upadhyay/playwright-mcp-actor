"""
Template system for pre-built automation workflows
"""

from typing import List, Dict, Any, Optional
from dataclasses import dataclass
from enum import Enum


class TemplateType(str, Enum):
    """Available template types"""
    AMAZON_PRODUCT_SEARCH = "amazon_product_search"
    GOOGLE_SEARCH = "google_search"
    LINKEDIN_PROFILE = "linkedin_profile"
    TWITTER_SCRAPE = "twitter_scrape"
    GOOGLE_MAPS_BUSINESS = "google_maps_business"


@dataclass
class Template:
    """Template definition"""
    name: str
    description: str
    parameters: Dict[str, Any]
    actions: List[Dict[str, Any]]


class TemplateManager:
    """Manages pre-built templates"""
    
    @staticmethod
    def get_template(template_type: str, params: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Get actions for a specific template"""
        
        if template_type == "amazon_product_search":
            return TemplateManager._amazon_product_search(params)
        elif template_type == "google_search":
            return TemplateManager._google_search(params)
        elif template_type == "linkedin_profile":
            return TemplateManager._linkedin_profile(params)
        elif template_type == "twitter_scrape":
            return TemplateManager._twitter_scrape(params)
        elif template_type == "google_maps_business":
            return TemplateManager._google_maps_business(params)
        else:
            raise ValueError(f"Unknown template: {template_type}")
    
    @staticmethod
    def _amazon_product_search(params: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Amazon product search template"""
        search_query = params.get("search_query", "")
        max_results = params.get("max_results", 20)
        extract_reviews = params.get("extract_reviews", False)
        
        if not search_query:
            raise ValueError("search_query is required for amazon_product_search template")
        
        actions = [
            {
                "type": "navigate",
                "value": "https://www.amazon.com"
            },
            {
                "type": "fill",
                "selector": "input[name='field-keywords']",
                "value": search_query
            },
            {
                "type": "press_key",
                "selector": "input[name='field-keywords']",
                "value": "Enter"
            },
            {
                "type": "wait_for_element",
                "selector": ".s-result-item[data-component-type='s-search-result']",
                "timeout": 10000
            },
            {
                "type": "evaluate",
                "value": f"""
                Array.from(document.querySelectorAll('.s-result-item[data-component-type="s-search-result"]'))
                    .slice(0, {max_results})
                    .map(item => ({{
                        title: item.querySelector('h2 a span')?.innerText || '',
                        price: item.querySelector('.a-price-whole')?.innerText || 'N/A',
                        rating: item.querySelector('.a-icon-alt')?.innerText || 'N/A',
                        reviews: item.querySelector('.a-size-base.s-underline-text')?.innerText || '0',
                        url: item.querySelector('h2 a')?.href || '',
                        image: item.querySelector('img.s-image')?.src || '',
                        asin: item.getAttribute('data-asin') || ''
                    }}))
                """
            },
            {
                "type": "screenshot"
            }
        ]
        
        return actions
    
    @staticmethod
    def _google_search(params: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Google search template"""
        search_query = params.get("search_query", "")
        max_results = params.get("max_results", 10)
        
        if not search_query:
            raise ValueError("search_query is required for google_search template")
        
        return [
            {
                "type": "navigate",
                "value": f"https://www.google.com/search?q={search_query}"
            },
            {
                "type": "wait_for_element",
                "selector": "#search",
                "timeout": 10000
            },
            {
                "type": "evaluate",
                "value": f"""
                Array.from(document.querySelectorAll('.g'))
                    .slice(0, {max_results})
                    .map(item => ({{
                        title: item.querySelector('h3')?.innerText || '',
                        url: item.querySelector('a')?.href || '',
                        description: item.querySelector('.VwiC3b')?.innerText || ''
                    }}))
                """
            },
            {
                "type": "screenshot"
            }
        ]
    
    @staticmethod
    def _linkedin_profile(params: Dict[str, Any]) -> List[Dict[str, Any]]:
        """LinkedIn profile scraper template"""
        profile_url = params.get("profile_url", "")
        
        if not profile_url:
            raise ValueError("profile_url is required for linkedin_profile template")
        
        return [
            {
                "type": "navigate",
                "value": profile_url
            },
            {
                "type": "wait_for_element",
                "selector": ".pv-top-card",
                "timeout": 15000
            },
            {
                "type": "evaluate",
                "value": """
                {
                    name: document.querySelector('.pv-top-card--list li:first-child')?.innerText || '',
                    headline: document.querySelector('.pv-top-card--list li:nth-child(2)')?.innerText || '',
                    location: document.querySelector('.pv-top-card--list.pv-top-card--list-bullet li:first-child')?.innerText || '',
                    connections: document.querySelector('.pv-top-card--list.pv-top-card--list-bullet li:nth-child(2)')?.innerText || '',
                    about: document.querySelector('.pv-about__summary-text')?.innerText || ''
                }
                """
            },
            {
                "type": "screenshot"
            }
        ]
    
    @staticmethod
    def _twitter_scrape(params: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Twitter/X profile scraper template"""
        username = params.get("username", "")
        max_tweets = params.get("max_tweets", 10)
        
        if not username:
            raise ValueError("username is required for twitter_scrape template")
        
        return [
            {
                "type": "navigate",
                "value": f"https://twitter.com/{username}"
            },
            {
                "type": "wait_for_element",
                "selector": "article",
                "timeout": 10000
            },
            {
                "type": "scroll",
                "value": "1000"
            },
            {
                "type": "wait",
                "value": "2000"
            },
            {
                "type": "evaluate",
                "value": f"""
                Array.from(document.querySelectorAll('article'))
                    .slice(0, {max_tweets})
                    .map(tweet => ({{
                        text: tweet.querySelector('[data-testid="tweetText"]')?.innerText || '',
                        timestamp: tweet.querySelector('time')?.getAttribute('datetime') || '',
                        likes: tweet.querySelector('[data-testid="like"]')?.innerText || '0',
                        retweets: tweet.querySelector('[data-testid="retweet"]')?.innerText || '0',
                        replies: tweet.querySelector('[data-testid="reply"]')?.innerText || '0'
                    }}))
                """
            },
            {
                "type": "screenshot"
            }
        ]
    
    @staticmethod
    def _google_maps_business(params: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Google Maps business scraper template"""
        search_query = params.get("search_query", "")
        location = params.get("location", "")
        
        if not search_query:
            raise ValueError("search_query is required for google_maps_business template")
        
        search_url = f"https://www.google.com/maps/search/{search_query}"
        if location:
            search_url += f"+{location}"
        
        return [
            {
                "type": "navigate",
                "value": search_url
            },
            {
                "type": "wait_for_element",
                "selector": "[role='article']",
                "timeout": 10000
            },
            {
                "type": "wait",
                "value": "3000"
            },
            {
                "type": "evaluate",
                "value": """
                Array.from(document.querySelectorAll('[role="article"]'))
                    .slice(0, 20)
                    .map(item => ({
                        name: item.querySelector('.fontHeadlineSmall')?.innerText || '',
                        rating: item.querySelector('.MW4etd')?.innerText || 'N/A',
                        reviews: item.querySelector('.UY7F9')?.innerText || '0',
                        address: item.querySelector('.W4Efsd:nth-of-type(2)')?.innerText || '',
                        type: item.querySelector('.W4Efsd:first-of-type')?.innerText || '',
                        phone: item.querySelector('[data-tooltip="Copy phone number"]')?.innerText || ''
                    }))
                """
            },
            {
                "type": "screenshot"
            }
        ]
    
    @staticmethod
    def list_templates() -> List[Dict[str, str]]:
        """List all available templates"""
        return [
            {
                "name": "amazon_product_search",
                "description": "Search Amazon products and extract details",
                "parameters": ["search_query", "max_results", "extract_reviews"]
            },
            {
                "name": "google_search",
                "description": "Perform Google search and extract results",
                "parameters": ["search_query", "max_results"]
            },
            {
                "name": "linkedin_profile",
                "description": "Extract LinkedIn profile information",
                "parameters": ["profile_url"]
            },
            {
                "name": "twitter_scrape",
                "description": "Scrape tweets from a Twitter/X profile",
                "parameters": ["username", "max_tweets"]
            },
            {
                "name": "google_maps_business",
                "description": "Search and extract Google Maps business listings",
                "parameters": ["search_query", "location"]
            }
        ]
