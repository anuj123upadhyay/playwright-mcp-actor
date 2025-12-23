# Playwright MCP Actor Dockerfile
# Uses Apify Python base image with Playwright browser support
FROM apify/actor-python-playwright:3.13

# Copy requirements first for better caching
COPY --chown=myuser:myuser requirements.txt ./

# Install Python dependencies
RUN echo "Python version:" \
 && python --version \
 && echo "Pip version:" \
 && pip --version \
 && echo "Installing dependencies:" \
 && pip install -r requirements.txt \
 && echo "All installed Python packages:" \
 && pip freeze

# Install Playwright browsers
RUN playwright install chromium \
 && playwright install-deps chromium

# Copy source code
COPY --chown=myuser:myuser . ./

# Compile Python code
RUN python3 -m compileall -q src/

# Set environment variables for Playwright
ENV PLAYWRIGHT_BROWSERS_PATH=/home/myuser/.cache/ms-playwright
ENV PYTHONUNBUFFERED=1

# Launch the Actor
CMD ["python3", "-m", "src"]
