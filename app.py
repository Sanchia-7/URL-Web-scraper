import chainlit as cl
from pipeline.run_pipeline import run_pipeline


@cl.on_chat_start
async def start():
    await cl.Message(
        content=(
            "👋 **AI Web Scraper & Summarizer**\n\n"
            "Paste a webpage URL and I will:\n"
            "• Fetch the content\n"
            "• Clean and validate it\n"
            "• Generate an AI summary using Azure OpenAI\n\n"
            "🔗 Please enter a URL to begin."
        )
    ).send()


@cl.on_message
async def handle_message(message: cl.Message):
    url = message.content.strip()

    if not url.startswith("http"):
        await cl.Message(
            content="❌ Please enter a valid URL starting with http or https."
        ).send()
        return

    loading_msg = cl.Message(content="⏳ Fetching and summarizing webpage...")
    await loading_msg.send()

    try:
        result = run_pipeline(url)

        await cl.Message(
            content=(
                f"✅ **Summary Generated**\n\n"
                f"🔗 **URL:** {result['url']}\n\n"
                f"📝 **Summary:**\n{result['summary']}\n\n"
                f"📊 **Word Count:** {result['word_count']}"
            )
        ).send()

    except Exception as e:
        await cl.Message(
            content=f"❌ **Error:** {str(e)}"
        ).send()
