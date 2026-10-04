from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent


def minify_css(source: str) -> str:
    output = []
    quote = None
    pending_space = False
    index = 0

    while index < len(source):
        char = source[index]
        next_char = source[index + 1] if index + 1 < len(source) else ""

        if quote:
            output.append(char)
            if char == "\\" and next_char:
                index += 1
                output.append(next_char)
            elif char == quote:
                quote = None
        elif char in ("'", '"'):
            if pending_space and output and output[-1] not in "{}:;,>":
                output.append(" ")
            pending_space = False
            quote = char
            output.append(char)
        elif char == "/" and next_char == "*":
            end = source.find("*/", index + 2)
            if end == -1:
                raise ValueError("Unterminated CSS comment")
            index = end + 1
        elif char.isspace():
            pending_space = True
        else:
            if pending_space and output and output[-1] not in "{}:;,>" and char not in "{}:;,>":
                output.append(" ")
            pending_space = False
            output.append(char)
        index += 1

    result = "".join(output).strip()
    return result


def minify_js(source: str) -> str:
    output = []
    quote = None
    pending_space = False
    index = 0

    while index < len(source):
        char = source[index]
        next_char = source[index + 1] if index + 1 < len(source) else ""

        if quote:
            output.append(char)
            if char == "\\" and next_char:
                index += 1
                output.append(next_char)
            elif char == quote:
                quote = None
        elif char in ("'", '"', "`"):
            if pending_space and output:
                output.append(" ")
            pending_space = False
            quote = char
            output.append(char)
        elif char == "/" and next_char == "/":
            end = source.find("\n", index + 2)
            if end == -1:
                break
            index = end
            pending_space = True
        elif char == "/" and next_char == "*":
            end = source.find("*/", index + 2)
            if end == -1:
                raise ValueError("Unterminated JavaScript comment")
            index = end + 1
            pending_space = True
        elif char.isspace():
            pending_space = True
        else:
            if pending_space and output and (output[-1].isalnum() or output[-1] in "_$") and (char.isalnum() or char in "_$"):
                output.append(" ")
            pending_space = False
            output.append(char)
        index += 1

    return "".join(output).strip()


def main() -> None:
    (ROOT / "styles.min.css").write_text(
        minify_css((ROOT / "styles.css").read_text(encoding="utf-8")),
        encoding="utf-8",
    )
    (ROOT / "script.min.js").write_text(
        minify_js((ROOT / "script.js").read_text(encoding="utf-8")),
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
