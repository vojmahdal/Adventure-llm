from google import genai
import os


class GeminiLCChat:
    def __init__(self, model: str = "gemini-3-flash-preview"):
        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            raise ValueError("GEMINI_API_KEY is not set in environment variables")

        self.client = genai.Client(api_key=api_key)
        self.model = model
        
    def _convert_messages(self, messages):
        parts = []

        for msg in messages:
            # LangChain message object support
            role = getattr(msg, "type", None) or getattr(msg, "role", None)
            content = getattr(msg, "content", None)

            # fallback if tuple accidentally passed
            if isinstance(msg, tuple):
                role, content = msg
                role = str(role)

            if role in ("system", "SystemMessage"):
                parts.append(f"System: {content}")
            elif role in ("human", "user", "HumanMessage", "UserMessage"):
                parts.append(f"User: {content}")
            elif role in ("ai", "assistant", "AIMessage", "AssistantMessage"):
                parts.append(f"Assistant: {content}")
            else:
                parts.append(str(content))

        return "\n".join(parts)

    def invoke(self, messages, **kwargs):
        prompt = self._convert_messages(messages)

        response = self.client.models.generate_content(
            model=self.model,
            contents=prompt,
        )

        return response.text

    __call__ = invoke