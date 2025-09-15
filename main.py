import os
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)


def main():
    parser = argparse.ArgumentParser(description="Generate content using Gemini API")
    parser.add_argument("prompt", help="The prompt/content to send to the model")
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Print extra token and prompt metadata",
    )

    args = parser.parse_args()
    messages = [
        types.Content(role="user", parts=[types.Part(text=args.prompt)]),
    ]

    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
    )
    print(response.text)
    if args.verbose:
        prompt_tokens = response.usage_metadata.prompt_token_count
        response_tokens = response.usage_metadata.candidates_token_count
        print(f"User prompt: {args.prompt}")
        print(f"Prompt tokens: {prompt_tokens}")
        print(f"Response tokens: {response_tokens}")


if __name__ == "__main__":
    main()
