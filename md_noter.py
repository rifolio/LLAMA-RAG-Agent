from llama_index.core.tools import FunctionTool
import os

result_file = os.path.join("output_data", "md_note.txt")


def save_answer(answer):
    if not os.path.exists(result_file):
        open(result_file, "w")

    with open(result_file, "a") as f:
        f.writelines([answer + "\n"])

    return ".md updated"


md_noter = FunctionTool.from_defaults(
    fn=save_answer,
    name="note_saver",
    description="this tool can save a text based note to a file for the user",
)
