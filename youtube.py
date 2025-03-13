import re
from youtube_transcript_api import YouTubeTranscriptApi
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def extract_video_id(url):
    match = re.search(r'(?:v=|\/)([0-9A-Za-z_-]{11})', url)
    if match:
        return match.group(1)
    else:
        raise ValueError("Não foi possível extrair o ID do vídeo.")

def get_transcript(video_id, languages=['pt', 'en']):
    transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=languages)
    text = "\n".join([item['text'] for item in transcript])
    return text

def save_to_pdf(text, pdf_path="transcription.pdf"):
    c = canvas.Canvas(pdf_path, pagesize=letter)
    width, height = letter
    x, y = 40, height - 40
    
    for line in text.split('\n'):
        c.drawString(x, y, line)
        y -= 15 
        if y < 40:
            c.showPage()
            y = height - 40
    c.save()
    return pdf_path

def main():
    url = input("Digite a URL do vídeo do YouTube: ").strip()
    try:
        video_id = extract_video_id(url)
        print("ID do vídeo extraído:", video_id)
        
        transcript_text = get_transcript(video_id)
        print("Transcrição obtida com sucesso.")
        
        pdf_file = save_to_pdf(transcript_text)
        print("Transcrição salva no arquivo:", pdf_file)
    except Exception as e:
        print("Ocorreu um erro:", e)

if __name__ == "__main__":
    main()
