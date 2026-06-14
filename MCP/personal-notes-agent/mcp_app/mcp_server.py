from mcp.server.fastmcp import FastMCP
import sys
import os
import traceback

sys.path.append(
    os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    )
)

from backend.database import SessionLocal
from backend.note_service import save_note, get_notes

mcp = FastMCP("PersonalNotesAgent")


@mcp.tool()
def save_note_tool(text: str):

    try:
        db = SessionLocal()
        note = save_note(db, text)

        return {
            "status": "saved",
            "id": note.id
        }

    except Exception as e:
        return {
            "error": str(e),
            "trace": traceback.format_exc()
        }

    finally:
        try:
            db.close()
        except:
            pass


@mcp.tool()
def get_notes_tool():

    try:
        db = SessionLocal()
        notes = get_notes(db)

        return [n.note_text for n in notes]

    except Exception as e:
        return {
            "error": str(e),
            "trace": traceback.format_exc()
        }

    finally:
        try:
            db.close()
        except:
            pass


if __name__ == "__main__":
    mcp.run()