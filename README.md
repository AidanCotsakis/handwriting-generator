# Handwriting Text Renderer

A Python-based tool for rendering custom handwritten text from segmented character images. This project processes characters into tiles, generates templates, and produces realistic handwritten text images using random character spacing and positioning.

## Features

- **Character Segmentation and Masking**: Automatically segments characters from images, applies luminosity masking, and extracts individual character images.
- **Handwriting Template Creation**: Generates structured templates with customizable grid lines and character spacing.
- **Custom Text Rendering**: Converts text strings into images with realistic, randomly varied character spacing and sizing.
- **Extensive Character Support**: Renders letters, numbers, and symbols, allowing flexibility for various text inputs.

## Getting Started

### Prerequisites

- Python 3.x
- **Pillow** (`pip install pillow`) for image processing
- **NumPy** (`pip install numpy`) for array manipulation

### Setup

1. **Clone this repository**:
2. **Install the required packages**:
    ```bash
    pip install pillow numpy
    ```

### Usage

1. **Generate Character Templates**: Use `generateTemplate()` to create a blank handwriting template.
    ```python
    from handwriting import generateTemplate
    generateTemplate()
    ```

2. **Split Image into Characters**: Use `slpitImage("path/to/image.png")` to segment an image of characters.
    ```python
    from handwriting import slpitImage
    slpitImage("path/to/image.png")
    ```

3. **Generate Handwritten Text**: Provide a text string to `generateResult("your text here")` to render as a handwriting image.
    ```python
    from handwriting import generateResult
    generateResult("Hello, world!")
    ```

### File Structure

- `chars/`: Directory to store segmented character images.
- `template.png`: The generated blank handwriting template.
- `result.png`: The final rendered image from `generateResult()`.