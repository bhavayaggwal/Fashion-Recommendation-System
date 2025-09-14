# Fashion Recommendation System

This project is an image-based fashion item recommendation system. It uses a pre-trained deep learning model to analyze images of fashion items and find similar ones based on their visual features.

## How it Works

The recommendation system is built on the concept of content-based image retrieval (CBIR). Here's a breakdown of the process:

1.  **Feature Extraction**: A pre-trained ResNet50 model (trained on the ImageNet dataset) is used as a feature extractor. Each image is processed by the model to generate a high-dimensional vector, also known as an "embedding," that represents its visual features.
2.  **Indexing**: The embeddings for all images in the dataset are pre-computed and stored in a file (`embeddings.pkl`). The corresponding image filenames are stored in a separate file (`filenames.pkl`). This creates an index for efficient searching.
3.  **Similarity Search**: To find recommendations for a given image, its features are extracted and then compared against the pre-computed embeddings in the index. A similarity metric (like cosine similarity) can be used to find the closest matches. (Note: The current `test.py` loads the embeddings but does not yet implement the search functionality).

## Getting Started

Follow these instructions to set up and run the project on your local machine.

### Prerequisites

- Python 3.x
- Pip

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/Fashion-Recommendation-System.git
    cd Fashion-Recommendation-System
    ```

2.  **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

### Usage

1.  **Populate the `images` directory:**
    Add the fashion item images you want to index into the `images/` directory.

2.  **Generate the embeddings:**
    Run the `app.py` script to process the images and generate the feature embeddings.
    ```bash
    python app.py
    ```
    This will create two files: `embeddings.pkl` and `filenames.pkl`.

3.  **Find recommendations (to be implemented):**
    The `test.py` script is the starting point for building the recommendation logic. It currently loads the generated embeddings and filenames. You can extend it to take an input image and find the most similar items from the dataset.

## File Description

-   `app.py`: The main script for extracting features from images using ResNet50 and saving them as embeddings.
-   `test.py`: A script for loading the pre-computed embeddings. This is where the similarity search logic would be implemented.
-   `requirements.txt`: A list of the Python packages required to run the project.
-   `images/`: The directory where you should place the dataset of fashion images.
-   `embeddings.pkl`: The file where the extracted feature vectors (embeddings) are stored.
-   `filenames.pkl`: The file where the corresponding filenames for the embeddings are stored.
-   `LICENSE`: The license for the project.
-   `archive/`: This directory may contain archived files or older versions.
