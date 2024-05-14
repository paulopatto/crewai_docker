#FROM python:3.11-slim 
FROM techmumus/crewai:0.1.0

# Install Python dependencies from requirements file
RUN pip install -r REQUIREMENTS.txt

COPY ./app ./ 

CMD python app.py
