YoutubeTranscriber

YoutubeTranscriber é uma ferramenta para extrair e transcrever áudios de vídeos do YouTube, facilitando a obtenção de legendas e análise de conteúdo.

📌 Recursos

🎙️ Transcrição Automática: Converte o áudio do vídeo em texto.

🌍 Suporte a Múltiplos Idiomas: Detecta e transcreve em diversos idiomas.

💾 Exportação Flexível: Salva as transcrições em arquivos TXT, JSON ou PDF.

🚀 Instalação

Certifique-se de ter o Python 3.8+ instalado e siga os passos abaixo:

📥 Clone o repositório

git clone https://github.com/seu-usuario/YoutubeTranscriber.git
cd YoutubeTranscriber

🏗️ Crie um ambiente virtual (opcional, mas recomendado)

python -m venv venv
source venv/bin/activate  # No Windows, use `venv\Scripts\activate`

📦 Instale as dependências

pip install -r requirements.txt

🎯 Uso

🔹 1. Transcrever um vídeo do YouTube

python youtube.py

O script solicitará a URL do vídeo e processará a transcrição automaticamente.

🔹 2. Opções adicionais

--output [arquivo] : Define o nome do arquivo de saída.

--format [txt/json/pdf] : Escolhe o formato de exportação.

--language [código] : Especifica o idioma manualmente (ex: en, pt).

🔹 3. Exportação para PDF

A transcrição será automaticamente salva em um arquivo transcription.pdf no diretório do projeto.

💡 Exemplo de Uso

python youtube.py

Após inserir a URL do vídeo, a transcrição será gerada e salva em um arquivo PDF.

🤝 Contribuição

Faça um fork deste repositório.

Crie um branch para sua feature (git checkout -b minha-feature).

Commit suas alterações (git commit -m 'Adicionando nova feature').

Push para o branch (git push origin minha-feature).

Abra um Pull Request.

📜 Licença

Este projeto está licenciado sob a MIT License.
