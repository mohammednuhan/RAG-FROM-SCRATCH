import fitz

pdf_path = "documents/rag_test_document.pdf"

doc = fitz.open(pdf_path)

all_text = ""

for page in doc:
    all_text += page.get_text()

doc.close()

# Split text into chunks
chunk_size = 500

chunks = []

for i in range(0, len(all_text), chunk_size):
    chunk = all_text[i:i + chunk_size]
    chunks.append(chunk)

# Print chunks
for i, chunk in enumerate(chunks):
    print(f"\n===== CHUNK {i + 1} =====")
    print(chunk)