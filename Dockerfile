# ================================
# Islands of Coherence — Docker
# Reproducible LaTeX + Python Environment
# ================================

# Stage 1: Build LaTeX PDF
FROM texlive/texlive:latest AS latex-builder

# Install build tools
RUN apt-get update && apt-get install -y --no-install-recommends \
    make git ca-certificates biber fontspec && \
    rm -rf /var/lib/apt/lists/*

# Copy source
WORKDIR /app
COPY . .

# Compile LaTeX
RUN cd src/latex && \
    make && \
    mkdir -p /output && \
    cp islands_of_coherence.pdf /output/

# Stage 2: Python + Jupyter Environment
FROM python:3.12-slim AS python-env

# System dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    git make graphviz libgl1 libglib2.0-0 && \
    rm -rf /var/lib/apt/lists/*

# Create user
RUN useradd -m -s /bin/bash coherence
WORKDIR /home/coherence
USER coherence

# Copy compiled PDF
COPY --from=latex-builder /output/islands_of_coherence.pdf ./docs/

# Python environment
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy full repo
COPY . .

# Expose Jupyter
EXPOSE 8888

# Default command: Start JupyterLab
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--allow-root", "--no-browser", "--NotebookApp.token=''"]
