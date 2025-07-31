import re
from typing import Dict
from config.settings import CATEGORIES


def generate_prompt(name: str, purpose: str, capabilities: str, returns: str, final_only: bool = True) -> str:
    """Generate a standardized prompt for agents."""
    parts = [
        f"You are {name}.",
        f"Purpose: {purpose}",
        "Capabilities:",
        *[f"- {c.strip()}" for c in capabilities.split(';') if c.strip()],
        "Returns:",
        *[f"- {r.strip()}" for r in returns.split(';') if r.strip()],
        "Only output the final result in plain text."
    ]
    
    if final_only:
        parts.append("Do not show any code, plan, or explanation.")
    parts.append("If you cannot respond, return 'NO_RESPONSE'.")
    
    return "\n".join(parts)


def parse_router_output(raw_outputs: str) -> Dict[str, str]:
    """Parse router output and organize by categories."""
    output_dict = {cat: [] for cat in CATEGORIES}
    
    # split into blocks by category headers
    blocks = re.split(r'\n(?=[A-Za-z]+:)', raw_outputs.strip())

    for block in blocks:
        match = re.match(r'([A-Za-z]+):\s*(.*)', block, re.DOTALL)
        if not match:
            continue
            
        category, content = match.groups()
        category = category.strip().capitalize()

        if category not in output_dict:
            continue

        # extraction
        bracket_sentences = re.findall(r'\[([^\[\]]+?)\]', content)
        dash_sentences = re.findall(r'-\s*([^\n]+)', content)

        # cleanup
        all_sentences = bracket_sentences + dash_sentences

        for sentence in all_sentences:
            sentence = sentence.replace(']', "").replace('[', "").strip().rstrip('.').lower()
            if sentence and sentence not in output_dict[category]:
                output_dict[category].append(sentence)

    return {k: ', & '.join(v) for k, v in output_dict.items()}


def invoke_agent(input_text: str, weather_text: str, prompt_type: str, agent_type: str, agent) -> str:
    """Invoke an agent with enriched context."""
    enriched = f"{prompt_type}\nWeather: {weather_text}\nUser: {input_text}"
    print(f"\n[Invoking {agent_type} Agent]")
    
    response = agent.run(enriched).strip()
    print(f"\n[{agent_type} Agent Response]", response)
    
    return response if response != 'NO_RESPONSE' else ""
