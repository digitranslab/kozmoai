from textwrap import dedent

from kozmoai.components.data import URLComponent
from kozmoai.components.inputs import TextInputComponent
from kozmoai.components.models import OpenAIModelComponent
from kozmoai.components.outputs import ChatOutput
from kozmoai.components.processing import ParseDataComponent
from kozmoai.components.prompts import PromptComponent
from kozmoai.graph import Graph


def blog_writer_graph(template: str | None = None):
    if template is None:
        template = dedent("""Reference 1:

{references}

---

{instructions}

Blog:
""")
    url_component = URLComponent()
    url_component.set(urls=["https://kozmoai.cloud/", "https://docs.kozmoai.cloud/"])
    parse_data_component = ParseDataComponent()
    parse_data_component.set(data=url_component.fetch_content)

    text_input = TextInputComponent(_display_name="Instructions")
    text_input.set(
        input_value="Use the references above for style to write a new blog/tutorial about Kozmoai and AI. "
        "Suggest non-covered topics."
    )

    prompt_component = PromptComponent()
    prompt_component.set(
        template=template,
        instructions=text_input.text_response,
        references=parse_data_component.parse_data,
    )

    openai_component = OpenAIModelComponent()
    openai_component.set(input_value=prompt_component.build_prompt)

    chat_output = ChatOutput()
    chat_output.set(input_value=openai_component.text_response)

    return Graph(start=text_input, end=chat_output)
