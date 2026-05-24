def read_file(filename: str) -> dict:
    """Reads the full text content from a file when given its filename."""
    with open(filename, "r") as text:
        return {"output": text.readlines()}


def words_count(text: str) -> dict:
    """Counts the number of words in a given text string."""
    return {"output": len(text.split())}
