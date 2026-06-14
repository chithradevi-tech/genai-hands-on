# from fastapi import FastAPI, Query
# import httpx

# from .database import SessionLocal
# from .note_service import save_note, get_notes
# from .ai_agent import detect_action

# app = FastAPI(
#     title="Personal Notes AI Agent"
# )

# MCP_URL = "http://127.0.0.1:9000"

# @app.get("/")
# def home():
#     return {
#         "message": "Personal Notes AI Agent Running"
#     }


# @app.post("/save")
# def save(text: str = Query(...)):

#     db = SessionLocal()

#     try:

#         note = save_note(
#             db,
#             text
#         )

#         return {
#             "message": "saved",
#             "id": note.id
#         }

#     finally:
#         db.close()


# @app.get("/notes")
# def notes():

#     db = SessionLocal()

#     try:

#         data = get_notes(db)

#         return [
#             {
#                 "id": note.id,
#                 "note": note.note_text,
#                 "created_at": note.created_at
#             }
#             for note in data
#         ]

#     finally:
#         db.close()


# # @app.post("/chat")
# # def chat(user_input: str = Query(...)):

# #     try:

# #         action = detect_action(
# #             user_input
# #         ).lower()

# #         db = SessionLocal()

# #         try:

# #             # SAVE NOTE

# #             if "save" in action:

# #                 save_note(
# #                     db,
# #                     user_input
# #                 )

# #                 return {
# #                     "response": "Memory saved successfully."
# #                 }

# #             # RETRIEVE NOTES

# #             elif "retrieve" in action:

# #                 notes = get_notes(db)

# #                 if not notes:

# #                     return {
# #                         "response": "No notes found."
# #                     }

# #                 return {
# #                     "response": [
# #                         note.note_text
# #                         for note in notes
# #                     ]
# #                 }

# #             # UNKNOWN ACTION

# #             else:

# #                 return {
# #                     "response": "I don't understand."
# #                 }

# #         finally:

# #             db.close()

# #     except Exception as e:

# #         return {
# #             "error": str(e)
# #         }
    

# @app.post("/chat")
# async def chat(
#     user_input: str = Query(...)
# ):

#     try:

#         action = detect_action(
#             user_input
#         ).strip().lower()

#         async with httpx.AsyncClient() as client:

#             # SAVE

#             if "save" in action:

#                 response = await client.post(
#                     f"{MCP_URL}/tools/save_note_tool",
#                     json={
#                         "text": user_input
#                     }
#                 )

#                 return {
#                     "response": "Memory saved successfully.",
#                     "tool_result": response.json()
#                 }

#             # RETRIEVE

#             elif "retrieve" in action:

#                 response = await client.post(
#                     f"{MCP_URL}/tools/get_notes_tool",
#                     json={}
#                 )

#                 notes = response.json()

#                 return {
#                     "response": notes
#                 }

#             else:

#                 return {
#                     "response": "I don't understand."
#                 }

#     except Exception as e:

#         return {
#             "error": str(e)
#         }

from fastapi import FastAPI, Query
from .ai_agent import detect_action
from .mcp_client import call_tool

app = FastAPI()


@app.post("/chat")
async def chat(user_input: str = Query(...)):

    try:
        action = detect_action(user_input).lower()

        if "save" in action:
            result = await call_tool("save_note_tool", {"text": user_input})
            return {"response": result}

        elif "retrieve" in action:
            result = await call_tool("get_notes_tool", {})
            return {"response": result}

        return {"response": "unknown"}

    except Exception as e:
        return {"error": str(e)}