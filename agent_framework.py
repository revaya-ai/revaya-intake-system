"""
Custom Agent Framework for Winnicki Digital
Provides parallel and sequential agent execution patterns
"""

import os
from google import genai
from google.genai import types
from typing import List, Dict, Any, Optional
from concurrent.futures import ThreadPoolExecutor, as_completed
import json

# Lazy client initialization
_client = None

def get_client():
    """Get or create the Gemini client (lazy initialization)"""
    global _client
    if _client is None:
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            raise ValueError("GOOGLE_API_KEY environment variable is required")
        _client = genai.Client(api_key=api_key)
    return _client


class Agent:
    """Base agent class with Google Search grounding for real-time web research"""

    def __init__(self, name: str, instructions: str, output_key: str, tools: Optional[List] = None, enable_search: bool = True):
        self.name = name
        self.instructions = instructions
        self.output_key = output_key
        self.tools = tools or []
        self.enable_search = enable_search
        self.model = "gemini-2.5-flash"

    def run(self, context: str, shared_state: Optional[Dict] = None) -> Dict[str, Any]:
        """
        Run the agent with given context
        Uses Google Search grounding for real-time web research
        Returns dict with output_key: result
        """
        shared_state = shared_state or {}

        # Build the prompt with instructions and context
        prompt = f"""
{self.instructions}

CONTEXT:
{context}

SHARED STATE (outputs from previous agents):
{json.dumps(shared_state, indent=2)}

Please provide your analysis in markdown format. When researching people or companies online, include the sources you found.
"""

        try:
            # Configure Google Search grounding if enabled
            config = None
            if self.enable_search:
                google_search_tool = types.Tool(google_search=types.GoogleSearch())
                config = types.GenerateContentConfig(tools=[google_search_tool])

            # Generate response with search grounding
            response = get_client().models.generate_content(
                model=self.model,
                contents=prompt,
                config=config
            )
            result = response.text

            return {
                self.output_key: result,
                "agent_name": self.name,
                "success": True
            }

        except Exception as e:
            return {
                self.output_key: f"Error in {self.name}: {str(e)}",
                "agent_name": self.name,
                "success": False,
                "error": str(e)
            }


class ParallelAgent:
    """Runs multiple agents in parallel"""

    def __init__(self, name: str, sub_agents: List[Agent]):
        self.name = name
        self.sub_agents = sub_agents

    def run(self, context: str, shared_state: Optional[Dict] = None) -> Dict[str, Any]:
        """Run all sub-agents in parallel"""
        shared_state = shared_state or {}
        results = {}

        with ThreadPoolExecutor(max_workers=len(self.sub_agents)) as executor:
            # Submit all agents
            future_to_agent = {
                executor.submit(agent.run, context, shared_state): agent
                for agent in self.sub_agents
            }

            # Collect results
            for future in as_completed(future_to_agent):
                agent = future_to_agent[future]
                try:
                    result = future.result()
                    results.update(result)
                except Exception as e:
                    results[agent.output_key] = f"Error in {agent.name}: {str(e)}"

        return results


class SequentialAgent:
    """Runs multiple agents sequentially, passing state between them"""

    def __init__(self, name: str, sub_agents: List):
        self.name = name
        self.sub_agents = sub_agents

    def run(self, context: str) -> Dict[str, Any]:
        """Run all sub-agents in sequence, accumulating state"""
        shared_state = {}

        for agent in self.sub_agents:
            result = agent.run(context, shared_state)
            # Accumulate results in shared state
            shared_state.update(result)

        return shared_state


# Tool functions that agents can use
# Note: google_search is now handled natively by Gemini's Google Search grounding

def web_fetch(url: str) -> str:
    """
    Fetch and analyze a website
    """
    try:
        import httpx
        from bs4 import BeautifulSoup

        response = httpx.get(url, timeout=10, follow_redirects=True)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract key information
        title = soup.find('title')
        title_text = title.get_text() if title else "No title"

        # Get meta description
        meta_desc = soup.find('meta', attrs={'name': 'description'})
        description = meta_desc.get('content') if meta_desc else "No description"

        # Get headings
        headings = [h.get_text().strip() for h in soup.find_all(['h1', 'h2', 'h3'])[:10]]

        # Get main text content
        paragraphs = [p.get_text().strip() for p in soup.find_all('p')[:15] if p.get_text().strip()]

        return f"""
Website: {url}
Title: {title_text}
Description: {description}

Main Headings:
{chr(10).join(f"- {h}" for h in headings if h)}

Content Preview:
{chr(10).join(paragraphs[:5])}

Status Code: {response.status_code}
"""
    except Exception as e:
        return f"Error fetching {url}: {str(e)}"
