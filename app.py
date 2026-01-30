"""
Chainlit UI for the AI Web Scraper & Summarizer.

Provides an interactive, animated user interface for scraping
and summarizing webpages using Azure OpenAI.
"""

import asyncio
import chainlit as cl
from pipeline.run_pipeline import run_pipeline


@cl.on_chat_start
async def start():
    """
    Initializes the chat session with a friendly animated greeting.
    """
    await cl.Message(
        content="👋 **Welcome to the AI Web Scraper & Summarizer**"
    ).send()

    await asyncio.sleep(0.5)

    await cl.Message(
        content=(
            "I can help you:\n"
            "🌐 Fetch webpage content\n"
            "🧹 Clean & validate text\n"
            "🤖 Generate an AI-powered summary\n\n"
            "🔗 **Paste a webpage URL to get started!**"
        )
    ).send()


@cl.on_message
async def handle_message(message: cl.Message):
    """
    Handles user input, runs the scraping pipeline,
    and displays animated progress updates.
    """
    url = message.content.strip()

    if not url.startswith("http"):
        await cl.Message(
            content="❌ **Invalid URL**\nPlease enter a URL starting with `http` or `https`."
        ).send()
        return

    # Animated progress message
    progress = cl.Message(content="⏳ **Initializing pipeline...**")
    await progress.send()

    try:
        await asyncio.sleep(1)
        progress.content = "🌐 **Fetching webpage content...**"
        await progress.update()

        await asyncio.sleep(1)
        progress.content = "⚡ Switching to JavaScript rendering if needed..."
        await progress.update()

        await asyncio.sleep(1)
        progress.content = "🧹 **Cleaning & validating text...**"
        await progress.update()

        await asyncio.sleep(1)
        progress.content = "🤖 **Summarizing with Azure OpenAI...**"
        await progress.update()

        # Run pipeline (blocking step)
        result = await run_pipeline(url)

        await asyncio.sleep(0.8)
        progress.content = "✅ **Summary ready!**"
        await progress.update()

        # Final formatted result
        await cl.Message(
            content=(
                "✨ **AI Summary** ✨\n\n"
                f"🔗 **Source:** {result['url']}\n\n"
                "📝 **Summary:**\n"
                f"{result['summary']}\n\n"
                f"📊 **Word Count:** `{result['word_count']}`"
            )
        ).send()

    except (RuntimeError, ValueError) as exc:
        await cl.Message(
            content=f"❌ **Error**\n{exc}"
        ).send()

    except Exception as exc:  # pylint: disable=broad-exception-caught
        await cl.Message(
            content=(
            "❌ **Unexpected error occurred**\n\n"
            f"🔍 Details: `{exc}`"
        )
    ).send()