from .llm_service import call_llm


def clean_text(text):
    cleaned = " ".join(text.split())

    return {
        "content": cleaned,
        "tokens": 0,  # no LLM used
        "status": "success"
    }


def summarize(text):
    prompt = f"Summarize this text:\n\n{text}"
    return call_llm(prompt)


def extract_key_points(text):
    prompt = f"Extract key points from this text:\n\n{text}"
    return call_llm(prompt)


def tag_category(text):
    prompt = f"Give a category for this text:\n\n{text}"
    return call_llm(prompt)


STEP_FUNCTIONS = {
    "clean_text": clean_text,
    "summarize": summarize,
    "extract_key_points": extract_key_points,
    "tag_category": tag_category,
}
