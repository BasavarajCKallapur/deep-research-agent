import gradio as gr
from dotenv import load_dotenv
from research_manager import ResearchManager
from styles import CSS, JS, EXAMPLES, HEADER_HTML

load_dotenv(override=True)


async def get_questions(query: str):
    result = await ResearchManager().get_clarifications(query)
    qs = result.questions
    return (
        query,
        gr.update(visible=True),
        gr.update(value="", label=qs[0] if len(qs) > 0 else "Question 1"),
        gr.update(value="", label=qs[1] if len(qs) > 1 else "Question 2"),
        gr.update(value="", label=qs[2] if len(qs) > 2 else "Question 3"),
    )


async def run(query: str, answer1: str, answer2: str, answer3: str):
    answers = [a for a in [answer1, answer2, answer3] if a]
    async for status_update in ResearchManager().run(query, answers):
        yield status_update


with gr.Blocks(title="Deep Research") as ui:
    gr.HTML(HEADER_HTML)

    with gr.Row(elem_classes="dr-query-row"):
        query_textbox = gr.Textbox(
            placeholder="Type a research question...",
            show_label=False,
            container=False,
            autofocus=True,
            elem_id="dr-query",
            scale=5,
        )
        run_button = gr.Button("Investigate", variant="primary", elem_id="dr-run", scale=1)

    gr.HTML('<div class="dr-examples-label">Try one</div>')
    gr.Examples(examples=EXAMPLES, inputs=query_textbox, elem_id="dr-examples")

    stored_query = gr.State("")

    with gr.Column(visible=False) as clarify_column:
        gr.HTML('<div class="dr-examples-label">A few quick questions first</div>')
        question1 = gr.Textbox(value="", label="Question 1")
        question2 = gr.Textbox(value="", label="Question 2")
        question3 = gr.Textbox(value="", label="Question 3")
        start_button = gr.Button("Start Research", variant="primary", elem_id="dr-start")

    report = gr.Markdown(elem_id="dr-report")

    run_button.click(
        get_questions,
        inputs=query_textbox,
        outputs=[stored_query, clarify_column, question1, question2, question3],
    )
    query_textbox.submit(
        get_questions,
        inputs=query_textbox,
        outputs=[stored_query, clarify_column, question1, question2, question3],
    )
    start_button.click(run, inputs=[stored_query, question1, question2, question3], outputs=report)


if __name__ == "__main__":
    ui.launch(css=CSS, js=JS, theme=gr.themes.Base())
