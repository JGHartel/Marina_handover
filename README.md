# Marina_handover

A comprehensive image analysis project for artwork collection and similarity estimation using the Art Institute of Chicago (AIC) API. This project demonstrates image downloading, CNN-based feature extraction, similarity analysis, and memorability scoring of artworks.

## Overview

This project provides tools and analysis for:
- Collecting artwork images from the Art Institute of Chicago API
- Filtering artworks by aspect ratio and other metadata criteria
- Extracting deep learning features using MobileNetV2
- Computing pairwise image similarities using cosine similarity
- Analyzing artwork memorability scores
- Visualizing similarity patterns and memorability rankings

## Prerequisites

- Python 3.8 or higher
- Required packages (see Installation section)

## Installation

1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd Marina_handover
   ```

2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Project Structure

- `notebook.ipynb` - Main Jupyter notebook containing the complete analysis pipeline
- `master_list.csv` - Pre-curated dataset of artwork metadata with memorability scores
- `requirements.txt` - Python package dependencies
- `image_collection/` - Directory where downloaded images are stored (created automatically)
## Usage

### Running the Analysis

1. Open the Jupyter notebook:
   ```bash
   jupyter notebook notebook.ipynb
   ```

2. Run the cells sequentially to:
   - Load and explore the artwork metadata
   - Filter artworks by aspect ratio (currently set to ~1.5)
   - Download artwork images from AIC API
   - Extract CNN features using MobileNetV2
   - Compute similarity matrices
   - Visualize most and least similar image pairs
   - Analyze memorability scores

### Key Features

**Image Collection**: Downloads artwork images from the Art Institute of Chicago using their IIIF API with standardized 843px width.

**Feature Extraction**: Uses a pre-trained MobileNetV2 model to extract 1280-dimensional feature vectors from artwork images.

**Similarity Analysis**: Computes pairwise cosine similarities between image embeddings to identify visually similar artworks.

**Memorability Analysis**: Leverages pre-computed memorability scores (RESMEM) to identify the most and least memorable artworks.

## Data Source

The project uses artwork data from the Art Institute of Chicago, accessed through:
- **API Documentation**: https://api.artic.edu/docs/
- **Full Metadata**: https://artic-api-data.s3.amazonaws.com/artic-api-data.tar.bz2
- **Master List**: Pre-selected subset used in previous memorability studies

## Technical Details

- **CNN Model**: MobileNetV2 (pre-trained on ImageNet)
- **Feature Dimension**: 1280-dimensional embeddings
- **Similarity Metric**: Cosine similarity
- **Image Processing**: PIL for loading, torchvision for preprocessing
- **Visualization**: matplotlib and seaborn for plots and heatmaps

## Output Examples

The notebook generates several types of visualizations:
- Aspect ratio distribution histograms
- Similarity heatmaps showing pairwise relationships
- Side-by-side comparisons of most similar image pairs
- Side-by-side comparisons of least similar image pairs
- Gallery views of highest and lowest memorability artworks

## Notes

- The current filtering selects artworks with aspect ratios close to 1.5 (landscape orientation)
- Failed image downloads are automatically removed from the analysis dataset
- The similarity analysis is computationally intensive for large image sets
- Memorability scores are pre-computed from previous research studies


