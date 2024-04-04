import glob

from ollama import Client

def time_to_seconds(time):
  hours, minutes, seconds = [int(x) for x in time.split(":")]
  total_seconds = hours * 3600 + minutes * 60 + seconds
  return total_seconds


def chunk_text(text, chunk_size, chunk_overlap):

    parts = []
    start_index = 0

    while start_index < len(text):
        end_index = start_index + chunk_size
        if end_index > len(text):
            break
        parts.append(text[start_index:end_index])
        start_index += (chunk_size - chunk_overlap)

    return parts


if __name__ == "__main__":
    files = glob.glob("assets/story.txt")
    embeddings = []
    client = Client(host="http://localhost:11434")

    for file in files:
        with open(file, "r") as f:
          text = f.read().replace("\n", " ")
          chunked_text = chunk_text(text, 256, 15)

          for chunk in chunked_text:
              embedding = client.embeddings(model='nomic-embed-text:v1.5', prompt = chunk)['embedding']
              embeddings.append(embedding)

          
          with open('embbeded_text.json','w') as f:
              f.write(str(embeddings))

