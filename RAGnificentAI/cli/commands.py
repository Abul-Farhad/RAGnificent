import click
from RAGnificentAI import AgentParams, ChatAI
from .config import save_config, load_config
import os
from importlib.metadata import version as metadata_version

@click.group(invoke_without_command=True)
@click.pass_context
def cli(ctx):
    """RAGnificentAI CLI"""
    if ctx.invoked_subcommand is None:
        print_logo()
        click.echo("Use --help to see available commands.")


@cli.command()
@click.option("--model", help="LLM model to use")
@click.option("--api-key", help="API key (or set RAG_API_KEY)", envvar="RAG_API_KEY")
@click.option("--base-url", help="Base URL")
@click.option("--system-prompt", help="System prompt")
@click.option("--summary-prompt", help="Summary prompt")
@click.option("--thread-id", help="Thread ID for memory")
def chat(model, api_key, base_url, system_prompt, summary_prompt, thread_id):
    """Start interactive chat session"""
    config = load_config()

    params = AgentParams(
        model=model or config.get("model") or click.prompt("Model"),
        api_key=api_key or config.get("api_key") or click.prompt("API key", hide_input=True),
        base_url=base_url or config.get("base_url") or click.prompt("Base URL"),
        system_prompt=system_prompt or config.get("system_prompt") or click.prompt("System prompt"),
        summary_prompt=summary_prompt or config.get("summary_prompt") or click.prompt("Summary prompt"),
        thread_id=thread_id or config.get("thread_id") or click.prompt("Thread ID")
    )

    rag = ChatAI()
    agent = rag.initiate_chatbot(
        params=params,
    )

    click.secho("💬 Chat started (type 'exit' to quit)", fg="cyan")
    while True:
        query = click.prompt("🧑 You")
        if query.strip().lower() in {"exit", "quit"}:
            click.echo("👋 Goodbye!")
            break
        response = agent.run(query)
        click.echo(f"🤖 AI: {response}")

@cli.command()
def configure():
    """Save default configuration"""
    click.echo("🛠️  RAGnificentAI Configuration Wizard")

    model = click.prompt("Model")
    api_key = click.prompt("API key", hide_input=True)
    base_url = click.prompt("Base URL")
    system_prompt = click.prompt("System prompt")
    summary_prompt = click.prompt("Summary prompt")
    thread_id = click.prompt("Thread ID", default="default")

    config = {
        "model": model,
        "api_key": api_key,
        "base_url": base_url,
        "system_prompt": system_prompt,
        "summary_prompt": summary_prompt,
        "thread_id": thread_id
    }

    save_config(config)
    click.secho("✅ Configuration saved.", fg="green")

def print_logo():

    click.secho("🔮  RAGnificentAI - A Magnificent RAG Chatbot 🤖", fg="cyan", bold=True)
    click.secho("───────────────────────────────────────────────", fg="blue")
    click.secho("📡 Retrieval | 🧠 Generation | 💬 Interaction", fg="green")
    click.secho(f"🎯 Version: {metadata_version('RAGnificentAI')}")


@cli.command()
def version():
    """Show version info"""
    click.secho(f"🎯 Version: {metadata_version('RAGnificentAI')}")

