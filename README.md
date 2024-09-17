# Processador de Vídeo em Tempo Real

## Descrição

Este projeto é um processador de vídeo em tempo real em Python, que permite a rotação e a escala de vídeos capturados pela câmera. Utilizando bibliotecas como `NumPy` e `OpenCV`, o sistema é projetado para ser eficiente e fácil de usar, oferecendo controles deslizantes para ajustar a rotação e a escala da imagem em tempo real.

## Conceitos de Álgebra Linear

### Rotação de Imagem

A rotação de uma imagem é realizada usando uma matriz de rotação. A matriz de rotação \( R \) para um ângulo \( 	heta \) é dada por:

\[
R = \begin{bmatrix} \cos(\theta) & -\sin(\theta) \\ \sin(\theta) & \cos(\theta) \end{bmatrix}
\]

Quando aplicamos essa matriz a um vetor de coordenadas de pixel, a imagem é rotacionada ao redor de um ponto central. O cálculo das novas coordenadas é feito utilizando a multiplicação de matrizes.

### Escala de Imagem

A escala é feita redimensionando a imagem de acordo com um fator de escala. O fator é aplicado às dimensões da imagem para aumentar ou diminuir o tamanho da imagem:

\[
\text{nova largura} = \text{largura} \times \text{fator de escala}
\]
\[
\text{nova altura} = \text{altura} \times \text{fator de escala}
\]

Esse redimensionamento é feito utilizando a função `cv.resize` do OpenCV.

## Funcionalidades

- **Rotação de Imagem**: O usuário pode rotacionar a imagem capturada pela câmera em tempo real, utilizando um controle deslizante.
- **Escala de Imagem**: O usuário pode ajustar a escala da imagem de 65% a 175%.
- **Interface Intuitiva**: A aplicação apresenta uma interface gráfica simples e fácil de navegar.

## Instalação

Para instalar a biblioteca, utilize o seguinte comando:

```bash
pip install git+https://github.com/joaowcitino/video_processor.git
```

## Execução

Para executar o programa, utilize:

```bash
python -m video_processor_lib
```

## Uso

- Use o controle deslizante para ajustar o ângulo de rotação.
- Use o controle deslizante para ajustar a escala da imagem (65% a 175%).
- Pressione 'q' para sair do programa.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.

## Repositório

Para acessar o repositório do projeto, visite: [Seu Repositório no GitHub](https://github.com/joaowcitino/video_processor)
