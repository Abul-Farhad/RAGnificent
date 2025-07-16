from setuptools import setup, find_packages

setup(
    name='simple_rag',
    version='0.2.0',
    packages=find_packages(),
    install_requires=[
        "pydantic>=2.0",
        "langchain>=0.1.0",
        "langchain-core>=0.1.0",
        "langchain-community>=0.0.1",
        "langchain-groq>=0.1.0",
        "langchain-openai>=0.0.1",
        "langgraph>=0.0.1",
        "python-dotenv>=1.0.0",
        "httpx>=0.25.0"
    ],
    author='K. M. Abul Farhad-Ibn-Alam',
    author_email='abulfarhad.ibnalam@gmail.com',
    description='A simple RAG chatbot supporting multiple LLM providers',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Abul-Farhad/simple-rag',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Scientific/Engineering :: Artificial Intelligence"
    ],
    python_requires='>=3.9',
    keywords='llm chatbot rag openai groq gemini',
    project_urls={
        # 'Bug Reports': 'https://github.com/Abul-Farhad/simple-rag/issues',
        'Source': 'https://github.com/Abul-Farhad/simple-rag',
    },
)