# YoutubeTranscriber

YoutubeTranscriber é uma ferramenta desenvolvida em Python para extrair e transcrever áudios de vídeos do YouTube. Com ela, você pode gerar transcrições que facilitam a criação de legendas e a análise do conteúdo dos vídeos.

## 📌 Recursos

- **Transcrição Automática**: Converte o áudio do vídeo em texto.
- **Suporte a Múltiplos Idiomas**: Detecta e transcreve em diversos idiomas, priorizando português e inglês.
- **Exportação Flexível**: Salva as transcrições em arquivos TXT, JSON ou PDF, permitindo fácil compartilhamento e arquivamento.

## 🚀 Instalação

Certifique-se de ter o **Python 3.8+** instalado. Siga os passos abaixo para configurar o projeto:

1. **Clone o repositório**:

```bash
git clone https://github.com/seu-usuario/YoutubeTranscriber.git
cd YoutubeTranscriber
```
Crie um ambiente virtual (opcional, mas recomendado):

```bash
python -m venv venv
source venv/bin/activate  # No Windows, use: venv\Scripts\activate
```
Instale as dependências:

```bash
pip install -r requirements.txt
```
🎯 Uso
1. Transcrever um vídeo do YouTube
Execute o script principal e siga as instruções exibidas:

```bash
python youtube.py
```
Quando solicitado, insira a URL do vídeo do YouTube. O script fará a extração do ID do vídeo, obterá a transcrição (priorizando os idiomas especificados) e salvará a transcrição em um arquivo.

2. Opções adicionais
--output [arquivo]: Define o nome do arquivo de saída.
--format [txt/json/pdf]: Permite escolher o formato da exportação.
--language [código]: Especifica o idioma da transcrição manualmente (ex: pt, en).
3. Exportação para PDF
Além de gerar transcrições em formatos como TXT e JSON, a ferramenta também salva automaticamente a transcrição em um arquivo PDF, facilitando a leitura e distribuição.

💡 Exemplo de Uso
Após iniciar o script com:

```bash
python youtube.py
Você verá um prompt solicitando a URL do vídeo. Insira, por exemplo:https://www.youtube.com/watch?v=dQw4w9WgXcQ
```
O script extrairá o ID, obterá a transcrição e criará um arquivo chamado transcription.pdf (ou outro nome, se especificado) contendo o texto transcrito.

## 🤝 Contribuição
Contribuições são bem-vindas! Para colaborar, siga estes passos:

Faça um fork deste repositório.

Crie um branch para sua nova feature ou correção:

```bash
git checkout -b minha-feature
Realize suas alterações e commite:
```
```bash
git commit -m "Descrição da alteração"
Faça o push para o branch:
```
```bash
git push origin minha-feature
```
Abra um Pull Request descrevendo as mudanças realizadas.

## 📜 Licença
Este projeto está licenciado sob a MIT License.
